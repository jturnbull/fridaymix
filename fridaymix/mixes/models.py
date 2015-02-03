from django.db import models
import datetime
from lxml import etree
from django.db.models import Sum

class Mix(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    icon = models.ImageField(upload_to="icons/")
    start = models.DateTimeField(default=lambda: datetime.datetime.now().replace(hour=12, minute=30, second=0, microsecond=0))
    end = models.DateTimeField(default=lambda: datetime.datetime.now().replace(hour=14, minute=00, second=0, microsecond=0))
    playlist = models.URLField(verify_exists=True)
    tracks_input = models.TextField(blank=True, null=True)
    tracks = models.ManyToManyField('Track', through='MixTrack')
    
    class Meta:
        ordering = ('-start',)
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if self.tracks_input:
            # delete all
            self.tracks.clear()
            
            for counter, track in enumerate(self.tracks_input.split('\r\n')):
                track, created = Track.objects.get_or_create(track_uri=track)
                
                if not track.completed:
                    track.complete()
                    
                MixTrack.objects.create(mix=self, track=track, mixtrack_number=counter)

            self.tracks_input = None
        return super(Mix, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('mix', (), { 'slug': self.slug })
    
    @property
    def upcoming(self):
        if datetime.datetime.now() < self.start:
            return True
        return False
    
    @property
    def active(self):
        if self.upcoming and datetime.datetime.now() < self.end:
            return True
        return False
        
    @property
    def length(self):
        return self.tracks.aggregate(Sum('length'))['length__sum']
        
    @property
    def length_display(self):
        if self.length:
            return "%s" % datetime.timedelta(seconds=int(self.length))
        return "00:00"
    
        
class MixTrack(models.Model):
    """Intermediary table to hold track's order in the mix"""
    
    mix = models.ForeignKey(Mix)
    track = models.ForeignKey('Track')
    mixtrack_number = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s track %s" % (self.mix.slug, self.mixtrack_number)


class Track(models.Model):
    """Track details loaded from Spotify API"""

    track_uri = models.CharField(blank=True, max_length=255)
    track_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, max_length=255)
    artist = models.CharField(blank=True, max_length=255)
    artist_uri = models.CharField(blank=True, max_length=255)
    album = models.CharField(blank=True, max_length=255)
    album_uri = models.CharField(blank=True, max_length=255)
    isrc = models.CharField(blank=True, max_length=255)
    length = models.FloatField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s - %s (%s)" % (self.artist, self.name, self.album)
        
    def get_absolute_url(self):
        return self.track_uri
        
    @property
    def length_display(self):
        if self.length:
            td = datetime.timedelta(seconds=int(self.length))
            return ':'.join(str(td).split(':')[-2:])
        return "00:00"            
    
    def complete(self):
        
        self.track_uri = self.track_uri.strip()
        
        url = self.track_uri.replace('http://open.spotify.com/track/', 'http://ws.spotify.com/lookup/1/?uri=spotify:track:')
        tree = etree.parse(url).getroot()
        
        track_number = tree.findall('{http://www.spotify.com/ns/music/1}track-number')
        if track_number:
            self.track_number = track_number[0].text
        
        names = tree.findall('{http://www.spotify.com/ns/music/1}name')
        if names:
            self.name = names[0].text
            
        artists = tree.findall('{http://www.spotify.com/ns/music/1}artist')
        if artists:
            artist = artists[0]
            if 'href' in artist.attrib:
                self.artist_uri = artist.attrib['href']
                
            names = artist.findall('{http://www.spotify.com/ns/music/1}name')
            if names:
                self.artist = names[0].text
                
        albums = tree.findall('{http://www.spotify.com/ns/music/1}album')
        if albums:
            album = albums[0]
            if 'href' in album.attrib:
                self.album_uri = album.attrib['href']
                
            names = album.findall('{http://www.spotify.com/ns/music/1}name')
            if names:
                self.album = names[0].text
                
        length = tree.findall('{http://www.spotify.com/ns/music/1}length')
        if length:
            self.length = length[0].text
        
        popularity = tree.findall('{http://www.spotify.com/ns/music/1}popularity')
        if popularity:
            self.popularity = popularity[0].text
            
            
        isrc = tree.findall('{http://www.spotify.com/ns/music/1}id') #FIXME: sesrch for only type = irsc (are there others?)
        if isrc:
            self.isrc = isrc[0].text
            
        self.completed = True
        
        import time
        # slow down for rate-limited api calls
        time.sleep(0.2)
        
        self.save()


    
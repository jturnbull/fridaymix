# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Track.track_uri'
        db.add_column('mixes_track', 'track_uri', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Track.completed'
        db.add_column('mixes_track', 'completed', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Changing field 'Track.album'
        db.alter_column('mixes_track', 'album', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))

        # Changing field 'Track.name'
        db.alter_column('mixes_track', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))

        # Changing field 'Track.artist_uri'
        db.alter_column('mixes_track', 'artist_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))

        # Changing field 'Track.album_uri'
        db.alter_column('mixes_track', 'album_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))

        # Changing field 'Track.isrc'
        db.alter_column('mixes_track', 'isrc', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Track.track_uri'
        db.delete_column('mixes_track', 'track_uri')

        # Deleting field 'Track.completed'
        db.delete_column('mixes_track', 'completed')

        # Changing field 'Track.album'
        db.alter_column('mixes_track', 'album', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))

        # Changing field 'Track.name'
        db.alter_column('mixes_track', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))

        # Changing field 'Track.artist_uri'
        db.alter_column('mixes_track', 'artist_uri', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))

        # Changing field 'Track.album_uri'
        db.alter_column('mixes_track', 'album_uri', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))

        # Changing field 'Track.isrc'
        db.alter_column('mixes_track', 'isrc', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))


    models = {
        'mixes.mix': {
            'Meta': {'object_name': 'Mix'},
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 24, 14, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 24, 12, 30)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tracks_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'mixes.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'album_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'artist_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isrc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mix': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': "orm['mixes.Mix']"}),
            'mixtrack_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'track_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['mixes']

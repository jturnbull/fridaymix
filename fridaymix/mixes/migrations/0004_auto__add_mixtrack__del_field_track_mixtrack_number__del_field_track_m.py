# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MixTrack'
        db.create_table('mixes_mixtrack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mixes.Mix'])),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mixes.Track'])),
            ('mixtrack_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('mixes', ['MixTrack'])

        # Deleting field 'Track.mixtrack_number'
        db.delete_column('mixes_track', 'mixtrack_number')

        # Deleting field 'Track.mix'
        db.delete_column('mixes_track', 'mix_id')


    def backwards(self, orm):
        
        # Deleting model 'MixTrack'
        db.delete_table('mixes_mixtrack')

        # Adding field 'Track.mixtrack_number'
        db.add_column('mixes_track', 'mixtrack_number', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Track.mix'
        db.add_column('mixes_track', 'mix', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='tracks', to=orm['mixes.Mix']), keep_default=False)


    models = {
        'mixes.mix': {
            'Meta': {'object_name': 'Mix'},
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 25, 14, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 25, 12, 30)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mixes.Track']", 'through': "orm['mixes.MixTrack']", 'symmetrical': 'False'}),
            'tracks_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'mixes.mixtrack': {
            'Meta': {'object_name': 'MixTrack'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mixes.Mix']"}),
            'mixtrack_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mixes.Track']"})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'track_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['mixes']

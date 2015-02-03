# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Track'
        db.create_table('mixes_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mix', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['mixes.Mix'])),
            ('mixtrack_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('track_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('artist_uri', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('album', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('album_uri', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('isrc', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('length', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('popularity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('mixes', ['Track'])

        # Adding field 'Mix.tracks_input'
        db.add_column('mixes_mix', 'tracks_input', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Track'
        db.delete_table('mixes_track')

        # Deleting field 'Mix.tracks_input'
        db.delete_column('mixes_mix', 'tracks_input')


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
            'album': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'album_uri': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'artist_uri': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mix': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': "orm['mixes.Mix']"}),
            'mixtrack_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'popularity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mixes']

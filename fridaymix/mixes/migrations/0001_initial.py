# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Mix'
        db.create_table('mixes_mix', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 24, 12, 30))),
            ('end', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 24, 14, 0))),
            ('playlist', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('mixes', ['Mix'])


    def backwards(self, orm):
        
        # Deleting model 'Mix'
        db.delete_table('mixes_mix')


    models = {
        'mixes.mix': {
            'Meta': {'object_name': 'Mix'},
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 24, 14, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlist': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 24, 12, 30)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mixes']

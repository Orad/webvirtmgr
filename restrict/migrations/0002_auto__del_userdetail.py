# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserDetail'
        db.delete_table(u'restrict_userdetail')


    def backwards(self, orm):
        # Adding model 'UserDetail'
        db.create_table(u'restrict_userdetail', (
            ('token', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='user_detail', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'restrict', ['UserDetail'])


    models = {
        u'restrict.restrictinfrastructure': {
            'Meta': {'object_name': 'RestrictInfrastructure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['restrict']
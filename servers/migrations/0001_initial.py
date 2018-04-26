# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compute'
        db.create_table(u'servers_compute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compute_organization', to=orm['organizations.Organization'])),
        ))
        db.send_create_signal(u'servers', ['Compute'])


    def backwards(self, orm):
        # Deleting model 'Compute'
        db.delete_table(u'servers_compute')


    models = {
        u'organizations.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'servers.compute': {
            'Meta': {'object_name': 'Compute'},
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compute_organization'", 'to': u"orm['organizations.Organization']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['servers']
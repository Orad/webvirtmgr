# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instance'
        db.create_table(u'instance_instance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servers.Compute'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36)),
        ))
        db.send_create_signal(u'instance', ['Instance'])

        # Adding model 'RunningHistory'
        db.create_table(u'instance_runninghistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['instance.Instance'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'instance', ['RunningHistory'])

        # Adding model 'RunningInstanceTime'
        db.create_table(u'instance_runninginstancetime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['instance.Instance'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('total_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'instance', ['RunningInstanceTime'])


    def backwards(self, orm):
        # Deleting model 'Instance'
        db.delete_table(u'instance_instance')

        # Deleting model 'RunningHistory'
        db.delete_table(u'instance_runninghistory')

        # Deleting model 'RunningInstanceTime'
        db.delete_table(u'instance_runninginstancetime')


    models = {
        u'instance.instance': {
            'Meta': {'object_name': 'Instance'},
            'compute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servers.Compute']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        },
        u'instance.runninghistory': {
            'Meta': {'object_name': 'RunningHistory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['instance.Instance']"})
        },
        u'instance.runninginstancetime': {
            'Meta': {'object_name': 'RunningInstanceTime'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['instance.Instance']"}),
            'total_time': ('django.db.models.fields.TimeField', [], {})
        },
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

    complete_apps = ['instance']
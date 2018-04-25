# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RunningInstanceTime.daily_time'
        db.add_column(u'instance_runninginstancetime', 'daily_time',
                      self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=20, decimal_places=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RunningInstanceTime.daily_time'
        db.delete_column(u'instance_runninginstancetime', 'daily_time')


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
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['instance.Instance']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'instance.runninginstancetime': {
            'Meta': {'object_name': 'RunningInstanceTime'},
            'daily_time': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '20', 'decimal_places': '4'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['instance.Instance']"}),
            'total_time': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '20', 'decimal_places': '4'})
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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Net2_edge'
        db.create_table('bitcoinapp_net2_edge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_from', to=orm['bitcoinapp.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_to', to=orm['bitcoinapp.User'])),
            ('val', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('bitcoinapp', ['Net2_edge'])


    def backwards(self, orm):
        # Deleting model 'Net2_edge'
        db.delete_table('bitcoinapp_net2_edge')


    models = {
        'bitcoinapp.address': {
            'Meta': {'object_name': 'Address'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.User']", 'null': 'True', 'blank': 'True'}),
            'val': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '34'})
        },
        'bitcoinapp.block': {
            'Meta': {'object_name': 'Block'},
            'created': ('django.db.models.fields.DateField', [], {}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bitcoinapp.net1_edge': {
            'Meta': {'object_name': 'Net1_edge'},
            'addr1': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'addr2': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bitcoinapp.net2_edge': {
            'Meta': {'object_name': 'Net2_edge'},
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_from'", 'to': "orm['bitcoinapp.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_to'", 'to': "orm['bitcoinapp.User']"}),
            'val': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'bitcoinapp.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Block']"}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bitcoinapp.tx_input': {
            'Meta': {'object_name': 'Tx_input'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Address']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Transaction']"})
        },
        'bitcoinapp.tx_output': {
            'Meta': {'object_name': 'Tx_output'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Address']"}),
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Transaction']"})
        },
        'bitcoinapp.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userid': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['bitcoinapp']
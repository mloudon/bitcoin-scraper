# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'User', fields ['username']
        db.delete_unique('bitcoinapp_user', ['username'])


    def backwards(self, orm):
        # Adding unique constraint on 'User', fields ['username']
        db.create_unique('bitcoinapp_user', ['username'])


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
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bitcoinapp.Block']", 'null': 'True', 'blank': 'True'}),
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
            'date_last': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_reg': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numposts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profileurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.BigIntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bitcoinapp']
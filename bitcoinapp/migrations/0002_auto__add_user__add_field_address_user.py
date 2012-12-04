# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('bitcoinapp_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('bitcoinapp', ['User'])

        # Adding field 'Address.user'
        db.add_column('bitcoinapp_address', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('bitcoinapp_user')

        # Deleting field 'Address.user'
        db.delete_column('bitcoinapp_address', 'user_id')


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
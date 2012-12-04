# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('bitcoinapp_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('val', self.gf('django.db.models.fields.CharField')(unique=True, max_length=34)),
        ))
        db.send_create_signal('bitcoinapp', ['Address'])

        # Adding model 'Block'
        db.create_table('bitcoinapp_block', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1000)),
            ('created', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('bitcoinapp', ['Block'])

        # Adding model 'Transaction'
        db.create_table('bitcoinapp_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1000)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.Block'])),
        ))
        db.send_create_signal('bitcoinapp', ['Transaction'])

        # Adding model 'Tx_input'
        db.create_table('bitcoinapp_tx_input', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.Address'])),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.Transaction'])),
        ))
        db.send_create_signal('bitcoinapp', ['Tx_input'])

        # Adding model 'Tx_output'
        db.create_table('bitcoinapp_tx_output', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.Address'])),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bitcoinapp.Transaction'])),
        ))
        db.send_create_signal('bitcoinapp', ['Tx_output'])

        # Adding model 'Net1_edge'
        db.create_table('bitcoinapp_net1_edge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addr1', self.gf('django.db.models.fields.CharField')(max_length=34)),
            ('addr2', self.gf('django.db.models.fields.CharField')(max_length=34)),
        ))
        db.send_create_signal('bitcoinapp', ['Net1_edge'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('bitcoinapp_address')

        # Deleting model 'Block'
        db.delete_table('bitcoinapp_block')

        # Deleting model 'Transaction'
        db.delete_table('bitcoinapp_transaction')

        # Deleting model 'Tx_input'
        db.delete_table('bitcoinapp_tx_input')

        # Deleting model 'Tx_output'
        db.delete_table('bitcoinapp_tx_output')

        # Deleting model 'Net1_edge'
        db.delete_table('bitcoinapp_net1_edge')


    models = {
        'bitcoinapp.address': {
            'Meta': {'object_name': 'Address'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        }
    }

    complete_apps = ['bitcoinapp']
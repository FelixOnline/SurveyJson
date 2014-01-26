# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Option'
        db.create_table(u'questions_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'questions', ['Option'])


    def backwards(self, orm):
        # Deleting model 'Option'
        db.delete_table(u'questions_option')


    models = {
        u'questions.option': {
            'Meta': {'object_name': 'Option'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['questions']
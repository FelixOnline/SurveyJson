# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'questions_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.CharField')(default='r', max_length=1)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('inline', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('reverse', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'questions', ['Question'])

        # Adding model 'Dependency'
        db.create_table(u'questions_dependency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_id', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Dependencies', to=orm['questions.Question'])),
        ))
        db.send_create_signal(u'questions', ['Dependency'])

        # Adding field 'Option.question'
        db.add_column(u'questions_option', 'question',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='Options', to=orm['questions.Question']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'questions_question')

        # Deleting model 'Dependency'
        db.delete_table(u'questions_dependency')

        # Deleting field 'Option.question'
        db.delete_column(u'questions_option', 'question_id')


    models = {
        u'questions.dependency': {
            'Meta': {'object_name': 'Dependency'},
            '_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Dependencies'", 'to': u"orm['questions.Question']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'questions.option': {
            'Meta': {'object_name': 'Option'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Options'", 'to': u"orm['questions.Question']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            'default': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'r'", 'max_length': '1'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'reverse': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['questions']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table(u'citi_digits_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'citi_digits', ['School'])

        # Adding model 'Teacher'
        db.create_table(u'citi_digits_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citi_digits.School'])),
            ('className', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'citi_digits', ['Teacher'])

        # Adding model 'Team'
        db.create_table(u'citi_digits_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citi_digits.Teacher'])),
        ))
        db.send_create_signal(u'citi_digits', ['Team'])

        # Adding model 'Student'
        db.create_table(u'citi_digits_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citi_digits.Team'])),
        ))
        db.send_create_signal(u'citi_digits', ['Student'])

        # Adding model 'CityDigitsUser'
        db.create_table(u'citi_digits_citydigitsuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('entityId', self.gf('django.db.models.fields.IntegerField')()),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'citi_digits', ['CityDigitsUser'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table(u'citi_digits_school')

        # Deleting model 'Teacher'
        db.delete_table(u'citi_digits_teacher')

        # Deleting model 'Team'
        db.delete_table(u'citi_digits_team')

        # Deleting model 'Student'
        db.delete_table(u'citi_digits_student')

        # Deleting model 'CityDigitsUser'
        db.delete_table(u'citi_digits_citydigitsuser')


    models = {
        u'citi_digits.citydigitsuser': {
            'Meta': {'object_name': 'CityDigitsUser'},
            'entityId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'citi_digits.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'citi_digits.student': {
            'Meta': {'object_name': 'Student'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Team']"})
        },
        u'citi_digits.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'className': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.School']"})
        },
        u'citi_digits.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Teacher']"})
        }
    }

    complete_apps = ['citi_digits']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'citi_digits_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'citi_digits', ['Location'])

        # Adding model 'Interview'
        db.create_table(u'citi_digits_interview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citi_digits.Student'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citi_digits.Location'])),
            ('interviewType', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('entityId', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'citi_digits', ['Interview'])

        # Adding model 'InterviewPlayer'
        db.create_table(u'citi_digits_interviewplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('do_you_ever_buy_lottery_tickets', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('why_or_why_not_audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('have_you_ever_won_the_lottery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('most_won', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('money_spent_on_lottery_in_average_week', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('jackpot_audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'citi_digits', ['InterviewPlayer'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'citi_digits_location')

        # Deleting model 'Interview'
        db.delete_table(u'citi_digits_interview')

        # Deleting model 'InterviewPlayer'
        db.delete_table(u'citi_digits_interviewplayer')


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
        u'citi_digits.interview': {
            'Meta': {'object_name': 'Interview'},
            'entityId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewType': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Location']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"})
        },
        u'citi_digits.interviewplayer': {
            'Meta': {'object_name': 'InterviewPlayer'},
            'do_you_ever_buy_lottery_tickets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'have_you_ever_won_the_lottery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jackpot_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'money_spent_on_lottery_in_average_week': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'most_won': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'why_or_why_not_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'citi_digits.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'InterviewComment.commenterClass'
        db.add_column(u'citi_digits_interviewcomment', 'commenterClass',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'InterviewComment.commenterClass'
        db.delete_column(u'citi_digits_interviewcomment', 'commenterClass')


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
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entityId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewType': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Location']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"})
        },
        u'citi_digits.interviewcomment': {
            'Meta': {'object_name': 'InterviewComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'commenterClass': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Interview']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'citi_digits.interviewplayer': {
            'Meta': {'object_name': 'InterviewPlayer'},
            'do_you_ever_buy_lottery_tickets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'have_you_ever_won_the_lottery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jackpot_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'money_spent_on_lottery_in_average_week': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'most_won': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'why_or_why_not_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'citi_digits.interviewretailer': {
            'Meta': {'object_name': 'InterviewRetailer'},
            'amount_tickets_bought_per_visit': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'customers_in_a_day': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'do_you_sell_lottery_tickets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage_buy_lottery_tickets': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'storeName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'why_or_why_not_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'why_or_why_not_lottery_neighborhood_audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'citi_digits.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'citi_digits.neighborhoodstatistics': {
            'Meta': {'object_name': 'NeighborhoodStatistics'},
            'adults_per_store': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'daily_income': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'daily_sale': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'daily_win': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'map_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_loss_per_store': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_win': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'percent_income': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_18_and_up': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_households': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_retailers': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        },
        u'citi_digits.tour': {
            'Meta': {'object_name': 'Tour'},
            'coverPhoto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"}),
            'teamPhoto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'citi_digits.tourauthors': {
            'Meta': {'object_name': 'TourAuthors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Student']"}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Tour']"})
        },
        u'citi_digits.tourslide': {
            'Meta': {'object_name': 'TourSlide'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citi_digits.Tour']"})
        }
    }

    complete_apps = ['citi_digits']
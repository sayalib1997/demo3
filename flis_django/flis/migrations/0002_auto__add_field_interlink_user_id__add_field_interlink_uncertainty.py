# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Interlink.user_id'
        db.add_column('flis_interlink', 'user_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Adding field 'Interlink.uncertainty'
        db.add_column('flis_interlink', 'uncertainty',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='interlinks', null=True, on_delete=models.PROTECT, to=orm['flis.Uncertainty']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Interlink.user_id'
        db.delete_column('flis_interlink', 'user_id')

        # Deleting field 'Interlink.uncertainty'
        db.delete_column('flis_interlink', 'uncertainty_id')


    models = {
        'flis.blossom': {
            'Meta': {'object_name': 'Blossom'},
            'date_of_conclusion_final': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_of_conclusion_planned': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'networks': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'new_or_update': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'other_parties': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ownership': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'project_team': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'purpose_and_target_audience': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_review_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_review_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_study_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'stakeholders_study_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'}),
            'time_plan_final': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'time_plan_planned': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'title_original': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'}),
            'who_is_doing': ('django.db.models.fields.CharField', [], {'max_length': '56', 'null': 'True'})
        },
        'flis.country': {
            'Meta': {'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'flis.earlywarning': {
            'Meta': {'object_name': 'EarlyWarning'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'earlywarnings'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'earlywarnings'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.flismodel': {
            'Meta': {'object_name': 'FlisModel'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flismodels'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'flismodels'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.geographicalcoverage': {
            'Meta': {'object_name': 'GeographicalCoverage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.geographicalscale': {
            'Meta': {'object_name': 'GeographicalScale'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.gmt': {
            'Meta': {'object_name': 'GMT'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gmts'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gmts'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.horizonscanning': {
            'Meta': {'object_name': 'HorizonScanning'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'horizonscannings'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'horizonscannings'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'base_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'end_year': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'geographical_coverage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalCoverage']"}),
            'geographical_scale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Indicators'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.GeographicalScale']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources_indicator'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'thematic_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Indicators'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.ThematicCategory']"}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'timeline'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Timeline']"})
        },
        'flis.interlink': {
            'Meta': {'object_name': 'Interlink'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flis.Country']"}),
            'gmt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks'", 'to': "orm['flis.GMT']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks_indicator_1'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_2'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_3'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'indicator_4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'interlinks_indicator_4'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Indicator']"}),
            'trend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Trend']"}),
            'uncertainty': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interlinks'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.Uncertainty']"}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'flis.methodtool': {
            'Meta': {'object_name': 'MethodTool'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'methodstools'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'methodstools'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.source': {
            'Meta': {'object_name': 'Source'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'year_of_publication': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'flis.steepcategory': {
            'Meta': {'object_name': 'SteepCategory'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.thematiccategory': {
            'Meta': {'object_name': 'ThematicCategory'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'flis.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'flis.trend': {
            'Meta': {'object_name': 'Trend'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trends'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.uncertainty': {
            'Meta': {'object_name': 'Uncertainty'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uncertainties'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'uncertainties'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'flis.wildcard': {
            'Meta': {'object_name': 'WildCard'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'file_id': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wildcards'", 'on_delete': 'models.PROTECT', 'to': "orm['flis.Source']"}),
            'steep_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wildcards'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': "orm['flis.SteepCategory']"}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['flis']
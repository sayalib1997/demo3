# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'NotificationUsers'
        db.delete_table(u'notifications_notificationusers')

        # Adding model 'NotificationUser'
        db.create_table(u'notifications_notificationuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'notifications', ['NotificationUser'])


    def backwards(self, orm):
        # Adding model 'NotificationUsers'
        db.create_table(u'notifications_notificationusers', (
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'notifications', ['NotificationUsers'])

        # Deleting model 'NotificationUser'
        db.delete_table(u'notifications_notificationuser')


    models = {
        u'notifications.notificationuser': {
            'Meta': {'object_name': 'NotificationUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['notifications']
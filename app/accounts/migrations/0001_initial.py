# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'P2PUProfile'
        db.create_table('accounts_p2puprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('p2pu_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('picture', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('accounts', ['P2PUProfile'])

        # Adding M2M table for field skills on 'P2PUProfile'
        db.create_table('accounts_p2puprofile_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('p2puprofile', models.ForeignKey(orm['accounts.p2puprofile'], null=False)),
            ('skill', models.ForeignKey(orm['mentorships.skill'], null=False))
        ))
        db.create_unique('accounts_p2puprofile_skills', ['p2puprofile_id', 'skill_id'])

        # Adding model 'Sponsor'
        db.create_table('accounts_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentorship_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.MentorshipRequest'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('receive_email_updates', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('accounts', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'P2PUProfile'
        db.delete_table('accounts_p2puprofile')

        # Removing M2M table for field skills on 'P2PUProfile'
        db.delete_table('accounts_p2puprofile_skills')

        # Deleting model 'Sponsor'
        db.delete_table('accounts_sponsor')


    models = {
        'accounts.p2puprofile': {
            'Meta': {'object_name': 'P2PUProfile'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'p2pu_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['mentorships.Skill']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'accounts.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentorship_request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.MentorshipRequest']"}),
            'receive_email_updates': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mentorships.mentorshiprequest': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'MentorshipRequest'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Skill']"}),
            'so_far': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'why': ('django.db.models.fields.TextField', [], {'max_length': '1000'})
        },
        'mentorships.skill': {
            'Meta': {'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
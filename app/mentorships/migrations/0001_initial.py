# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MentorshipRequest'
        db.create_table('mentorships_mentorshiprequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('learning', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Skill'])),
            ('so_far', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('why', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mentorships', ['MentorshipRequest'])

        # Adding model 'Mentorship'
        db.create_table('mentorships_mentorship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentor', to=orm['auth.User'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='student', to=orm['auth.User'])),
            ('learning', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Skill'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mentorships', ['Mentorship'])

        # Adding model 'MentorshipLog'
        db.create_table('mentorships_mentorshiplog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentorship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Mentorship'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mentorships', ['MentorshipLog'])

        # Adding model 'Skill'
        db.create_table('mentorships_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mentorships', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'MentorshipRequest'
        db.delete_table('mentorships_mentorshiprequest')

        # Deleting model 'Mentorship'
        db.delete_table('mentorships_mentorship')

        # Deleting model 'MentorshipLog'
        db.delete_table('mentorships_mentorshiplog')

        # Deleting model 'Skill'
        db.delete_table('mentorships_skill')


    models = {
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
        'mentorships.mentorship': {
            'Meta': {'object_name': 'Mentorship'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Skill']"}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentor'", 'to': "orm['auth.User']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student'", 'to': "orm['auth.User']"})
        },
        'mentorships.mentorshiplog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'MentorshipLog'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentorship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Mentorship']"})
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

    complete_apps = ['mentorships']
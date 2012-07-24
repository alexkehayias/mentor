# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('mentorships_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('looking_for', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('project_type', self.gf('django.db.models.fields.CharField')(default='l', max_length=1)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mentorships', ['Project'])

        # Adding M2M table for field skills on 'Project'
        db.create_table('mentorships_project_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['mentorships.project'], null=False)),
            ('skill', models.ForeignKey(orm['accounts.skill'], null=False))
        ))
        db.create_unique('mentorships_project_skills', ['project_id', 'skill_id'])

        # Adding M2M table for field members on 'Project'
        db.create_table('mentorships_project_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['mentorships.project'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('mentorships_project_members', ['project_id', 'user_id'])

        # Adding model 'JoinRequest'
        db.create_table('mentorships_joinrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Project'])),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mentorships', ['JoinRequest'])

        # Adding model 'ProjectLog'
        db.create_table('mentorships_projectlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Project'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mentorships', ['ProjectLog'])

        # Adding model 'Sponsor'
        db.create_table('mentorships_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentorships.Project'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('receive_email_updates', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('mentorships', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('mentorships_project')

        # Removing M2M table for field skills on 'Project'
        db.delete_table('mentorships_project_skills')

        # Removing M2M table for field members on 'Project'
        db.delete_table('mentorships_project_members')

        # Deleting model 'JoinRequest'
        db.delete_table('mentorships_joinrequest')

        # Deleting model 'ProjectLog'
        db.delete_table('mentorships_projectlog')

        # Deleting model 'Sponsor'
        db.delete_table('mentorships_sponsor')


    models = {
        'accounts.skill': {
            'Meta': {'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'mentorships.joinrequest': {
            'Meta': {'object_name': 'JoinRequest'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Project']"})
        },
        'mentorships.project': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Project'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'looking_for': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'project_type': ('django.db.models.fields.CharField', [], {'default': "'l'", 'max_length': '1'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounts.Skill']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'mentorships.projectlog': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'ProjectLog'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Project']"})
        },
        'mentorships.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentorships.Project']"}),
            'receive_email_updates': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['mentorships']
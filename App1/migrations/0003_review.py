# Generated by Django 4.0.3 on 2022-03-06 12:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_project_demo_link_alter_project_source_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, max_length=500, null=True)),
                ('value', models.CharField(choices=[('up', 'up'), ('down', 'down')], max_length=50)),
                ('creaed', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.project')),
            ],
        ),
    ]
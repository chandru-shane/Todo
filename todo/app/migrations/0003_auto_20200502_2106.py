# Generated by Django 3.0.5 on 2020-05-02 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='work',
            new_name='task',
        ),
    ]
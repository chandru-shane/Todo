# Generated by Django 3.0.5 on 2020-05-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('start', 'start'), ('doing', 'doing'), ('done', 'done')], max_length=100, null=True),
        ),
    ]

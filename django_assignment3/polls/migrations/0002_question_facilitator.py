# Generated by Django 2.2 on 2019-04-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='facilitator',
            field=models.CharField(default='temp', max_length=200),
        ),
    ]

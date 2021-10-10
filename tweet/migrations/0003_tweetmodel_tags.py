# Generated by Django 3.2.6 on 2021-10-10 13:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tweet', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

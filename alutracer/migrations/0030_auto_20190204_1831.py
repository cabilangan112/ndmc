# Generated by Django 2.1.3 on 2019-02-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alutracer', '0029_auto_20190204_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='facebook_account',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='twitter_account',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]

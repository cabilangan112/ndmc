# Generated by Django 2.1.3 on 2019-02-05 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alutracer', '0040_auto_20190205_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='contact_1',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='email_id_1',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='name_1',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='social_network_id_1',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]

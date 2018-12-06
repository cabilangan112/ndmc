# Generated by Django 2.1.3 on 2018-12-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alutracer', '0005_auto_20181203_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='content_description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='content_heading',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='footer_content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='footer_heading',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_1',
            field=models.ImageField(default=None, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_1_content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_1_heading_content',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_2',
            field=models.ImageField(default=None, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_2_content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='parallax_2_heading_content',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='media'),
            preserve_default=False,
        ),
    ]

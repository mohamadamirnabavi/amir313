# Generated by Django 3.1.7 on 2021-03-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210327_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblog_setting',
            name='site_title',
        ),
        migrations.RemoveField(
            model_name='weblog_setting',
            name='status',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='postcat', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]

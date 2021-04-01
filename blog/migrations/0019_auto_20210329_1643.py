# Generated by Django 3.1.7 on 2021-03-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210329_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='postcat', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]

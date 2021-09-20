# Generated by Django 3.2.6 on 2021-08-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210825_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readers',
            old_name='title',
            new_name='fio',
        ),
        migrations.RemoveField(
            model_name='readers',
            name='author',
        ),
        migrations.RemoveField(
            model_name='readers',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='readers',
            name='description',
        ),
        migrations.RemoveField(
            model_name='readers',
            name='image',
        ),
        migrations.AddField(
            model_name='readers',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readers',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
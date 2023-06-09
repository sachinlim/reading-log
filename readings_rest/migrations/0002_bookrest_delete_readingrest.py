# Generated by Django 4.1.7 on 2023-03-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookREST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('pages', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='ReadingREST',
        ),
    ]

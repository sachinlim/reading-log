# Generated by Django 4.1.7 on 2023-03-19 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readings_rest', '0002_bookrest_delete_readingrest'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

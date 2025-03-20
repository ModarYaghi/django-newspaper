# Generated by Django 5.0.13 on 2025-03-19 23:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Enter your comment (max 140 characters).', max_length=140)),
                ('article', models.ForeignKey(help_text='Select the article this comment is related to.', on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('author', models.ForeignKey(help_text='User who authored this comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

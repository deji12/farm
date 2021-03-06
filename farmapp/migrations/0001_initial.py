# Generated by Django 4.0.4 on 2022-04-26 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumb', models.FileField(upload_to='thumbs')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.CharField, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmapp.post')),
            ],
        ),
    ]

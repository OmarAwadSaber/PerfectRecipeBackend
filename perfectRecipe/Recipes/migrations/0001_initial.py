# Generated by Django 5.2.1 on 2025-05-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/')),
                ('description', models.TextField()),
                ('course_name', models.CharField(max_length=200)),
                ('ingredients', models.JSONField(default=list)),
                ('instructions', models.TextField()),
            ],
        ),
    ]

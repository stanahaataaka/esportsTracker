# Generated by Django 4.2.11 on 2024-05-02 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_match_matchplayers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='matchPlayers',
        ),
    ]
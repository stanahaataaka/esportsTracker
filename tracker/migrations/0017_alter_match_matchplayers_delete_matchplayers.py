# Generated by Django 4.2.11 on 2024-05-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_match_matchplayers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='matchPlayers',
            field=models.ManyToManyField(related_name='players', to='tracker.player'),
        ),
        migrations.DeleteModel(
            name='MatchPlayers',
        ),
    ]
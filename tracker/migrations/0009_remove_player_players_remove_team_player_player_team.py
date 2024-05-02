# Generated by Django 5.0.2 on 2024-05-02 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_rename_players_player_rename_players_team_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='players',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tracker.team'),
        ),
    ]

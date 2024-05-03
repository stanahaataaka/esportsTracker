# Generated by Django 4.2.11 on 2024-05-03 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_alter_match_matchplayers_delete_matchplayers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='matchPlayers',
        ),
        migrations.CreateModel(
            name='MatchPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.match')),
                ('playerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.player')),
            ],
        ),
    ]

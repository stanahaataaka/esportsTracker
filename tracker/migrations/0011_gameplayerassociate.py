# Generated by Django 5.0.2 on 2024-05-03 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_player_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlayerAssociate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tracker.game')),
                ('playerID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tracker.player')),
            ],
        ),
    ]
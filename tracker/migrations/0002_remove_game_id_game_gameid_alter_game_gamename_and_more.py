# Generated by Django 5.0.2 on 2024-04-28 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='id',
        ),
        migrations.AddField(
            model_name='game',
            name='gameID',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='gameName',
            field=models.CharField(choices=[('Rocket League', 'Rocket League'), ('Minecraft', 'Minecraft'), ('Valorant', 'Valorant')], default='Minecraft', max_length=25),
        ),
        migrations.RemoveField(
            model_name='team',
            name='game',
        ),
        migrations.AddField(
            model_name='team',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tracker.game'),
        ),
    ]
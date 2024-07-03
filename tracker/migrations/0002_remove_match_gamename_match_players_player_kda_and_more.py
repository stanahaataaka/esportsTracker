# Generated by Django 5.0.2 on 2024-05-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='gameName',
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='tracker.player'),
        ),
        migrations.AddField(
            model_name='player',
            name='KDA',
            field=models.CharField(default='0/0/0', max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='deaths',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='kills',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Upcoming', 'Upcoming')], default='Completed', max_length=10),
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordwolves', '0003_player_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='plain_pass',
            field=models.CharField(max_length=5, null=True),
        ),
    ]

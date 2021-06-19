# Generated by Django 3.2.4 on 2021-06-17 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameApp', '0006_character_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='attributes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_attributes', to='GameApp.attributes'),
        ),
        migrations.AlterField(
            model_name='character',
            name='faction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_factions', to='GameApp.faction'),
        ),
        migrations.AlterField(
            model_name='character',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_party', to='GameApp.party'),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='character_players', to='GameApp.player'),
        ),
    ]

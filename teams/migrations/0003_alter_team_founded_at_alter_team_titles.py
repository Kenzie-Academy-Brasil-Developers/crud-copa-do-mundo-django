# Generated by Django 4.1.3 on 2022-12-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_alter_team_founded_at_alter_team_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='founded_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='titles',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

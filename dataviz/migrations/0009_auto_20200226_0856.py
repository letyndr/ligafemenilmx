# Generated by Django 3.0.3 on 2020-02-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataviz', '0008_club_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadora',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]

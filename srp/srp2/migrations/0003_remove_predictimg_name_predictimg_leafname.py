# Generated by Django 4.0.6 on 2022-10-06 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srp2', '0002_remove_predictimg_predictimg_predictimg_userimg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictimg',
            name='name',
        ),
        migrations.AddField(
            model_name='predictimg',
            name='LeafName',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.1 on 2019-08-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor_app', '0015_auto_20190826_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='i_donated_recently',
            field=models.DateField(blank=True, null=True, verbose_name="I've donated recently"),
        ),
    ]

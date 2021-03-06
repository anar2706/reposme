# Generated by Django 2.2.1 on 2019-06-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor_app', '0011_remove_donor_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Account is private'),
        ),
        migrations.AlterIndexTogether(
            name='donor',
            index_together={('first_name', 'last_name', 'phone', 'is_private', 'is_closed')},
        ),
    ]

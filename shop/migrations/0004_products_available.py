# Generated by Django 2.2 on 2021-07-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210729_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

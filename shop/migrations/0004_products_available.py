# Generated by Django 3.2.6 on 2021-08-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_categ_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-09 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20211009_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='salesuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.salesuser'),
        ),
    ]

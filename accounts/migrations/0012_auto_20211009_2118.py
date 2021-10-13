# Generated by Django 3.2.7 on 2021-10-09 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20211007_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('br_code', models.CharField(max_length=2, null=True)),
                ('br_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'unique_together': {('br_code', 'br_name')},
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CASH RET', 'CASH RET'), ('CREDIT', 'CREDIT'), ('CREDIT RET', 'CREDIT RET')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesm_name', models.CharField(max_length=50, null=True)),
                ('salesm_br', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.branch')),
            ],
            options={
                'unique_together': {('salesm_name',)},
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.branch'),
        ),
        migrations.AddField(
            model_name='order',
            name='salesman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.salesman'),
        ),
        migrations.AlterField(
            model_name='salesuser',
            name='su_br',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.branch'),
        ),
    ]
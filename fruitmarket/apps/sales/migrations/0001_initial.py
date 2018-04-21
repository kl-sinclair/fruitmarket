# Generated by Django 2.0.4 on 2018-04-21 16:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='datetime updated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='datetime created')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='quantity')),
                ('amount', models.PositiveIntegerField(editable=False, verbose_name='amount')),
                ('sold_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='datetime sold')),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Fruit')),
            ],
            options={
                'verbose_name': 'sale of fruit',
                'verbose_name_plural': 'sales of fruit',
                'ordering': ['-sold_at'],
            },
        ),
    ]

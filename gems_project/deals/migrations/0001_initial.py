# Generated by Django 4.2.3 on 2023-07-30 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField(max_length=64, unique=True, verbose_name='Логин клиента')),
                ('spent_money', models.PositiveIntegerField(default=0, verbose_name='Потраченная сумма')),
            ],
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=64, unique=True, verbose_name='Название')),
                ('customers', models.ManyToManyField(related_name='gems', to='deals.customer', verbose_name='Клиенты')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(verbose_name='Сумма сделки')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество товара')),
                ('date', models.DateTimeField(verbose_name='Дата сделки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='deals.customer', verbose_name='Клиент')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='deals.gem', verbose_name='Товар')),
            ],
        ),
    ]
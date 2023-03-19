# Generated by Django 4.1.7 on 2023-03-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candle', '0002_info_alter_candle_burn_time_alter_candle_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterModelOptions(
            name='candle',
            options={'verbose_name': 'Таблица товаров', 'verbose_name_plural': 'Таблица товаров'},
        ),
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Инфо', 'verbose_name_plural': 'Инфо'},
        ),
    ]

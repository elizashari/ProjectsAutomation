# Generated by Django 4.2.6 on 2023-10-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr_auto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_time', models.TimeField(verbose_name='Время созвона')),
            ],
        ),
        migrations.CreateModel(
            name='PM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя PM')),
                ('telegram_id', models.CharField(db_index=True, max_length=50, verbose_name='Telegram id')),
                ('call_time', models.TimeField()),
            ],
        ),
    ]

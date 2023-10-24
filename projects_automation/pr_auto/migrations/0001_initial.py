# Generated by Django 4.2.6 on 2023-10-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=25, verbose_name='Уровень')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя студента')),
                ('telegram_id', models.CharField(db_index=True, max_length=50, verbose_name='Telegram id')),
                ('email', models.CharField(db_index=True, max_length=50, verbose_name='email')),
                ('is_dv', models.BooleanField(blank=True, default=None, null=True, verbose_name='Ученик с Дальнего Востока')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.level', verbose_name='Уровень ученика')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': ' Students',
            },
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-25 21:29

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
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': ' Levels',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Имя студента')),
                ('telegram_id', models.CharField(db_index=True, max_length=50, verbose_name='Telegram id')),
                ('email', models.CharField(db_index=True, max_length=50, verbose_name='email')),
                ('project_week', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Неделя проекта')),
                ('call_time', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Удобное время для созвона')),
                ('is_dv', models.BooleanField(blank=True, default=None, null=True, verbose_name='Ученик с Дальнего Востока')),
                ('registration_status', models.BooleanField(default=False, verbose_name='Статус регистрации в проекте')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.level', verbose_name='Уровень ученика')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': ' Students',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Название проекта')),
                ('brief', models.FileField(max_length=254, upload_to=None)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.level', verbose_name='Уровень проекта')),
            ],
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('name', 'email', 'telegram_id'), name='unique_name_email_telegram_id'),
        ),
    ]

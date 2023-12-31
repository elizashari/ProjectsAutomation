# Generated by Django 4.2.6 on 2023-10-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pr_auto', '0003_remove_pm_call_time_pm_call_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Группа')),
                ('pm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.pm', verbose_name='PM проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.project')),
                ('students', models.ManyToManyField(to='pr_auto.student')),
            ],
        ),
    ]

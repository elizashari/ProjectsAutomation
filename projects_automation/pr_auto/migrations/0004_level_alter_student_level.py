# Generated by Django 4.2.6 on 2023-10-25 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pr_auto', '0003_student_call_time'),
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
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pr_auto.level', verbose_name='Уровень ученика'),
        ),
    ]

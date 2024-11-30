# Generated by Django 5.0.4 on 2024-04-17 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_lesson_visit_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_visit',
            name='groups',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='visiting', to='myapp.group'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='year',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='year',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson_visit',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visiting', to='myapp.discipline'),
        ),
        migrations.AlterField(
            model_name='lesson_visit',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visiting', to='myapp.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='myapp.group'),
        ),
    ]

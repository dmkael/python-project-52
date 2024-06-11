# Generated by Django 5.0.6 on 2024-06-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0004_alter_label_name'),
        ('tasks', '0004_alter_task_options_alter_task_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='labels.label', verbose_name='Labels'),
        ),
    ]
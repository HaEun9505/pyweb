# Generated by Django 4.0 on 2021-12-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_question_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

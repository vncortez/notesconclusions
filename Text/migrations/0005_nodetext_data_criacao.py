# Generated by Django 3.2.9 on 2021-11-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Text', '0004_alter_nodetext_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodetext',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
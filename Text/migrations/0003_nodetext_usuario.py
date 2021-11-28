# Generated by Django 3.2.9 on 2021-11-28 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Text', '0002_nodetext_tipo_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodetext',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]

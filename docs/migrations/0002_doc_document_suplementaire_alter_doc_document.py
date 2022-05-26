# Generated by Django 4.0.2 on 2022-05-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='document_suplementaire',
            field=models.FileField(blank=True, default=None, null=True, upload_to='docs/files/<int:pk>/'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='document',
            field=models.FileField(upload_to='docs/files/<int:pk>/'),
        ),
    ]

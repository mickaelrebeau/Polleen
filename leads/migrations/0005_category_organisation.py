# Generated by Django 4.0.2 on 2022-03-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_category_lead_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]

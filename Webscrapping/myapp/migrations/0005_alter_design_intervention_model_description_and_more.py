# Generated by Django 5.0.3 on 2024-03-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_design_intervention_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="design",
            name="intervention_model_description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="design",
            name="primary_purpose",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="design",
            name="study_type",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
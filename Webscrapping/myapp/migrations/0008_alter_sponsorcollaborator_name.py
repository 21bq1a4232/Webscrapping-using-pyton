# Generated by Django 5.0.3 on 2024-03-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_alter_sponsorcollaborator_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsorcollaborator",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]

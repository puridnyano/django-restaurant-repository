# Generated by Django 5.1.4 on 2025-01-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Base_App", "0003_feedback_image_alter_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="Rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mini_blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name="post",
            name="images",
        ),
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.AddField(
            model_name="post",
            name="images",
            field=models.ImageField(blank=True, null=True, upload_to="post_images"),
        ),
    ]

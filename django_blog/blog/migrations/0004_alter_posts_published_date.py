# Generated by Django 5.0.7 on 2024-09-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blog_posts_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

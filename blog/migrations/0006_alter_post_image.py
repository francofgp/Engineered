# Generated by Django 4.0.4 on 2022-05-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../static/images/blog_post.jpg', upload_to='post/images/'),
        ),
    ]

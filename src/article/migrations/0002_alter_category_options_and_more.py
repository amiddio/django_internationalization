# Generated by Django 4.2.5 on 2023-09-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_translations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['-pub_datetime'], name='article_art_pub_dat_0df5f8_idx'),
        ),
    ]
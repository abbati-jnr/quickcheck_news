# Generated by Django 4.1.1 on 2022-09-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsitem_by_alter_newsitem_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

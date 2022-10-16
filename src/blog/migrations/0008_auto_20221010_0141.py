# Generated by Django 3.2 on 2022-10-09 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_auteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='ingredient',
            field=models.ManyToManyField(to='blog.Ingredient'),
        ),
    ]
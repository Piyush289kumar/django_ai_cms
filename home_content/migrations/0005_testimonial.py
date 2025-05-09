# Generated by Django 5.2 on 2025-04-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_content', '0004_team_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

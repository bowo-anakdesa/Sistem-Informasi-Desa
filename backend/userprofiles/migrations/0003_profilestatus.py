# Generated by Django 2.2.2 on 2019-06-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20190629_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('status_content', models.CharField(max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='userprofiles.Profile')),
            ],
            options={
                'verbose_name_plural': 'statuses',
            },
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-08 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['pk'],
            },
        ),
    ]

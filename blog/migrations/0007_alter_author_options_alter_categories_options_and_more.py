# Generated by Django 4.0.3 on 2022-09-26 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('-created',), 'verbose_name_plural': 'مدرسان'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('-created',), 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'اعلان ها'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',), 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ('-created',), 'verbose_name_plural': 'تگ ها'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_click',
        ),
    ]
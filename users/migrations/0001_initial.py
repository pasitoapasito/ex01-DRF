# Generated by Django 4.0.4 on 2022-05-24 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('kakao_id', models.BigIntegerField()),
                ('email', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('profile_image_url', models.CharField(default='https://cdn.pixabay.com/photo/2016/03/31/19/58/avatar-1295429_960_720.png', max_length=2000)),
                ('point', models.IntegerField(default=1000000)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'users_lectures',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='lectures',
            field=models.ManyToManyField(related_name='users', through='users.UserLecture', to='lectures.lecture'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
    ]

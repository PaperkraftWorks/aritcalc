# Generated by Django 4.1.7 on 2023-03-03 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('amount', models.BigIntegerField(default=0)),
                ('user_balance', models.BigIntegerField(default=0)),
                ('operation_response', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('operation_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='operations.operation')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
            ],
        ),
    ]

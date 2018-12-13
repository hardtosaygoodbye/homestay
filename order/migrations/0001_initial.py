# Generated by Django 2.1.4 on 2018-12-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '待付款'), (1, '已完成'), (2, '已取消')], verbose_name='订单状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单价格')),
                ('name', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(max_length=11)),
                ('id_card', models.CharField(max_length=18)),
                ('person_num', models.CharField(max_length=5)),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

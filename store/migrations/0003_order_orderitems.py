# Generated by Django 5.0.3 on 2024-03-05 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_basketitem_is_order_placed_basketitem_size_object'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('is_paid', models.BooleanField(default=False)),
                ('total', models.PositiveIntegerField()),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('intransit', 'intransit'), ('dispatched', 'dispatched'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='order-placed', max_length=200)),
                ('basket_item_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.basketitem')),
                ('order_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseitems', to='store.order')),
            ],
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dash", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="productcategory",
            field=models.CharField(
                choices=[
                    ("Goods", "Goods"),
                    ("Electronics", "Electronics"),
                    ("Foods", "Foods"),
                    ("Bags", "Bags"),
                ],
                default="Bags",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="productimage",
            field=models.ImageField(
                blank=True, default="media/bag_6fTAjkq.jpg", upload_to="media"
            ),
        ),
    ]

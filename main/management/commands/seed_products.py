# main/management/commands/seed_products.py
from django.core.management.base import BaseCommand
from main.models import Product

DATA = [
    dict(name="Mike Zoom Mercurial", price=2599000, description="Speed boots ringan dengan upper knit responsif.",
         thumbnail="https://static.nike.com/a/images/f_auto/mercurial.jpg", category="Boots", is_featured=True,
         stock=12, brand="Mike", rating=4.7),
    dict(name="Mike Phantom GX", price=2299000, description="Kontrol presisi dengan tekstur grippy.",
         thumbnail="https://static.nike.com/a/images/f_auto/phantom-gx.jpg", category="Boots", is_featured=False,
         stock=8, brand="Mike", rating=4.5),
    dict(name="Mike Flight Match Ball", price=799000, description="Bola pertandingan dengan stabilitas lintasan.",
         thumbnail="https://static.nike.com/a/images/f_auto/flight-ball.jpg", category="Ball", is_featured=False,
         stock=30, brand="Mike", rating=4.6),
    dict(name="Mike Guard Pro", price=199000, description="Shin guard ergonomis, nyaman dan aman.",
         thumbnail="https://static.nike.com/a/images/f_auto/guard.jpg", category="Accessories", is_featured=False,
         stock=40, brand="Mike", rating=4.3),
    dict(name="Mike Club Jersey 24/25", price=599000, description="Jersey replika bahan breathable.",
         thumbnail="https://static.nike.com/a/images/f_auto/jersey.jpg", category="Jersey", is_featured=True,
         stock=25, brand="Mike", rating=4.4),
    dict(name="Mike Stadium Backpack", price=449000, description="Ransel lapangan multi-kompartemen.",
         thumbnail="https://static.nike.com/a/images/f_auto/backpack.jpg", category="Bags", is_featured=False,
         stock=15, brand="Mike", rating=4.2),
]

class Command(BaseCommand):
    help = "Seed database with sample products"

    def handle(self, *args, **options):
        created = 0
        for item in DATA:
            obj, is_created = Product.objects.get_or_create(
                name=item["name"],
                defaults=item,
            )
            created += int(is_created)
        self.stdout.write(self.style.SUCCESS(f"Seed done. Created: {created}, total in DB: {Product.objects.count()}"))

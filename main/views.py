from django.shortcuts import render
from .models import Product

def index(request):
    app_name = "Mike — Football Shop"
    student_name = "Muhammad Rayyan Basalamah"
    student_class = "PBP E / 2406496372"

    products_qs = list(Product.objects.all())
    if products_qs:
        products = products_qs
    else:
        # fallback dummy bila DB kosong
        products = [
            {
                "name": "Mike Tiempo Legend",
                "price": 1899000,
                "description": "Sepatu bola kulit klasik yang nyaman.",
                "thumbnail": "https://static.nike.com/a/images/f_auto/dpr_2.0,cs_srgb/w_906,c_limit/e2987c5b-boot.jpg",
                "category": "Boots",
                "is_featured": True,
                "brand": "Mike",
            },
            {
                "name": "Mike Flight Ball",
                "price": 799000,
                "description": "Bola match-quality dengan aerowtrac grooves.",
                "thumbnail": "https://static.nike.com/a/images/f_auto/dpr_2.0,cs_srgb/w_906,c_limit/ball.jpg",
                "category": "Ball",
                "is_featured": False,
                "brand": "Mike",
            },
        ]

    ctx = {
        "app_name": app_name,
        "student_name": student_name,
        "student_class": student_class,
        "products": products,
    }
    return render(request, "main/index.html", ctx)
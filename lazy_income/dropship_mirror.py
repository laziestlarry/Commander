# lazy_income/dropship_mirror.py

def mirror_products():
    print("📦 Fetching hot trending products from AliExpress / Amazon...")

    trending_items = [
        {"name": "Mini Desktop Vacuum", "price": 12.99},
        {"name": "Portable Blender Cup", "price": 24.50},
        {"name": "LED Galaxy Projector", "price": 19.90},
        # New product offers for expansion
        {"name": "Smart Water Bottle with Hydration Reminder", "price": 29.99},
        {"name": "Wireless Charging Desk Lamp", "price": 34.95},
        {"name": "Ergonomic Laptop Stand", "price": 21.75}
    ]
        {"name": "Smart Water Bottle with Hydration Reminder", "price": 29.99},
        {"name": "Wireless Charging Desk Lamp", "price": 34.95},
        {"name": "Ergonomic Laptop Stand", "price": 21.75}
    ]

    for item in trending_items:
        print(f"🛒 Mirrored: {item['name']} – Suggested Price: ${round(item['price'] * 1.8, 2)}")

    print("✅ Dropship mirroring complete.")
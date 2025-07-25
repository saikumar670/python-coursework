# -------------------------------------
# 💎 Giva Jewellery App - Take Input & Display in 4 Styles
# -------------------------------------

# App name
app_name = "💎 Giva Jewellery App"

# --- Take input from user ---
jewel_name = input("Enter Jewellery Name: ")
customer_name = input("Enter Customer Name: ")
quantity = int(input("Enter Quantity: "))
price_per_piece = float(input("Enter Price per Piece (₹): "))
is_available = input("Is the product available? (yes/no): ").lower() == "yes"
delivery_date = input("Enter Delivery Date (press Enter to skip): ") or None
categories = [cat.strip() for cat in input("Enter Categories (comma-separated): ").split(",")]
rating_score = float(input("Enter Product Rating (e.g., 4.5): "))
rating_label = input("Enter Rating Label (e.g., Premium Quality): ")
jewel_rating = (rating_score, rating_label)
jewel_details = {
    "product": jewel_name,
    "customer": customer_name,
    "quantity": quantity
}
special_features = {feat.strip() for feat in input("Enter Special Features (comma-separated): ").split(",")}
product_code = 2024 + 1j

# --- App Header ---
print(f"\n🛍 Welcome to {app_name}")
print("-" * 40)

# --- f-strings ---
print("\n📦 Jewellery Order Summary (f-strings):")
print(f"Product: {jewel_name} for {customer_name}")
print(f"Price per item: ₹{price_per_piece:,.2f}")
print(f"Quantity: {quantity:,}")
print(f"Total Price: ₹{price_per_piece * quantity:,.2f}")
print(f"Available: {'Yes' if is_available else 'No'}")
print(f"Categories: {', '.join(categories)}")
print(f"Rating: {jewel_rating[0]} stars ({jewel_rating[1]})")
print(f"Details (dict): {jewel_details}")
print(f"Special Features (set): {', '.join(special_features)}")
print(f"Delivery Date: {delivery_date}")
print(f"Product Code (complex): {product_code}")

# --- .format() method ---
print("\n📋 Using .format() method:")
print("Product: {} | Customer: {}".format(jewel_name, customer_name))
print("Each ₹{:.2f} × {} = ₹{:.2f}".format(price_per_piece, quantity, price_per_piece * quantity))

# --- % formatting ---
print("\n📊 Using %% formatting:")
print("Product: %s | Buyer: %s" % (jewel_name, customer_name))
print("₹%.2f per item × %d = ₹%.2f" % (price_per_piece, quantity, price_per_piece * quantity))

# --- End of App ---
print("\n✅ Thank you for shopping at", app_name)

# Sample sales data
sales_data = [
    {"product_id" : 101, "product_name" : "Smartphone", "sale_amount" : 500, "sale_date" : "2025-01-01"},
    {"product_id" : 102, "product_name" : "Laptop", "sale_amount" : 300, "sale_date" : "2025-01-02"},
    {"product_id" : 101, "product_name" : "Smartphone", "sale_amount" : 400, "sale_date" : "2025-01-03"},
    {"product_id" : 103, "product_name" : "Smartwatch", "sale_amount" : 700, "sale_date" : "2025-01-04"}
]

# -----------------------------
# Step 1: Calculate total sales
# -----------------------------
total_sales = 0
for sale in sales_data :
    total_sales += sale["sale_amount"]

# -----------------------------
# Step 2: Calculate sales per product
# -----------------------------
sales_per_product = {}  # {product_id: total_amount}
product_names = {}  # {product_id: product_name}

for sale in sales_data :
    pid = sale["product_id"]
    pname = sale["product_name"]
    amount = sale["sale_amount"]

    if pid not in sales_per_product :
        sales_per_product[pid] = 0
        product_names[pid] = pname

    sales_per_product[pid] += amount

# -----------------------------
# Step 3: Average sales per product
# -----------------------------
average_sales = total_sales // len(sales_per_product)

# -----------------------------
# Step 4: Find highest-selling product
# -----------------------------
max_sales = 0
highest_product_id = None

for pid, amount in sales_per_product.items() :
    if amount > max_sales :
        max_sales = amount
        highest_product_id = pid

highest_product = {
    "product_id" : highest_product_id,
    "product_name" : product_names[highest_product_id]
}

# -----------------------------
# Final result
# -----------------------------
result = {
    "Total Sales" : total_sales,
    "Average Sales" : average_sales,
    "Highest-Selling Product" : highest_product
}

print(result)

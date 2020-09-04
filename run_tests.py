import requests, uuid, random, csv

base_url = "https://prod.tabyeats.com/api/"

res = requests.get("{}/menu".format(base_url))
menu = res.json()

print("Menu data: ")
print(menu)

random_section = random.sample(menu['sections'], 1)
random_subsection = random.sample(random_section[0]['subsections'], 1)
random_items = random.sample(random_subsection[0]['items'], min(len(random_subsection[0]['items']), 5))

new_order = []
sub_total = 0
tax = 0
for item in random_items:
    new_item =     {
      "id": item['item_id'],
      "name": item['title'],
      "external_id": item['external_id'],
      "price": "{:3,.2f}".format(item['price']),
      "quantity": "1",
      "notes": item['item_description'],
      "mods": []
    }
    new_order.append(new_item)
    sub_total += item['price']
    tax += item['price'] * item['tax_rate'] / 100.0

tip = 0.2 * sub_total

total = sub_total + tax + tip

customer = {
    "id": "078eb998-3b05-4ae3-8b5c-9063124338cd",
    "name": "Jane J. Doe",
    "phone": "5555555555",
    "email": "prince@tabyeats.com",
    "address1": "1234 S Main Street",
    "address2": "Suite 180",
    "city": "New York",
    "state": "NY",
    "zip": "10001",
    "cross_street": "Rodeo Drive",
    "special_instructions": "Doorman will let you up."
  }

info = {
    "id": "{}".format(uuid.uuid4()),
    "pickup_code": "AZ45jd9pQckJf078",
    "service_type": "Pick-Up",
    "payment_is_cash": False,
    "payment_type": "credit",
    "tip_payment_is_cash": True,
    "tip_payment_type": "cash",
    "subtotal": "{:3,.2f}".format(sub_total),
    "delivery_charge": "3.75",
    "sales_tax": "{:3,.2f}".format(tax),
    "tip": "{:3,.2f}".format(tip),
    "total": "{:3,.2f}".format(total),
    "coupon_description": "New York Restaurant Coupons - neighborhood discount",
    "coupon_amount": "4.75"
  }

order = {
      'customer': customer,
      'info': info,
      'items': new_order
  }

res = requests.post("{}/order".format(base_url), json={'order': order}).json()

print("Order response: ")
print(res)

# order_id = requests.get("{}/order?orderId={}".format(base_url, res['id'])).text
# print("Order details: ")
# print(order_id)
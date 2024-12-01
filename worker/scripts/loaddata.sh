#!/bin/bash

migrations_dir="api/migrations/"

if ! ls -A "$migrations_dir" | grep -q "^[0-9]"; then
    python manage.py makemigrations
fi

python manage.py migrate

echo "Load data from fixtures"

echo "======Load users======"
python manage.py loaddata user.json

echo "======Load carts======"
python manage.py loaddata carts.json

echo "======Load category======"
python manage.py loaddata category.json

echo "======Load subcategory======"
python manage.py loaddata subcategory.json

echo "======Load product======"
python manage.py loaddata product.json

echo "======Load product_attr======"
python manage.py loaddata product_attr.json

echo "======Load product_sku======"
python manage.py loaddata product_sku.json

echo "======Load product_images======"
python manage.py loaddata product_images.json

echo "======Load province======"
python manage.py loaddata province.json

echo "======Load district======"
python manage.py loaddata district.json

echo "======Load ward======"
python manage.py loaddata ward.json

echo "======Load payment_method======"
python manage.py loaddata payment_method.json

echo "======Load shipment_method======"
python manage.py loaddata shipment_method.json

echo "======Load order======"
python manage.py loaddata order.json

echo "======Load order_item======"
python manage.py loaddata order_item.json

echo "======Load payment======"
python manage.py loaddata payment.json

echo "======Load shipment======"
# python manage.py loaddata shipment.json


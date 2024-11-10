#!/bin/bash

migrations_dir="api/migrations/"

if ! ls -A "$migrations_dir" | grep -q "^[0-9]"; then
    python manage.py makemigrations
fi

python manage.py migrate

echo "Load data from fixtures"

python manage.py loaddata user.json
python manage.py loaddata carts.json
python manage.py loaddata category.json
python manage.py loaddata subcategory.json
python manage.py loaddata product.json
python manage.py loaddata product_attr.json
python manage.py loaddata product_sku.json
python manage.py loaddata product_images.json

# python manage.py shell

import json
from expenses.models import Category, Expense

with open("fixtures.json") as f:
    fixtures_json = json.load(f)

for c_fixture in fixtures_json:
    if c_fixture["model"] == "expenses.category":
        c_fixture = Category(name=c_fixture["fields"]["name"])
        c_fixture.save()
d = {
    1: Category.objects.get(pk=1),
    2: Category.objects.get(pk=2),
    3: Category.objects.get(pk=3),
    4: Category.objects.get(pk=4),
}

for e_fixture in fixtures_json:
    if e_fixture["model"] == "expenses.expense":
        e_fixture = Expense(
            category=d[e_fixture["fields"]["category"]],
            name=e_fixture["fields"]["name"],
            amount=e_fixture["fields"]["amount"],
            date=e_fixture["fields"]["date"],
        )
        e_fixture.save()

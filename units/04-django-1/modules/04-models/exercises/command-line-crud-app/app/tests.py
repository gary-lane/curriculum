from django.test import TestCase
from app import models
class TestContact(TestCase):
    def test_can_add_item(self):
        item = models.add_item(
            "Plate Mail Armor",
            300.00,
            1,
            True,
        )
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "Plate Mail Armor")
        self.assertEqual(item.value, 300.00)
        self.assertEqual(item.amount, 1)
        self.assertTrue(item.is_favorite)
    def test_can_view_all_items_at_once(self):
        items_data = [
            {
                "name": "Apple",
                "value": 1.00,
                "amount": 10,
                "is_favorite": True,
            },
            {
                "name": "Orange",
                "value": 1.25,
                "amount": 8,
                "is_favorite": False,
            },
            {
                "name": "Banana",
                "value": 1.75,
                "amount": 12,
                "is_favorite": True,
            }
        ]
        for item_data in items_data:
            models.add_item(
                item_data["name"],
                item_data["value"],
                item_data["amount"],
                item_data["is_favorite"],
            )
        items = models.all_items()
        self.assertEqual(len(items), len(items_data))
        items_data = sorted(items_data, key=lambda i: i["name"])
        items = sorted(items, key=lambda i: i.name)
        for data, item in zip(items_data, items):
            self.assertEqual(data["name"], item.name)
            self.assertEqual(data["value"], item.value)
            self.assertEqual(data["amount"], item.amount)
            self.assertEqual(data["is_favorite"], item.is_favorite)
    def test_can_search_by_name(self):
        items_data = [
            {
                "name": "Apple",
                "value": 1.00,
                "amount": 10,
                "is_favorite": True,
            },
            {
                "name": "Orange",
                "value": 1.25,
                "amount": 8,
                "is_favorite": False,
            },
            {
                "name": "Banana",
                "value": 1.75,
                "amount": 12,
                "is_favorite": True,
            }
        ]
        for item_data in items_data:
            models.add_item(
                item_data["name"],
                item_data["value"],
                item_data["amount"],
                item_data["is_favorite"],
            )
        self.assertIsNone(models.find_item_by_name("aousnth"))
        item = models.find_item_by_name("Banana")
        self.assertIsNotNone(item)
        self.assertEqual(item.value, 1.75)
        self.assertEqual(item.amount, 12)
    def test_can_view_favorites(self):
        items_data = [
            {
                "name": "Apple",
                "value": 1.00,
                "amount": 10,
                "is_favorite": True,
            },
            {
                "name": "Orange",
                "value": 1.25,
                "amount": 8,
                "is_favorite": False,
            },
            {
                "name": "Banana",
                "value": 1.75,
                "amount": 12,
                "is_favorite": True,
            }
        ]
        for item_data in items_data:
            models.add_item(
                item_data["name"],
                item_data["value"],
                item_data["amount"],
                item_data["is_favorite"],
            )
        self.assertEqual(len(models.favorite_items()), 2)
    def test_can_update_contacts_email(self):
        items_data = [
            {
                "name": "Apple",
                "value": 1.00,
                "amount": 10,
                "is_favorite": True,
            },
            {
                "name": "Orange",
                "value": 1.25,
                "amount": 8,
                "is_favorite": False,
            },
            {
                "name": "Banana",
                "value": 1.75,
                "amount": 12,
                "is_favorite": True,
            }
        ]
        for item_data in items_data:
            models.add_item(
                item_data["name"],
                item_data["value"],
                item_data["amount"],
                item_data["is_favorite"],
            )
        models.update_item_amount("Apple", 15)
        self.assertEqual(
            models.find_item_by_name("Apple").amount, 15
        )
    def test_can_delete_contact(self):
        items_data = [
            {
                "name": "Apple",
                "value": 1.00,
                "amount": 10,
                "is_favorite": True,
            },
            {
                "name": "Orange",
                "value": 1.25,
                "amount": 8,
                "is_favorite": False,
            },
            {
                "name": "Banana",
                "value": 1.75,
                "amount": 12,
                "is_favorite": True,
            }
        ]
        for item_data in items_data:
            models.add_item(
                item_data["name"],
                item_data["value"],
                item_data["amount"],
                item_data["is_favorite"],
            )
        models.delete_item("Orange")
        self.assertEqual(len(models.all_items()), 2)
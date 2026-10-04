import unittest
from app import LibraryCatalog

class TestLibraryCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = LibraryCatalog()

    def test_add_book(self):
        book = self.catalog.add_book("Абай жолы", "Мұхтар Әуезов")
        self.assertEqual(len(self.catalog.get_all_books()), 1)
        self.assertEqual(book["title"], "Абай жолы")

    def test_search_book(self):
        self.catalog.add_book("Көшпенділер", "Ілияс Есенберлин")
        results = self.catalog.search_book("Көшпенділер")
        self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()
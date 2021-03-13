from django.test import TestCase

# Create your tests here.


class FirstTestCase(TestCase):
    def setUp(self):
        x = 0

    def test_first_test_case(self):
        self.assertEqual(0, 0)

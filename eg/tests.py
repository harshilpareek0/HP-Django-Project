from django.test import TestCase
from .models import Exercise
from .views import ProgressView
from math import floor

# Create your tests here.


class FirstTestCase(TestCase):
    def setUpTestData(cls):
        Exercise.objects.create(exercise_name="sprint")
        Exercise.objects.create(exercise_name="swim")
        Exercise.objects.create(exercise_name="walk")


    def test_first_test_case(self):
        self.assertEqual(0, 0)

    def test_progress_percentage_test_case(self):
        progress = (Exercise.objects.count() % 10) * 100
        progress_percentage = progress / 10
        self.assertEqual(30, progress_percentage)
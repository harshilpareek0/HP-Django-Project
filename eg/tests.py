from django.test import TestCase
from eg.models import Exercise
from eg.views import ProgressView
from math import floor
from django.contrib.auth.models import User

# Create your tests here.


class FirstTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user("Can Unlu", "cu6fb@virginia.edu", "password")
        Exercise.objects.create(exercise_name="sprint", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="sprint", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="swim", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="walk", exerciser_name=self.test_user)


    def test_first_test_case(self):
        self.assertEqual(0, 0)

    def test_user_history(self):
        self.assertEqual(Exercise.objects.filter(exerciser_name=self.test_user.id, exercise_name="sprint").count(), 2)

    def test_individual_user_history(self):
        new_test_user = User.objects.create_user("Some guy", "abcd@virginia.edu", "different password")
        Exercise.objects.create(exercise_name="sprint", exerciser_name=new_test_user)
        Exercise.objects.create(exercise_name="walking", exerciser_name=new_test_user)
        Exercise.objects.create(exercise_name="swim", exerciser_name=new_test_user)
        self.assertNotEqual(Exercise.objects.filter(exerciser_name=self.test_user.id).count(), Exercise.objects.filter(exerciser_name=new_test_user.id).count())

    def test_progress_percentage_test_case(self):
        progress = (Exercise.objects.filter(exerciser_name=self.test_user.id).count() % 10) * 100
        progress_percentage = progress / 10
        self.assertEqual(40, progress_percentage)

    def test_level_test_case(self):
        level = floor(Exercise.objects.filter(exerciser_name=self.test_user.id).count() / 10)
        self.assertEqual(0, level)

    def test_level_up_case(self):
        Exercise.objects.create(exercise_name="football", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="tennis", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="swim", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="walk", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="basketball", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="swim", exerciser_name=self.test_user)
        Exercise.objects.create(exercise_name="walk", exerciser_name=self.test_user)
        level = floor(Exercise.objects.filter(exerciser_name=self.test_user.id).count() / 10)
        self.assertEqual(1, level)


    def test_create_profile_page_view(self):
        response = self.client.get('/create_profile_page/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('create_user_profile_page.html')

    def test_user_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('register.html')

    def test_input_exercise_view(self):
        response = self.client.get('/exercise/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('exercise.html')

    def test_post_forum_view(self):
        response = self.client.get('/forum_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('forum_post.html')

    def test_forum_view(self):
        response = self.client.get('/forum/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('forum.html')
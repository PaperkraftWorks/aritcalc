from users.tests.factories import UserFactory
from django.test import TestCase

class UserTestCase(TestCase):
    def test_random_user(self):
        users = UserFactory.create_batch(10)
        expected_length = 10
        self.assertEqual(expected_length, len(users))
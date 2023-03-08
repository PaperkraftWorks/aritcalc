from users.services import get_user_by_id
from django.test import TestCase
from users.tests.factories import UserFactory
from users.dataclasses import UserData
from uuid import uuid4

class GetUserByIdTestCase(TestCase):
    def test_existent_user(self):
        user = UserFactory()
        user.save()
        
        received_object = get_user_by_id(user_id=user.id)
        
        self.assertIsInstance(received_object, UserData)
        self.assertEqual(user.id, received_object.id)
        self.assertEqual(user.status, received_object.status)
        self.assertEqual(user.username, received_object.username)
        
        
    def test_non_existent_user(self):
        fake_id = uuid4()
        received_object = get_user_by_id(user_id=fake_id)
        
        self.assertIsNone(received_object)
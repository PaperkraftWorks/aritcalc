from users.tests.factories import UserFactory
from users.providers import get_user_by_id
from users.models import User
from django.test import TestCase
from uuid import uuid4

class GetUserTestCase(TestCase):
    def test_return_one_user(self):
        expected_user_id = uuid4()
        UserFactory(id=expected_user_id).save()
        
        received_user = get_user_by_id(user_id=expected_user_id)
        
        self.assertIsInstance(received_user, User)
        self.assertEqual(expected_user_id, received_user.id)
        
    def test_return_none(self):
        expected_user_id = uuid4()
        unexpected_user_id = uuid4()
    
        UserFactory(id=expected_user_id).save()
        
        received_user = get_user_by_id(user_id=unexpected_user_id)
        
        self.assertIsNone(received_user)
        
        
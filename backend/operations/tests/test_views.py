from operations.tests.factories import OperationFactory
from django.test import TestCase, Client
from django.conf import settings
from django.urls import reverse
from users.tests.factories import UserFactory
from rest_framework.test import force_authenticate
from django.test.client import encode_multipart, RequestFactory
from rest_framework.test import APIClient

class OperationsViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(is_superuser=True, password='1234')
        operation_types = ['ADD', 'MUL', 'SUB', 'DIV']
        self.operations_list = [OperationFactory(type=i) for i in operation_types]
        self.name = 'operations'
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.expected_structure = [
            'count',
            'next',
            'previous',
            'results',
        ]
        
    def test_get_paginated_all_pages(self):
        url = reverse(self.name)
        expected_total_count = 4
        expect_page_one_count = 3
        expect_page_two_count = 1
        
        received_return = self.client.get(url)
        self.assertListEqual(self.expected_structure, list(received_return.json().keys()))
        self.assertEqual(expected_total_count, received_return.json().get('count'))
        self.assertEqual(expect_page_one_count, len(received_return.json().get('results')))
        received_next_page = received_return.json().get('next')
        received_second_page = self.client.get(received_next_page)
        self.assertListEqual(
            self.expected_structure,
            list(received_second_page.json().keys())
        )
        self.assertEqual(expected_total_count, received_second_page.json().get('count'))
        self.assertEqual(expect_page_two_count, len(received_second_page.json().get('results')))
        received_next_page = received_second_page.json().get('next')
        self.assertIsNone(received_next_page)


        
from operations.tests.factories import OperationFactory
from django.test import TestCase

class OperationFactoryTestCase(TestCase):
    def test_factory_ten_obj(self):
        operations = OperationFactory.create_batch(10)
        expected_length = 10
        
        self.assertEqual(expected_length, len(operations))
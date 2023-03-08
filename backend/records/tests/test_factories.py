from records.tests.factories import RecordFactory
from django.test import TestCase

class RecordFactoryTestCase(TestCase):
    def test_random_10(self):
        
        random_10_records = RecordFactory.create_batch(10)
        expected_length = 10
        self.assertEqual(expected_length, len(random_10_records))
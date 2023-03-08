from operations import services as operations_services
from typing import Optional, Literal
from operations.constants import TYPE_CHOICES
from operations.dataclasses import OperationData
from django.test import TestCase
from operations.tests.factories import OperationFactory

class GetOperationByTypeTestCase(TestCase):
    def test_existent_type(self):
        for _type in list(zip(*TYPE_CHOICES))[0][-1]:
            with self.subTest(_type=_type):
                operation = OperationFactory(type=_type)
                operation.save()
                expected_id = operation.id
                expected_cost = operation.cost
                received_output = operations_services.get_operation_by_type(_type=_type)
                self.assertIsInstance(received_output, OperationData)
                self.assertEqual(expected_cost, received_output.cost)
                self.assertEqual(expected_id, received_output.id)
                
    def test_non_existent_type(self):
        fake_type='ZZZ'
        received_output = operations_services.get_operation_by_type(_type=fake_type)
        self.assertIsNone(received_output)
        
from operations import providers as operations_providers
from django.test import TestCase
from operations.models import Operation
from operations.tests import factories as operations_factories
from operations.constants import TYPE_CHOICES

class GetOperationByTypeTestCase(TestCase):
    def test_existent_operation(self):
        for _type in list(zip(*TYPE_CHOICES))[0][:-1]:
            with self.subTest(_type=_type):
                operation_obj = operations_factories.OperationFactory(type=_type)
                operation_obj.save()
                
                expected_operation_id = operation_obj.id
                expected_operation_cost = operation_obj.cost
                
                
                received_operation = operations_providers.get_operation_by_type(_type=_type)
                
                self.assertIsInstance(received_operation, Operation)
                self.assertEqual(expected_operation_cost, received_operation.cost)
                self.assertEqual(expected_operation_id, received_operation.id)
        
    def test_non_existent_operation(self):
        fake_type= list(zip(*TYPE_CHOICES))[0][-1]
        received_operation = operations_providers.get_operation_by_type(_type=fake_type)
        
        self.assertIsNone(received_operation)
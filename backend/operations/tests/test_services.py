from operations import services as operations_services
from typing import Optional, Literal, List
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
        
class FilterOperationByTypeTestCase(TestCase):
    def test_existent_single_operation(self):
        for _type in list(zip(*TYPE_CHOICES))[0][:-1]:
            with self.subTest(_type=_type):
                operation_obj = OperationFactory(type=_type)
                operation_obj.save()
                
                expected_operation_cost = operation_obj.cost
                expected_count = 1
                
                
                received_cost_list = operations_services.get_operation_cost_list_by_type(operation_types=[_type])
                self.assertEqual(expected_count, len(received_cost_list))
                self.assertEqual([expected_operation_cost], received_cost_list)
    def test_existent_multiple_operations(self):
        types = list(zip(*TYPE_CHOICES))[0][:-1]
        expected_length = len(types)
        operation_objs = [OperationFactory(type=_type) for _type in types]
        expected_costs = [operation.cost for operation in operation_objs]
        
        received_cost = operations_services.get_operation_cost_list_by_type(operation_types=types)
        self.assertEqual(expected_length, len(received_cost))
        self.assertListEqual(expected_costs, received_cost)
        
    def test_non_existent_operation(self):
        fake_type= ["FFF"]
        received_operation = operations_services.get_operation_cost_list_by_type(operation_types=fake_type)
        
        self.assertIsNone(received_operation)
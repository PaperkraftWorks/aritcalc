from records import business_rules as records_business_rules
from unittest import TestCase
from records.tests import factories as records_factories
from records.dataclasses import RecordData
from datetime import datetime
from records.constants import OK_REASON, INSUFICIENT_FUNDS_REASON,USER_DOES_NOT_EXIST_REASON
from uuid import uuid4
from operations.tests.factories import OperationFactory
from operations.constants import TYPE_CHOICES
from random import sample, randint, choices

class GetLastUserBalancePerUserIdtestCase(TestCase):
    def test_get_existent_user_balance(self):
        record_first:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,1,0,0,1), user_balance = 10000000
            )
        user = record_first.user
        record_last:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,3,0,0,1), user_id=user.id, user_balance=1200000
            )
        record_first.save(); record_last.save()
        
        expected_user_balance = 1200000
        received_user_balance = records_business_rules.get_last_user_balance_per_user_id(user_id=user.id)
        
        self.assertEqual(expected_user_balance, received_user_balance)
        
    def test_get_nonexistent_user_balance(self):
        record_first:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,1,0,0,1), user_balance = 10000000
            )
        user = record_first.user
        record_last:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,3,0,0,1), user_id=user.id, user_balance=1200000
            )
        record_first.save(); record_last.save()
        
        fake_user_uuid = uuid4()
        received_user_balance = records_business_rules.get_last_user_balance_per_user_id(user_id=fake_user_uuid)
        
        self.assertIsNone(received_user_balance)
        
class IsBalanceForOperationEnoughTestCase(TestCase):
    def setUp(self):
        self.user_balance = 1000000
        last_record = records_factories.RecordFactory(user_balance=1000000)
        self.user_id = last_record.user_id
    def test_user_has_suficient_funds(self):
        cost=100000
        received_return = records_business_rules.is_balance_for_operation_enough(cost=cost, user_id=self.user_id)
        self.assertTrue(received_return)
    def test_user_has_insuficient_funds(self):
        cost=10000000
        received_return = records_business_rules.is_balance_for_operation_enough(cost=cost, user_id=self.user_id)
        self.assertFalse(received_return)
    def test_user_has_no_record(self):
        cost=10000000
        received_return = records_business_rules.is_balance_for_operation_enough(cost=cost, user_id=uuid4())
        self.assertIsNone(received_return)
    
class GenerateReasontestCase(TestCase):
    def test_user_dont_exist(self):
        authorized = None
        reason = USER_DOES_NOT_EXIST_REASON
        expected_return = {
        "authorized":authorized,
        "reason": reason
        }
        received_return = records_business_rules.generate_response(authorized=authorized)
        self.assertDictEqual(expected_return,received_return)
        
    def test_user_insuficient_funds(self):
        authorized = False
        reason = INSUFICIENT_FUNDS_REASON
        expected_return = {
        "authorized":authorized,
        "reason": reason
        }
        received_return = records_business_rules.generate_response(authorized=authorized)
        self.assertDictEqual(expected_return,received_return)
        
    def test_user_ok(self):
        authorized = True
        reason = OK_REASON
        expected_return = {
        "authorized":authorized,
        "reason": reason
        }
        received_return = records_business_rules.generate_response(authorized=authorized)
        self.assertDictEqual(expected_return,received_return)
        
        
class TotalCostTestCase(TestCase):
    def setUp(self):
        all_types =  list(zip(*TYPE_CHOICES))[0]
        self.operation_objs = [OperationFactory(type=_type) for _type in all_types]
    
    def test_single_operation_cost(self):
        for operation in self.operation_objs:
            with self.subTest(operation=operation):
                expected_value = operation.cost
                received_return = records_business_rules.total_cost(operation_type_list=[operation.type])
                
                self.assertEqual(expected_value, received_return)
                
    def test_multiple_operations(self):
        operations_t = [choices(self.operation_objs, k=randint(2,40)) for i in range(randint(2,10))]
        for operations in operations_t:
            with self.subTest(operations=operations):
                expected_operations_cost = sum([operation.cost for operation in operations])
                operation_type_list = [operation.type for operation in operations]
                received_return = records_business_rules.total_cost(operation_type_list=operation_type_list)
                self.assertEqual(expected_operations_cost, received_return)
            
            
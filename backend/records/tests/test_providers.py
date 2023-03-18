from records.providers import create_record, get_last_record_by_user_id
from django.test import TestCase
from operations.models import Operation
from records.models import Record
from users.models import User
from operations.tests import factories as operatons_factories
from users.tests import factories as users_factories
from records.tests.factories import RecordFactory
import random
from records.constants import MAX_BALANCE_VALUE_FACTORY, MIN_BALANCE_VALUE_FACTORY

class CreateRecordTestCase(TestCase):
    def test_common_record(self):
        operation = operatons_factories.OperationFactory()
        user = users_factories.UserFactory()
        operation.save()
        user.save()
        amount = random.randint(MIN_BALANCE_VALUE_FACTORY, MAX_BALANCE_VALUE_FACTORY)
        user_balance = random.randint(MIN_BALANCE_VALUE_FACTORY, MAX_BALANCE_VALUE_FACTORY)
        operation_response = "test operation ok"
        
        received_record = create_record(
            operation_id=operation.id,
            user_id=user.id,
            amount=amount,
            user_new_balance=user_balance,
            operation_response=operation_response
        )
        
        self.assertIsInstance(received_record, Record)
        self.assertEqual(received_record.operation_id, operation.id)
        self.assertEqual(received_record.user_id, user.id)
        self.assertEqual(received_record.amount, amount)
        self.assertEqual(received_record.operation_response, operation_response)
        
class GetLastRecordByUserID(TestCase):
    def test_has_record_one_record(self):
        user = users_factories.UserFactory()
        operation= operatons_factories.OperationFactory()
        user.save()
        operation.save()
        record = RecordFactory(user=user, operation=operation)
        record.save()
        
        user = record.user
        
        received_record = get_last_record_by_user_id(user_id=user.id)
        
        self.assertIsInstance(received_record, Record)
        self.assertEqual(received_record.id, received_record.id)
        
    def test_has_record_several_records(self):
        user = users_factories.UserFactory()
        operation= operatons_factories.OperationFactory()
        user.save()
        operation.save()
        records = RecordFactory.create_batch(100, user=user, operation=operation)
        [record.save() for record in records]
        
        received_record = get_last_record_by_user_id(user_id=user.id)
        
        self.assertIsInstance(received_record, Record)
        
        
    
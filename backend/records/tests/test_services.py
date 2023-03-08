from records import services as record_services
from unittest.mock import MagicMock
from django.test import TestCase
from records.tests import factories as records_factories
from records.dataclasses import RecordData
from datetime import datetime, tzinfo
from uuid import uuid4

class GetLastRecordByUserIDTest(TestCase):
    def test_existent_record(self):
        record_first:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,1,0,0,1), user_balance = 10000000
            )
        user = record_first.user
        record_last:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,3,0,0,1), user_id=user.id, user_balance=1200000
            )
        record_first.save(); record_last.save()
        
        expected_user_balance = 1200000
        expected_operation_id = record_last.operation_id
        expected_amount = record_last.amount
        expected_operation_response = record_last.operation_response
        expected_id = record_last.id
        
        received_record  = record_services.get_last_record_by_user_id(user_id=user.id)
        self.assertIsInstance(received_record, RecordData)
        self.assertEqual(expected_amount, record_last.amount)
        self.assertEqual(expected_operation_id, record_last.operation_id)
        self.assertEqual(expected_operation_response, record_last.operation_response)
        self.assertEqual(expected_user_balance, record_last.user_balance)
        self.assertEqual(expected_id, record_last.id)
        
    def test_existent_record(self):
        record_first:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,1,0,0,1), user_balance = 10000000
            )
        user = record_first.user
        record_last:RecordData = records_factories.RecordFactory(
            date=datetime(2023,1,3,0,0,1), user_id=user.id, user_balance=1200000
            )
        record_first.save(); record_last.save()
        
        expected_user_balance = 1200000
        expected_operation_id = record_last.operation_id
        expected_amount = record_last.amount
        expected_operation_response = record_last.operation_response
        expected_id = record_last.id
        
        received_record  = record_services.get_last_record_by_user_id(user_id=user.id)
        self.assertIsInstance(received_record, RecordData)
        self.assertEqual(expected_amount, record_last.amount)
        self.assertEqual(expected_operation_id, record_last.operation_id)
        self.assertEqual(expected_operation_response, record_last.operation_response)
        self.assertEqual(expected_user_balance, record_last.user_balance)
        self.assertEqual(expected_id, record_last.id)
        
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
        received_user_balance = record_services.get_last_record_by_user_id(user_id=fake_user_uuid)
        
        self.assertIsNone(received_user_balance)
        
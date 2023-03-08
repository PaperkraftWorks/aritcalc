from records import business_rules as records_business_rules
from unittest import TestCase
from records.tests import factories as records_factories
from records.dataclasses import RecordData
from datetime import datetime
from uuid import uuid4

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
        
    
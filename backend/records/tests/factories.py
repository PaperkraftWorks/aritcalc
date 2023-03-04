import factory
from records.models import Record
import random
from records.constants import (
    MAX_BALANCE_VALUE_FACTORY,
    MIN_BALANCE_VALUE_FACTORY,
)
from users.tests.factories import UserFactory
from operations.tests.factories import OperationFactory

class RecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Record
    
    amount = factory.Faker("pyint", min_value=MIN_BALANCE_VALUE_FACTORY, max_value=MAX_BALANCE_VALUE_FACTORY)
    user_balance = factory.Faker("pyint", min_value=MIN_BALANCE_VALUE_FACTORY, max_value=MAX_BALANCE_VALUE_FACTORY)
    user = factory.SubFactory(UserFactory)
    operation = factory.SubFactory(OperationFactory)
    

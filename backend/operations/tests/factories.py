from operations.models import Operation
from operations.constants import TYPE_CHOICES, MAX_COST_FACTORY, MIN_COST_FACTORY
import factory
import factory.fuzzy
import random

class OperationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Operation
        django_get_or_create = ("type",)
    type = factory.fuzzy.FuzzyChoice(choices=list(zip(*TYPE_CHOICES))[0])
    cost = factory.Faker("pyint", min_value=MIN_COST_FACTORY, max_value=MAX_COST_FACTORY)
    
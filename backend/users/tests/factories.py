from users.models import User
import factory
import factory.fuzzy
from users.constants import STATUS_CHOICES

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    status = factory.fuzzy.FuzzyChoice(choices=list(zip(*STATUS_CHOICES))[0])
    username=factory.Faker("email")
    
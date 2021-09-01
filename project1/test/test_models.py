from django.test import TestCase
from travel.models import Destination


class TestModels(TestCase):

    def setUp(self):
        self.dest1 = Destination.object.create(
            name = 'kolkata',
            desc = 'the city of joy',
            price = 700,
            offer = False
        )
        
    


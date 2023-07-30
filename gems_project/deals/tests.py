from django.test import TestCase

from deals.models import Gem


class TestModelGem(TestCase):
    """Testing Gem model."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.gem = Gem.objects.create(name='Diamond')

    def test_objects_have_correct_names(self):
        """Checks __str__ method is object name."""
        gem = self.__class__.gem
        self.assertEqual(str(gem), gem.name)

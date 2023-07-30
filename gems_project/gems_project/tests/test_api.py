from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from api.views import CustomerAPIView
from deals.models import Customer, Deal, Gem

TEST_URL = 'http://testserver/api/v1/clients/'


class TestCustomerAPIView(APITestCase):
    """Testing Customer view class."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.gem_diamond = Gem.objects.create(name='Diamond')
        cls.gem_emerald = Gem.objects.create(name='Emerald')
        cls.gem_ruby = Gem.objects.create(name='Ruby')
        cls.client_nick = Customer.objects.create(
            username='Nick',
            spent_money=100
        )
        cls.client_mike = Customer.objects.create(
            username='Mike',
            spent_money=200
        )
        for client in Customer.objects.all():
            cls.gem_diamond.customers.add(client)
        cls.gem_emerald.customers.add(cls.client_nick)
        cls.gem_ruby.customers.add(cls.client_mike)

    def test_customer_cache_has_correct_data(self):
        """Checks Customer view returns correct data from cache."""
        nick = self.__class__.client_nick
        mike = self.__class__.client_mike
        diamond = self.__class__.gem_diamond
        template = [
            {
                'username': mike.username,
                'spent_money': mike.spent_money,
                'gems': [
                    str(diamond)
                ]
            },
            {
                'username': nick.username,
                'spent_money': nick.spent_money,
                'gems': [
                    str(diamond)
                ]
            },
        ]
        CustomerAPIView.update_cache()
        data = CustomerAPIView.get_cache()
        self.assertEqual(data, template)

    def test_api_handlers_file_correctly(self):
        """Checks parsing results of .csv file."""
        file_path = 'gems_project/tests/fixtures/test_data.csv'
        file = {'deals': open(file_path, 'rb')}
        client = RequestsClient()
        response = client.post(TEST_URL, files=file)
        data_string = r'customer,Diamond,342,2,2018-12-15 15:00:59.858739'
        username, gem, total, quantity, date = data_string.split(',')
        self.assertTrue(
            Customer.objects.filter(
                username=username,
                spent_money=total
            ).exists()
        )
        self.assertTrue(
            Gem.objects.filter(name=gem).exists()
        )
        self.assertTrue(
            Deal.objects.filter(
                customer=Customer.objects.get(username=username),
                item=Gem.objects.get(name=gem),
                total=total,
                quantity=quantity,
                date=date
            ).exists()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'Status': 'OK'})

    def test_get_returns_correct_response(self):
        """Checks structure of get endpoint response."""
        response = self.client.get(TEST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('response' in response.data)

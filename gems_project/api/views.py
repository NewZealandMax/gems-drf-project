from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.schemas import customer_response, deals_response, deals_schema
from deals.models import Customer, Deal, Gem
from deals.serializers import CustomerSerializer


class CustomerAPIView(APIView):
    """Handlers Customers' info."""

    __cached_response = None

    @swagger_auto_schema(responses=customer_response)
    def get(self, request):
        if self.get_cache() is None:
            self.update_cache()
        return Response(
            {
                'response': self.get_cache(),
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=deals_schema,
        responses=deals_response
    )
    def post(self, request):
        if 'deals' not in request.data:
            return Response(
                {
                    'Status': 'Error',
                    'Desc': 'Field \"deals\" is required.',
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        file = request.data.get('deals')
        try:
            lines = iter(file)
            next(lines)
            for line in lines:
                deal_data = line.decode(encoding='utf-8').strip().split(',')
                username, gem, total, quantity, date = deal_data
                try:
                    total, quantity = map(int, (total, quantity))
                except ValueError:
                    return Response(
                        {
                            'Status': 'Error',
                            'Desc': 'Данные в \"total\" или \"quantity\" '
                                    'не являются целым числом '
                                    '- в процессе обработки файла произошла ошибка.'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                customer, client_created = Customer.objects.get_or_create(
                    username=username
                )
                customer.spent_money += total
                customer.save()
                gem, gem_created = Gem.objects.get_or_create(name=gem)
                gem.customers.add(customer)
                Deal.objects.create(
                    customer=customer,
                    item=gem,
                    total=total,
                    quantity=quantity,
                    date=date
                )
        except Exception:
            return Response(
                {
                    'Status': 'Error',
                    'Desc': 'Ошибка: убедитесь, что в поле \"deals\" '
                            'передан файловый объект в правильном формате '
                            '- в процессе обработки файла произошла ошибка.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        self.update_cache()
        return Response({'Status': 'OK'}, status=status.HTTP_200_OK)

    @classmethod
    def get_cache(cls):
        return cls.__cached_response

    @classmethod
    def update_cache(cls):
        customers = Customer.objects.order_by('-spent_money')[:5]
        serializer = CustomerSerializer(customers, many=True)
        cls.__cached_response = serializer.data

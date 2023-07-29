from drf_yasg import openapi
from rest_framework import status

customer_response = {
    status.HTTP_200_OK: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'response': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'username': openapi.Schema(
                            type=openapi.TYPE_STRING
                        ),
                        'spent_money': openapi.Schema(
                            type=openapi.TYPE_INTEGER
                        ),
                        'gems': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_STRING
                            )
                        ),
                    },
                )
            ),
        }
    )
}

deals_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'deals': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='.csv file in bytes string'
        ),
    },
    required=['deals']
)

deals_response = {
    status.HTTP_200_OK: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'Status': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='OK'
            )
        }
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'Status': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='Error'
            ),
            'Desc': openapi.Schema(
                type=openapi.TYPE_STRING
            )
        }
    ),
}

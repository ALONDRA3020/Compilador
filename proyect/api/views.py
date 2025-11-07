from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def main(request):
    return Response(
        {"mensaje":"Hola"},
        status=status.HTTP_200_OK
    )
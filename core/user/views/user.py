from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers.user import UserSerializer

def notexist():
    return {"error": "Los datos no fueron encontrados"}


class UserView(APIView):
    filter_fields = ["username", "first_name", "last_name"]

    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)

        # Filtros
        filters = {}
        for field in self.filter_fields:
            value = request.query_params.get(field)
            if value is not None:
                filters[field + "__icontains"] = value  # para búsqueda parcial

        if filters:
            queryset = User.objects.filter(**filters)
            if not queryset.exists():
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = User.objects.all()

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

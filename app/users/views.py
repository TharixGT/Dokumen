"""Summary."""
from blindjupp.common.generics import BlindjuppApiViewSet
from blindjupp.users import models as users_models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponseForbidden, HttpResponseBadRequest
from django.utils.translation import ugettext_lazy as _


class UserApiViewSet(BlindjuppApiViewSet):
    """Summary.

    Attributes:
        queryset (TYPE): Description
        serializer_class (TYPE): Description
    """

    queryset = users_models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """Summary.

        Returns:
            TYPE: Description
        """
        queryset = super(UserApiViewSet, self).get_queryset()
        return queryset


@api_view(['POST'])
def change_password(request):
    """Retrieve a price of edition and competition by customer and edition."""
    if not request.user.id:
        return HttpResponseForbidden()
    password = request.data.get('password', None)
    password2 = request.data.get('password2', None)
    current = request.data.get('current', None)
    if not password or not password2 or not current:
        return HttpResponseBadRequest()
    user = request.user
    if not user.check_password(current):
        return Response({
            'current': _('Current password invalid')},
            status=status.HTTP_400_BAD_REQUEST)
    if password2 != password:
        return Response({
            'password2': _('Passwords do not match')},
            status=status.HTTP_400_BAD_REQUEST)

    user.set_password(password)
    user.save()
    return Response(status=status.HTTP_200_OK)

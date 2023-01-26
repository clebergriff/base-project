from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


class AuthenticatedView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    pass


class AllowPostOnlyPermission(GenericAPIView):
    """
    The request is permitted only if the method is POST
    """

    def has_permission(self, request, view):
        if (request.method == 'POST' or
                request.user and request.user.is_authenticated()):
            return True
        return False

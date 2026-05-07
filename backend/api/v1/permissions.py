from rest_framework.permissions import BasePermission
from api.v1.constants import UPDATE_REQUEST_METHODS

class IsPortfolioOwner(BasePermission):
    """Права пользователя для взаимодействия со своим портфолио"""
    def has_object_permission(self, request, view, obj):
        if request.method in UPDATE_REQUEST_METHODS:
            if request.user.id == obj.user.id:
                return True
            else:
                return False
        else:
            return True
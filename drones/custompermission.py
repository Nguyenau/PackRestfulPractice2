from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      # the method is a safe method: GET
      return True
    else:
      # the method isn't a safe method
      # only owners are granted permissions for unsafe methods
      return obj.owner == request.user

    
"""
authentication or identification by itself is not usually sufficient to gain information | code.
 entity requesting access must have authorization .
 
 authentication + throttling : together determine if request granted | denied 
 
 permission checks run at start of the view. before any other code.
 
 mainly and mostly uses request.user |& request.auth
 
 """
  IsAuthenticated  
  
  """
  Permissions in REST framework are always defined as a list of permission classes.
  
  before running the main body , each permision in the list is checked 
  
  if any permission fails -exceptions.PermissionDenied or
                          -exceptions.NotAuthenticated
  
  and the main body wont run 
  """
  
 """
 Object Level Permissions::
  are used to determine if a user should be allowed to act on a particular object.which will be a modal instance.
  
 - run by generic views when .get_object() is called. exceptions.PermissionDenied raised if not.
 - if want to enforce or override , ecplicitly call .check_object_permissions(request, obj) .
 at the point at which you've retrieved the object.
 
 
"""
 
 """
default permission policy set globally , using DEFAULT_PERMISSION_CLASSES

"""
 ------------------------
 REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES':(
     'rest_framework.permissions.isAuthenticated',
  )
 }
 
 ------------------------
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ExampleView(APIView):
    permission_classes = (IsAuthenticated|ReadOnly,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
     

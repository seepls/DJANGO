"""
class - based views : APIView 
requests passed to the handler method will be REST framework's request instances
incoming request dispatched to appropritate handler method such as .get() and .post()

"""

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import authentication , permissions
from django.contrib.auth.models import User 

class ListUsers(APIView):
    """ View to list all users in the system 
    * only admin users are able to access the view
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    
    def get(self,request  , format = None):
        """
        return list of all users
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
        
   
   
   
"""

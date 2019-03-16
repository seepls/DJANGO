"""
set of simple decorators that wrap your function based views to ensure that they recieve an Instance of request and allows
them to run the response , and allow to configure how the request is processed 
"""

@api_view()
"""
The core of this functionality is the api_view decorator, which takes a list of HTTP methods that your view should respond to. 
"""
from rest_framework.decorators import api_view

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
    
"""
By default only GET methods will be accepted.
To alter this behaviour, specify which methods the view allows.
"""

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
    
"""
The available decorators are:

@renderer_classes(...)
@parser_classes(...)
@authentication_classes(...)
@throttle_classes(...)
@permission_classes(...)
"""

"""
To override the default schema generation for function based views you may use the @schema decorator
"""
from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...

@api_view(['GET'])
@schema(CustomAutoSchema())
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

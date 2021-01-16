import jwt
import json

from django.http    import JsonResponse

from my_settings    import SECRET_KEY, ALGORITHM
from user.models    import User

email_regax    = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
password_regax = '[A-Za-z0-9@#$]{10,1000}'

def login_decorator(func):
    def wrapper(self,request, *args, **kwargs):
        try:
            token        = request.headers.get("Authorization")
            payload      = jwt.decode(token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id=payload['use-id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'})
        
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'})

        return func(self, request, *args, **kwargs)

    return wrapper

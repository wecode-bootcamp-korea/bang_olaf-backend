import json
import re
import bcrypt
import jwt


from django.views import View
from django.http  import JsonResponse


from user.models  import Users
from user.utils   import email_regax, password_regax
from my_settings  import ALGORITHM, SECRET

class SignView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            first_name              = data['first_name']
            last_name               = data['last_name']
            email                   = data['email']
            password                = data['password']
            confirm_password        = data['confirm_password']
            receive_communications  = data['receive_communications']

            if not first_name:
                return JsonResponse({'MESSAGE' : 'FIRST_NAME_IS_REQUIRED'}, status=400)

            if not last_name:
                return JsonResponse({'MESSAGE' : 'LAST_NAME_IS_REQUIRED'}, status=400)

            if not email:
                return JsonResponse({'MESSAGE' : 'EMAIL_IS_REQUIRED'}, status=400)

            if not password:
                return JsonResponse({'MESSAGE' : 'PASSWORD_IS_REQUIRED'}, status=400)

            if not confirm_password:
                return JsonResponse({'MESSAGE' : 'CONFRIM_PASSWORD_IS_REQUIRED'}, status=400)

            if not re.search(email_regax, email):
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL'}, status=400)

            if Users.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE' : 'EXIST_USER'}, status=401)

            if not re.search(password_regax, password):
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status=400)

            if not password == confirm_password:
                return JsonResponse({'MESSAGE' : 'PASSWORD_UNMATCH'}, status=400)

            save_password    = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            Users.objects.create(
                first_name             = first_name,
                last_name              = last_name,
                email                  = email,
                password               = save_password,
                receive_communications = receive_communications
            )
     
            return JsonResponse({'MESSAGES' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERRORS'}, status=400)


class LoginView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            
            email          = data['email']
            input_password = data['password']
            users          = Users.objects.get(email=email)
            
            if not email:
                return JsonResponse({'MESSAGE' : 'EMAIL_IS_REQUIRED'}, status=400)

            if not input_password:
                return JsonResponse({'MESSAGE' : 'PASSWORD_IS_REQUIRED'}, status=400)
            
            if bcrypt.chechpw(input_password.encode('utf-8'), users.password.encode('utf-8')):
                token = jwt.encode({'user-id' : users.id}, SECRET, ALGORITHM)

                return JsonResponse({token : 'token'}, status=200)
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=401)
  
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERRORS'}, status=400)

        except Users.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=400)
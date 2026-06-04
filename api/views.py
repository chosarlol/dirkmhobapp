from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def admin_login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Check user credentials
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Restrict login access to staff or admin roles
                if user.is_staff or user.is_superuser:
                    login(request, user)
                    return JsonResponse({'status': 'success', 'message': 'Admin logged in'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Not authorized as admin'}, status=403)
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)

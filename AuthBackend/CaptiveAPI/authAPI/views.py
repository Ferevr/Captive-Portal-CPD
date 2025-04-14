from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .radius_client import authenticate_with_radius

# Create your views here.
@csrf_exempt
def radius_login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if authenticate_with_radius(username, password):
                return JsonResponse({"success": True}, status=200)
            else:
                return JsonResponse({"success": False, "error": "Acceso denegado"}, status=401)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
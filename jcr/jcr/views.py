from django.http.response import JsonResponse

def index(request):
    return JsonResponse({'healthy': True})
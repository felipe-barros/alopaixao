from django.shortcuts import render
from .models import Deslike
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})

# Create your views here.
def deslikes(request):
    data = Deslike.objects.all().order_by('-created_date')  # ordena do mais novo pro mais antigo
    return render(request, 'core/deslikes.html', {'deslikes': data})

@csrf_exempt  # Permite que a requisição POST sem CSRF falhe se não houver um token adequado
def atualizar_mico(request, deslike_id):
    if request.method == 'POST':
        try:
            deslike = Deslike.objects.get(id=deslike_id)
            deslike.likes_count += 1
            deslike.save()

            return JsonResponse({
                'success': True,
                'new_count': deslike.likes_count
            })
        except Deslike.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Deslike não encontrado.'}, status=404)
    return JsonResponse({'success': False, 'error': 'Método não permitido.'}, status=405)
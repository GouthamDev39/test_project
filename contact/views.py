
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage  
from django.shortcuts import render



def index(request):
    return render(request, 'contacts/index.html')


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            message = data.get('message')

            # Validate data (optional but recommended)
            if not name or not message:
                return JsonResponse({'error': 'Name and message are required.'}, status=400)

            # Save to DB
            ContactMessage.objects.create(name=name, message=message)

            return JsonResponse({'message': f'Thank you, {name}! We received your review.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST allowed'}, status=405)


def contact_page(request):
    return render(request, 'contacts/contacts.html')

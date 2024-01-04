# frontend/views.py
from django.shortcuts import render
from django.http import JsonResponse

def form_view(request):
    return render(request, 'form.html')

def submit_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Get other form fields as needed

        # Handle the data (e.g., save to database)
        # ...

        # Return a JSON response
        return JsonResponse({'message': 'Data submitted successfully!'})

    # Handle other HTTP methods
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


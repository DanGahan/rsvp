import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.shortcuts import render, redirect

def form_view(request):
    return render(request, 'form.html')

def success_page_view(request):
    return render(request, 'success.html')  # replace 'path_to_static_page.html' with the actual path to your static HTML file

def submit_data(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        plus_one = request.POST.get('plus_one')
        plus_one_name = request.POST.get('plus_one_name')
        song_suggestion = request.POST.get('song_suggestion')

        # Prepare data for API call
        data = {
            'name': name,
            'plus_one': plus_one,
            'plus_one_name': plus_one_name,
            'song_suggestion': song_suggestion
        }

        headers = {
            'Content-Type': 'application/json',
        }

        # Make API call to backend
        api_url = 'http://backend:5000/rsvp'
        
        response = requests.post(api_url, headers=headers, data=json.dumps(data))

        # Check if API call was successful
        if response.status_code == 201:
            # Process the API response if needed
            #api_response = response.json()
            # ...
            #return JsonResponse({'status': 'success', 'message': 'Data submitted successfully'})
            return redirect('success_page')
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to submit data to backend'}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

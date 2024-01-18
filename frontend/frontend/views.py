import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.shortcuts import render, redirect

##########################################################
#Views for frontend pages                                #
##########################################################
def header_view(request):
    return render(request, 'header.html')

def footer_view(request):
    return render(request, 'footer.html')

def form_view(request):
    return render(request, 'form.html')

##########################################################
#POST into backend API for RSVP submission               #
##########################################################
def submit_data(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        attending = request.POST.get('attending')
        vegetarian = request.POST.get('vegetarian')
        plus_one = request.POST.get('plus_one')
        plus_one_name = request.POST.get('plus_one_name')
        plus_one_vegetarian = request.POST.get('plus_one_vegetarian')
        song_suggestion = request.POST.get('song_suggestion')

        # Prepare data for API call
        data = {
            'name': name,
            'attending': attending,
            'vegetarian': vegetarian,
            'plus_one': plus_one,
            'plus_one_name': plus_one_name,
            'plus_one_vegetarian': plus_one_vegetarian,
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
                    # Redirect to the success page with a success parameter
           request.session['rsvp_success'] = True
           return redirect('success_page')
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to submit data to backend'}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

##########################################################################
#Set RSVP message on success page if navigated to from RSVP Post         #
##########################################################################
def success_page_view(request):
    rsvp_success = request.session.get('rsvp_success', False)
    if rsvp_success: 
            success_message = 'RSVP submitted successfully!'
            return render(request, 'success.html', {'success_message': success_message})
    else: 
        return render(request, 'success.html')

##########################################################
#GET into backend API to retrieve all rsvps              #
##########################################################
def get_all_rsvps(request):
    all_rsvps_url = 'http://backend:5000/rsvps'  # Update the URL to match your Flask API endpoint
    all_evening_rsvps_url = 'http://backend:5000/evening_rsvps'
    
    all_rsvps_response = requests.get(all_rsvps_url)
    all_evening_rsvps_response = requests.get(all_evening_rsvps_url)
    
    if all_rsvps_response.status_code == 200 and all_evening_rsvps_response.status_code == 200:
        rsvps_data = all_rsvps_response.json()
        evening_rsvps_data = all_evening_rsvps_response.json() 
        
        return render(request, 'all_rsvps.html', {'rsvps_data': rsvps_data, 'evening_rsvps_data': evening_rsvps_data})
    else:
        # Handle the API error
        return render(request, 'error_page.html', {'error_message': 'Failed to fetch RSVP data'})

#########################################################
#GET into backend API to retrieve all rsvps              #
##########################################################
def get_all_evening_rsvps(request):
    api_url = 'http://backend:5000/evening_rsvps'  # Update the URL to match your Flask API endpoint
    response = requests.get(api_url)

    if response.status_code == 200:
        evening_rsvps_data = response.json()
        return render(request, 'all_rsvps.html', {'evening_rsvps_data': evening_rsvps_data})
    else:
        # Handle the API error
        return render(request, 'error_page.html', {'error_message': 'Failed to fetch evening RSVP data'})
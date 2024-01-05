// frontend/static/js/form.js

$(document).ready(function() {
    $('#submitForm').submit(function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Gather the form data
        var formData = {
            'name': $('#name').val(),
            'plus_one': $('#plus_one').val(),
            'plus_one_name' $('#plus_one_name').val(),
            'song_suggestion' $('#song_suggestion').val(),
            // Add other form fields as needed
        };

        // Make an AJAX request to the backend API
        $.ajax({
            type: 'POST',
            url: 'http://backend:5000/rsvp/',  // Update the URL to match your backend API endpoint
            data: formData,
            dataType: 'json',
            success: function(response) {
                // Handle the successful API response
                console.log(response);
                alert('Data submitted successfully!');
            },
            error: function(error) {
                // Handle the API error
                console.log(error);
                alert('An error occurred while submitting the data.');
            }
        });
    });
});


$(document).ready(function() {
    // Event handler when the document is ready

    $('#plus_one').on('change', function() {
        var plusOneValue = $(this).val();
        if (plusOneValue === 'Yes') {
            $('#plus_one_name').prop('disabled', false);
        } else {
            $('#plus_one_name').prop('disabled', true);
        }
    });
  });

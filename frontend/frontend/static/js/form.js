$(document).ready(function() {
    // Initialize the form elements
    var attendingSelect = $("#attending");
    var vegetarianSelect = $("#vegetarian");
    var plusOneSelect = $("#plus_one");
    var plusOneNameInput = $("#plus_one_name");
    var plusOneVegetarianSelect = $("#plus_one_vegetarian");
    var songSuggestionInput = $("#song_suggestion");
  
    // Disable initial form elements
    vegetarianSelect.prop("disabled", true).addClass("disabled");
    plusOneSelect.prop("disabled", true).addClass("disabled");
    plusOneNameInput.prop("disabled", true).addClass("disabled");
    plusOneVegetarianSelect.prop("disabled", true).addClass("disabled");
    songSuggestionInput.prop("disabled", true).addClass("disabled");
  
    // Enable or disable form elements based on the selected values
    attendingSelect.on("change", function() {
      var attendingValue = attendingSelect.val();
  
      if (attendingValue === "Yes") {
        vegetarianSelect.prop("disabled", false).removeClass("disabled");
        plusOneSelect.prop("disabled", false).removeClass("disabled");
  
        if (plusOneSelect.val() === "Yes") {
          plusOneNameInput.prop("disabled", false).removeClass("disabled");
          plusOneVegetarianSelect.prop("disabled", false).removeClass("disabled");
        } else {
          plusOneNameInput.prop("disabled", true).addClass("disabled");
          plusOneVegetarianSelect.prop("disabled", true).addClass("disabled");
        }
  
        songSuggestionInput.prop("disabled", false).removeClass("disabled");
      } else {
        vegetarianSelect.prop("disabled", true).addClass("disabled");
        plusOneSelect.prop("disabled", true).addClass("disabled");
        plusOneNameInput.prop("disabled", true).addClass("disabled");
        plusOneVegetarianSelect.prop("disabled", true).addClass("disabled");
        songSuggestionInput.prop("disabled", true).addClass("disabled");
      }
    });
  
    // Enable or disable plus_one_name and plus_one_vegetarian based on plus_one value
    plusOneSelect.on("change", function() {
      if (attendingSelect.val() === "Yes" && plusOneSelect.val() === "Yes") {
        plusOneNameInput.prop("disabled", false).removeClass("disabled");
        plusOneVegetarianSelect.prop("disabled", false).removeClass("disabled");
      } else {
        plusOneNameInput.prop("disabled", true).addClass("disabled");
        plusOneVegetarianSelect.prop("disabled", true).addClass("disabled");
      }
    });
  });
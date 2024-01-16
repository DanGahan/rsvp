document.addEventListener("DOMContentLoaded", function() {
    // Target date for the countdown
    var targetDate = new Date("October 17, 2024").getTime();
  
    // Update the countdown every second
    setInterval(function() {
      // Get the current date and time
      var now = new Date().getTime();
  
      // Calculate the remaining time in milliseconds
      var remainingTime = targetDate - now;
  
      // Calculate the remaining days
      var days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
  
      // Update the content on the webpage
      var countdownElement = document.getElementById("countdown");
      countdownElement.textContent = days + " days until the big day";
    }, 1000);
  });
document.addEventListener("DOMContentLoaded", function() {
    // Target date for the countdown
    let targetDate = new Date("October 17, 2024").getTime();
  
    // Update the countdown every second
    setInterval(function() {
      // Get the current date and time
      let now = new Date().getTime();
  
      // Calculate the remaining time in milliseconds
      let remainingTime = targetDate - now;
  
      // Calculate the remaining days
      let days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
  
      // Update the content on the webpage
      let countdownElement = document.getElementById("countdown");
      countdownElement.textContent = days + " days until the big day";
    }, 1000);
  });
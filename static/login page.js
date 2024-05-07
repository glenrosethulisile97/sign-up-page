ocument.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login page").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Validate password
        var password = document.getElementById("password").value;
        if (!isValidPassword(password)) {
            alert("Password must be at least 8 characters long and contain at least one number, one letter, and one symbol.");
            return;
        }

        // If password is valid, proceed with sign up logic
        // Your sign up logic here
        alert("login successful!");
    });
});

function isValidPassword(password) {
    // Password must be at least 8 characters long
    if (password.length < 8) {
        return false;
    }
    // Password must contain at least one number, one letter, and one symbol
    var hasNumber = /\d/.test(password);
    var hasLetter = /[a-zA-Z]/.test(password);
    var hasSymbol = /[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]/.test(password);
    return hasNumber && hasLetter && hasSymbol;
}


function goToLandingPage1( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/Concept%20Design";
   }

   function goToLandingPage2( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/Material%20and%20Finish";
   }

   function goToLandingPage3( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/Styling%20and%20Decoration";
   }


   function goToLandingPage4( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/Renovation%20and%20Remodeling";
   }

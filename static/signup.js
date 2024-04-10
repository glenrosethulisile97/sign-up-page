document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        // Validate password
        var password = document.getElementById("password").value;
        if (!isValidPassword(password)) {
            alert("Password must be at least 8 characters long and contain at least one number, one letter, and one symbol.");
            return;
        }

        // If password is valid, proceed with sign up logic
        // Your sign up logic here
        alert("Sign up successful!");
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
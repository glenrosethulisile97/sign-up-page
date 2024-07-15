$(document).ready(function() {
    $('#signupForm').on('submit', function(event) {
        var isValid = true;

        // Validate username
        if ($('#username').val().trim() === '') {
            $('#username').addClass('is-invalid');
            isValid = false;
        } else {
            $('#username').removeClass('is-invalid');
        }

        // Validate email
        var email = $('#email').val().trim();
        var emailRegex = /^[\w.-]+@[\w.-]+\.\w+$/;
        if (email === '' || !emailRegex.test(email)) {
            $('#email').addClass('is-invalid');
            isValid = false;
        } else {
            $('#email').removeClass('is-invalid');
        }

        // Validate password
        if ($('#password').val().trim() === '') {
            $('#password').addClass('is-invalid');
            isValid = false;
        } else {
            $('#password').removeClass('is-invalid');
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});

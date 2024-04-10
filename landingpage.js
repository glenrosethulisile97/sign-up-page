<script>
    // JavaScript code to handle search functionality
    document.getElementById('search-form').addEventListener('submit', function(event) {
        event.preventDefault() // Prevent the form from submitting normally

        // Get the value entered in the search input
        var searchText = document.getElementById('search-input').value.toLowerCase();

        // Get the list of services
        var servicesList = document.querySelectorAll('#services ul li');

        // Loop through each service
        servicesList.forEach(function(service) {
            // Convert the service text to lowercase for case-insensitive comparison
            var serviceText = service.textContent.toLowerCase();

            // If the search text is found in the service text, display the service, otherwise hide it
            if (serviceText.includes(searchText)) {
                service.style.display = 'block';
            } else {
                service.style.display = 'none';
            }
        });
    });
</script>
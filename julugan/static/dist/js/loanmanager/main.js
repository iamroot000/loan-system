var approveButtons = document.querySelectorAll(".approve-loan-btn");

if (approveButtons.length === 1) {
    // If there is only one button, attach the click event listener directly to the button
    approveButtons[0].addEventListener("click", function() {
        var loanId = this.closest("tr").querySelector(".request-tbl-loan-id").textContent;
        var csrftoken = getCookie('csrftoken');
        // Log the loan id value to the console
        console.log(loanId);
        
        $.ajax({
            type: 'POST',
            url: 'approve-loan',
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
                'loanId': loanId,
            },
            success: function(response){
                // console.log(response);
                location.reload();
            }
        });
        
        return false;
    });
} else {
    // Loop through all the buttons and attach a click event listener to each
    approveButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Get the loan id value
            var loanId = this.parentNode.parentNode.querySelector(".request-tbl-loan-id").textContent;
            var csrftoken = getCookie('csrftoken');
            // Log the loan id value to the console
            console.log(loanId);
            
            $.ajax({
                type: 'POST',
                url: 'approve-loan',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'loanId': loanId,
                },
                success: function(response){
                    // console.log(response);
                    location.reload();
                }
            });
            
            return false;
        });
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
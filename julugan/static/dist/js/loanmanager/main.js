var approveLoanButtons = document.querySelectorAll(".approve-loan-btn");
var approvePaymentButtons = document.querySelectorAll(".approve-payment-btn");

if (approveLoanButtons.length === 1) {
    // If there is only one button, attach the click event listener directly to the button
    approveLoanButtons[0].addEventListener("click", function() {
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
    approveLoanButtons.forEach(function(button) {
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

if (approvePaymentButtons.length === 1) {
    // If there is only one button, attach the click event listener directly to the button
    approvePaymentButtons[0].addEventListener("click", function() {
        var paymentRequestNumber = this.closest("tr").querySelector(".payment-tbl-request-number").textContent;
        var csrftoken = getCookie('csrftoken');
        // Log the loan id value to the console
        console.log(paymentRequestNumber);
        
        $.ajax({
            type: 'POST',
            url: 'approve-payment',
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
                'paymentRequestNumber': paymentRequestNumber,
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
    approvePaymentButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Get the loan id value
            var paymentRequestNumber = this.parentNode.parentNode.querySelector(".payment-tbl-request-number").textContent;
            var csrftoken = getCookie('csrftoken');
            // Log the loan id value to the console
            console.log(paymentRequestNumber);
            
            $.ajax({
                type: 'POST',
                url: 'approve-payment',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'paymentRequestNumber': paymentRequestNumber,
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
// Get references to the loan amount and number of days elements
const loanAmountInput = document.getElementById('loanAmount');
const numberOfDaysSelect = document.getElementById('numberOfDays');
const loanWithPercent = document.getElementById("loanWithPercent");
const amountPerDay = document.getElementById("amountPerDay");

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


//make it dynamic where table can load inside modal to updaTE data in tables
var loanLinks = document.querySelectorAll('.loan-link');
loanLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // prevent the default link behavior
        var loanValue = this.getAttribute('data-value');
        console.log(loanValue); // replace this with your code to display the value
        var loanDetailsModalTitle = document.getElementById("loanDetailsModalTitle");
        var loan_details_borrower = document.getElementById("loan_details_borrower");
        var loan_details_amount_loan = document.getElementById("loan_details_amount_loan");
        var loan_details_start_date = document.getElementById("loan_details_start_date");
        var loan_details_due_date = document.getElementById("loan_details_due_date");
        var loan_details_total_days = document.getElementById("loan_details_total_days");
        var loan_details_amount_per_day = document.getElementById("loan_details_amount_per_day");
        var loan_details_progress = document.getElementById("loan_details_progress");
        var loan_details_amount_paid = document.getElementById("loan_details_amount_paid");
        var loan_details_amount_left = document.getElementById("loan_details_amount_left");
        var loan_details_paid_days = document.getElementById("loan_details_paid_days");
        var loan_details_days_left = document.getElementById("loan_details_days_left");
        var loan_details_total_profit = document.getElementById("loan_details_total_profit");
        var loan_details_payment_table = document.getElementById("loan_details_payment_table");
        loanDetailsModalTitle.textContent = "Loan ID: " + loanValue;
        $.ajax({
            type: 'GET',
            url: 'get-borrower-details/' + loanValue,
            success:  function(response){
                console.log(response)
                var var_payments_list = response.payments
                var var_details = response.details
                
                var_details.forEach(detail => {
                    var varAmountLeft = detail.amount_left;
                    var varAmountLoan = detail.amount_loan;
                    var varAmountPerDay = detail.amount_per_day;
                    var varDaysLeft = detail.days_left;
                    var varDueDate = detail.due_date;
                    var varLoanProfit = detail.loan_profit;
                    var varTataProfit = detail.tata_profit;
                    var varTotalProfit = varTataProfit + varLoanProfit;
                    var varName = detail.name;
                    var varPaidAmount = detail.paid_amount;
                    var varPaidDays = detail.paid_days;
                    var varProgress = detail.progress;
                    var varStartDate = detail.start_date;
                    var varTotalDays = detail.total_days;
                    
                    loan_details_amount_left.innerHTML = varAmountLeft;
                    loan_details_borrower.innerHTML = varName;
                    loan_details_amount_loan.innerHTML = varAmountLoan;
                    loan_details_start_date.innerHTML = varStartDate;
                    loan_details_due_date.innerHTML = varDueDate;
                    loan_details_total_days.innerHTML = varTotalDays;
                    loan_details_amount_per_day.innerHTML = varAmountPerDay;
                    loan_details_progress.innerHTML = "<div class='progress-bar bg-warning' role='progressbar' style='width: " + varProgress + "%' aria-valuenow='" + varProgress + "' aria-valuemin='0' aria-valuemax='100'></div>";
                    loan_details_amount_paid.innerHTML = varPaidAmount;
                    console.log(varPaidAmount);
                    loan_details_total_profit.innerHTML = varTotalProfit;
                    loan_details_paid_days.innerHTML = varPaidDays;
                    loan_details_days_left.innerHTML = varDaysLeft;
                    
                });
                    var_payments_list.forEach(element => {
                    
                        loan_details_payment_table.innerHTML += "<tr>"+
                        "<td>" + element.paid + "</td>"+
                        "<td>" + element.dates_to_pay + "</td>"+
                        "<td>" + element.paid_dates + "</td>"+
                        "</tr>"
                    });
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
                
            });
        });
    });
    
    // Add an event listener to the loan amount input field
    loanAmountInput.addEventListener('input', function() {
        const loanAmount = parseFloat(this.value);
        // Determine the options to display based on the loan amount
        let options;
        if (loanAmount === 500) {
            options = [27];
        } else if (loanAmount === 1000) {
            options = [27, 36];
        } else if (loanAmount === 1500) {
            options = [33];
        } else if (loanAmount === 2000) {
            options = [27];
        } else if (loanAmount === 3000) {
            options = [27];
        } else if (loanAmount === 5000) {
            options = [27, 36];
        } else {
            options = [];
        }
        
        // Update the options of the number of days select element
        numberOfDaysSelect.innerHTML = options.map(option => `<option>${option}</option>`).join('');
        //Update the loan percentage field value 10% of the total amount loan
        loanWithPercent.value = Number(this.value) * 0.1 + Number(this.value);
        //Update the field total of days to pay value depends on the set amount loan and days
        numberOfDaysSelect.selectedIndex = 0;
        
        varNumberOfDays = document.getElementById('numberOfDays');
        
        if (loanAmount === 500 && parseInt(varNumberOfDays.value) === 27) {
            amountPerDay.value = 20;
        } else if (loanAmount === 1000 && parseInt(varNumberOfDays.value) === 27) {
            amountPerDay.value = 40;
        } else if (loanAmount === 1000 && parseInt(varNumberOfDays.value) === 36) {
            amountPerDay.value = 30;
        } else if (loanAmount === 1500 && parseInt(varNumberOfDays.value) === 33) {
            amountPerDay.value = 50;
        } else if (loanAmount === 2000 && parseInt(varNumberOfDays.value) === 27) {
            amountPerDay.value = 80;
        } else if (loanAmount === 3000 && parseInt(varNumberOfDays.value) === 27) {
            amountPerDay.value = 120;
        } else if (loanAmount === 5000 && parseInt(varNumberOfDays.value) === 27) {
            amountPerDay.value = 200;
        } else if (loanAmount === 5000 && parseInt(varNumberOfDays.value) === 36) {
            amountPerDay.value = 150;
        } else {
            amountPerDay.value = 0;
        }
    });
    
    numberOfDaysSelect.addEventListener('change', function() {
        const loanAmount = parseFloat(loanAmountInput.value);
        const numberOfDays = parseFloat(this.value);
        
        // Update amountPerDay based on the selected loanAmount and numberOfDays
        if (loanAmount === 500 && numberOfDays === 27) {
            amountPerDay.value = 20;
        } else if (loanAmount === 1000 && numberOfDays === 27) {
            amountPerDay.value = 40;
        } else if (loanAmount === 1000 && numberOfDays === 36) {
            amountPerDay.value = 30;
        } else if (loanAmount === 1500 && numberOfDays === 33) {
            amountPerDay.value = 50;
        } else if (loanAmount === 2000 && numberOfDays === 27) {
            amountPerDay.value = 80;
        } else if (loanAmount === 3000 && numberOfDays === 27) {
            amountPerDay.value = 120;
        } else if (loanAmount === 5000 && numberOfDays === 27) {
            amountPerDay.value = 200;
        } else if (loanAmount === 5000 && numberOfDays === 36) {
            amountPerDay.value = 150;
        } else {
            amountPerDay.value = 0;
        }
    });
    
    // Get the submit button element
    const submitAddLoan = document.getElementById('submitAddLoan');
    
    // Add event listener to the submit button
    submitAddLoan.addEventListener('click', function() {
        // Retrieve the values of the input fields
        const borrowerName = document.getElementById('borrowerName').value;
        const loanAmount = document.getElementById('loanAmount').value;
        const paymentMethod = document.getElementById('paymentMethod').checked;
        const numberOfDays = document.getElementById('numberOfDays').value;
        const amountPerDay = document.getElementById('amountPerDay').value;
        const loanWithPercent = document.getElementById('loanWithPercent').value;
        var csrftoken = getCookie('csrftoken');
        
        // Log the values to the console
        console.log(borrowerName);
        console.log(loanAmount);
        console.log(paymentMethod);
        
        $.ajax({
            type: 'POST',
            url: 'add-loan',
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
                'borrowerName': borrowerName,
                'loanAmount': loanAmount,
                'paymentMethod': paymentMethod,
                'numberOfDays': numberOfDays,
                'amountPerDay': amountPerDay,
                'loanWithPercent': loanWithPercent,
            },
            success: function(response){
                location.reload();
            }
        });
        
    });
    
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
    
    numberOfDaysSelect.style.color = 'black';
    
    
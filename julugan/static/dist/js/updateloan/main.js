// Get references to the loan amount and number of days elements
const loanAmountInput = document.getElementById('loanAmount');
const numberOfDaysSelect = document.getElementById('numberOfDays');
const loanWithPercent = document.getElementById("loanWithPercent");
const amountPerDay = document.getElementById("amountPerDay");
const updatePayment = document.getElementById("updatePayment");

const const_payment_col_1 = document.getElementById("payment_col_1");
for (let i = 1; i < 13; i++) {
    const_payment_col_1.innerHTML +=
    "<div class='custom-control custom-checkbox' id='paymentCheckBox"+i+"' hidden>" +
    "<input type='checkbox' class='custom-control-input' name='optionsRadios' id='optionsRadios"+i+"' value=''>" +
    "<label for='optionsRadios"+i+"' class='custom-control-label' id='optionsRadiosLabel"+i+"'></label>"+
    "</div>";
}

const const_payment_col_2 = document.getElementById("payment_col_2");
for (let i = 13; i < 25; i++) {
    const_payment_col_2.innerHTML +=
    "<div class='custom-control custom-checkbox' id='paymentCheckBox"+i+"' hidden>" +
    "<input type='checkbox' class='custom-control-input' name='optionsRadios' id='optionsRadios"+i+"' value=''>" +
    "<label for='optionsRadios"+i+"' class='custom-control-label' id='optionsRadiosLabel"+i+"'></label>"+
    "</div>";
}

const const_payment_col_3 = document.getElementById("payment_col_3");
for (let i = 25; i < 37; i++) {
    const_payment_col_3.innerHTML +=
    "<div class='custom-control custom-checkbox' id='paymentCheckBox"+i+"' hidden>" +
    "<input type='checkbox' class='custom-control-input' name='optionsRadios' id='optionsRadios"+i+"' value=''>" +
    "<label for='optionsRadios"+i+"' class='custom-control-label' id='optionsRadiosLabel"+i+"'></label>"+
    "</div>";
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
                    var varStaffProfit = detail.staff_profit;
                    var varTotalProfit = varStaffProfit + varLoanProfit;
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
                var counter_payment = 1;
                var_payments_list.forEach(element => {
                    var var_options_radios = document.getElementById("optionsRadios" + counter_payment);
                    // var_options_radios_label.insertAdjacentElement("afterend", "test");
                    var var_payment_check_box = document.getElementById("paymentCheckBox"+counter_payment);
                    console.log(element)
                    // console.log(element.dates_to_pay);
                    var_payment_check_box.hidden=false;
                    var_options_radios.value = element.dates_to_pay;
                    // var var_options_radios_label = document.getElementById("optionsRadios" + counter_payment).parentNode;
                    var var_options_radios_label = document.getElementById("optionsRadiosLabel" + counter_payment);
                    if(element.paid_dates===null){
                        var_options_radios_label.innerHTML = element.dates_to_pay + "<span class='text-info' style='margin: 3px'>(NONE)</span>";                
                    }else{
                        var_options_radios_label.innerHTML = element.dates_to_pay + "<span class='text-primary' style='margin: 3px'>" + element.paid_dates + "</span>";
                        var_options_radios.checked=true;
                        var_options_radios.disabled=true;
                    }
                    counter_payment++;
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
const submitLoanRequest = document.getElementById('submitAddLoan');

// Add event listener to the submit button
submitLoanRequest.addEventListener('click', function() {
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

updatePayment.addEventListener('click', function(){
    const checkboxes = document.querySelectorAll('[name="optionsRadios"]');
    var checkedBoxes = [];
    var loan_details_borrower = document.getElementById("loan_details_borrower");
    var loan_details_amount_per_day = document.getElementById("loan_details_amount_per_day");
    const loanId = document.querySelector('#loanDetailsModalTitle').textContent.split(': ')[1];
    var borrower = loan_details_borrower.innerHTML;
    var amountPerDay = loan_details_amount_per_day.innerHTML;
    var csrftoken = getCookie('csrftoken');
    
    for (let i = 0; i < checkboxes.length; i++) {
        const checkbox = checkboxes[i];
        
        if (checkbox.checked && !checkbox.disabled){
            checkedBoxes.push(checkbox.value);
        }
    }
    console.log(amountPerDay);
    console.log(borrower);
    console.log(loanId);
    console.log(checkedBoxes);
    $.ajax({
        type: 'POST',
        url: 'submit-payment-request',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify({
            'borrower': borrower,
            'loan_id': loanId,
            'list_of_paid_dates': checkedBoxes,
            'amount_per_day': amountPerDay,
        }),
        success: function(response){
            location.reload();
            // console.log(response)
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
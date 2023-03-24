var dailyTableContent = document.getElementById('daily-table-content')

$.ajax({
    type: 'GET',
    url: 'get-daily-table',
    success:  function(response){
        console.log(response)
        data = response.data
        console.log(data)
        data.forEach(element => {

            var varPaidAmount = element.paidAmount;
            var varAmountLoan = element.amountLoan;
            var varProgress = ( varPaidAmount / varAmountLoan ) * 100;

            dailyTableContent.innerHTML += "<tr>"+
            "<td>" + element.name + "</td>"+
            "<td>" + element.amountLeft + "</td>"+
            "<td>"+
            "<div class='progress'>"+
            "<div class='progress-bar bg-warning' role='progressbar' style='width: " + varProgress + "%' aria-valuenow='" + varProgress + "' aria-valuemin='0' aria-valuemax='100'></div>"+
            "</div>"+
            "</td>"+
            "<td>" + element.amountLoan + "</td>"+
            "<td>" + element.dueDate + "</td>"+
            "</tr>"
        });
    }

});
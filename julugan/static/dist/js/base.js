const profilebtn =  document.getElementById("profile-btn");


profilebtn.addEventListener('click', function(event) {
    event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: '/user-profile',
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(response){
            console.log(response.total_profit);
            console.log(response.balance_profit);
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
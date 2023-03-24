function login(){
  
  var varUsername = document.getElementById("username").value
  var varPassword = document.getElementById("password").value
  var csrftoken = getCookie('csrftoken');
  
  $.ajax({
    type: 'POST',
    url: '',
    headers: {
      'X-CSRFToken': csrftoken
    },
    data: {'username': varUsername,
    'password': varPassword,
  },
  success: function(response){
    window.location.href='/dashboard/';
  }
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
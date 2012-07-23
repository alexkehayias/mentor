$ ->
    $(".signup").on "click", (e) ->
        e.preventDefault()
        $("#signupDialog").reveal()
    $("#signupForm").on "submit", (e) ->
        e.preventDefault()
        email = $("#email").val()
        password = $("#password").val()
        alert_box = $ "#signupAlert"
        if not email
            alert_box.html "You must enter your email"
            alert_box.show()            
            return
        if password.length <= 6
            alert_box.html "You must enter a password longer than 6 char"
            alert_box.show()
            return
        $.post '/signup/',
            email: email
            password: password
            (response) ->
                window.location = "/profile/edit/"

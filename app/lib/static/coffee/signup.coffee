$ ->
    $(".signup").on "click", (e) ->
        e.preventDefault()
        $("#signupDialog").reveal()
    $("#signupForm").on "submit", (e) ->
        e.preventDefault()
        p2pu_id = $("#p2pu_id").val()
        password = $("#password").val()
        alert_box = $ "#signupAlert"
        if not p2pu_id
            alert_box.html "You must enter your username"
            alert_box.show()            
            return
        if password.length <= 6
            alert_box.html "You must enter your password"
            alert_box.show()
            return
        $.ajax
            url: '/signup/'
            data:
                p2pu_id: p2pu_id
                password: password
            type: "POST"
            dataType: "json"
            success: (response) ->
                window.location = "/profile/edit/"
            error: (e) =>
                alert_box.html e.responseText
                alert_box.show()
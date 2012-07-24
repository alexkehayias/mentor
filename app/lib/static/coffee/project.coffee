$ ->
    $(".connect").on "click", (e) ->
        e.preventDefault()
        modal = $ "#connectModal"
        modal.reveal()

    $("#connectModal>.accept").on "click", (e) ->
        # Ajax post to the server to create a new Mentorship instance
        e.preventDefault()
        target = $ e.currentTarget
        note = $("#note").val()
        if note
            $("#connectModal").trigger "reveal:close"
            $.post window.href, 
                note: note
                (response) ->
                    console.log response
        else
            $("#alert").html("You must add a message").show()

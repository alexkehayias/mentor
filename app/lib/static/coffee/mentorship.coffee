$ ->
    $(".connect").on "click", (e) ->
        e.preventDefault()
        user_id = e.currentTarget.getAttribute "data-user-id"
        skill_id = e.currentTarget.getAttribute "data-skill-id"
        mentorship_request_id = e.currentTarget.getAttribute "data-mentorship-request-id"
        modal = $ "#connectModal"
        modal_headline = $ "#connectModal>h2"
        modal_button = $ "#connectModal>.button"
        modal_headline.html "Connect with " + e.name
        modal_button.attr "name", user_id
        modal_button.attr "data-skill-id", skill_id
        modal_button.attr "data-mentorship-request-id", mentorship_request_id
        modal.reveal()

    $("#connectModal>.accept").on "click", (e) ->
        # Ajax post to the server to create a new Mentorship instance
        e.preventDefault()
        target = $ e.currentTarget
        $("#connectModal").trigger "reveal:close"
        $.post "/mentorship-requests/", 
            user_id: target.attr "name"
            skill_id: target.attr "data-skill-id"
            mentorship_request_id: target.attr "data-mentorship-request-id"
            (response) ->

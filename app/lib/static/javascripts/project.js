(function() {

  $(function() {
    $(".connect").on("click", function(e) {
      var modal;
      e.preventDefault();
      modal = $("#connectModal");
      return modal.reveal();
    });
    return $("#connectModal>.accept").on("click", function(e) {
      var note, target;
      e.preventDefault();
      target = $(e.currentTarget);
      note = $("#note").val();
      if (note) {
        $("#connectModal").trigger("reveal:close");
        return $.post(window.href, {
          note: note
        }, function(response) {
          return console.log(response);
        });
      } else {
        return $("#alert").html("You must add a message").show();
      }
    });
  });

}).call(this);

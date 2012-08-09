(function() {

  $(function() {
    $(".signup").on("click", function(e) {
      e.preventDefault();
      return $("#signupDialog").reveal();
    });
    return $("#signupForm").on("submit", function(e) {
      var alert_box, loading, p2pu_id, password,
        _this = this;
      e.preventDefault();
      loading = $("#loading");
      loading.show();
      p2pu_id = $("#p2pu_id").val();
      password = $("#password").val();
      alert_box = $("#signupAlert");
      if (!p2pu_id) {
        alert_box.html("You must enter your username");
        alert_box.show();
        loading.hide();
        return;
      }
      if (password.length <= 6) {
        alert_box.html("You must enter your password");
        alert_box.show();
        loading.hide();
        return;
      }
      return $.ajax({
        url: '/signup/',
        data: {
          p2pu_id: p2pu_id,
          password: password
        },
        type: "POST",
        dataType: "json",
        success: function(response) {
          return window.location = "/profile/edit/";
        },
        error: function(e) {
          alert_box.html(e.responseText);
          alert_box.show();
          return loading.hide();
        }
      });
    });
  });

}).call(this);

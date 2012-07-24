(function() {

  $(function() {
    $(".signup").on("click", function(e) {
      e.preventDefault();
      return $("#signupDialog").reveal();
    });
    return $("#signupForm").on("submit", function(e) {
      var alert_box, email, password;
      e.preventDefault();
      email = $("#email").val();
      password = $("#password").val();
      alert_box = $("#signupAlert");
      if (!email) {
        alert_box.html("You must enter your email");
        alert_box.show();
        return;
      }
      if (password.length <= 6) {
        alert_box.html("You must enter a password longer than 6 char");
        alert_box.show();
        return;
      }
      return $.post('/signup/', {
        email: email,
        password: password
      }, function(response) {
        return window.location = "/profile/edit/";
      });
    });
  });

}).call(this);

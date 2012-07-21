(function() {
  var __indexOf = Array.prototype.indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  $(function() {
    return $(".accept, .reject").on("click", function(e) {
      var state;
      if (__indexOf.call(e.currentTarget.classList, "accept") >= 0) {
        state = "accept";
      } else {
        state = "reject";
      }
      return $.post(window.href, {
        request_id: e.currentTarget.name,
        state: state
      }, function(response) {
        return console.log(response);
      });
    });
  });

}).call(this);

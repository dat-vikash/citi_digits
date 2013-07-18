/**
 * User: vikashdat
 * Date: 7/17/13
 * Time: 10:20 PM
 */

/*
  Handle Sign Up, Login, Logout
 */
 $(".membership").click(function(ev) {
        ev.preventDefault(); // prevent navigation
        var url = $(this).data("form"); // get the contact form url
        $("#signUpModal").load(url, function() { // load the url into the modal
            $(this).modal('show').css({
                  width: '900px',
                  'margin-left': function () {
            return -($(this).width() / 2);
        }
    }); // display the modal on url load
        });
        return false; // prevent the click propagation
    });

//    $('.contact-form').live('submit', function() {
//        $.ajax({
//            type: $(this).attr('method'),
//            url: this.action,
//            data: $(this).serialize(),
//            context: this,
//            success: function(data, status) {
//                $('#contactModal').html(data);
//            }
//        });
//        return false;
//    });
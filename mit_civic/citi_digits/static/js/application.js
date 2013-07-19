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

/*
 * Sign Up workflow logic
 */
$("#signUpModal").on("click", ".workflow_1_click", function (ev) {
    ev.preventDefault(); // prevent navigation
    //hide sign up workflow part 1
    $("#signUpModal #workflow_1").hide();
    $("#signUpModal .workflow_1_click").hide();
    //show workflow 2
    $("#signUpModal #workflow_2").show();
    $("#signUpModal .workflow_2_add_team").show();
});

$('#signUpModal').on("click", ".add_student", function (ev) {
    ev.preventDefault(); // prevent navigation
    //get team name
    var teamName = $(this).closest("div").find("#team_name").val();
    if(!teamName){
        teamName = "Team";
    }

    //get student count
//    $("div").attr('id').replace(/button/, '')
    var student_count = $(this).closest(".team").find(".student").length + 1;
//    console.log($(this).closest("div").find("#team_name").val());
    var studentFirstNameInput = '<input class="input-medium student" type="text" placeholder="Student First Name" name="teams[' +
        teamName+'][' + student_count +'][name]">';
    var studentPassword = '<input class="input-medium" type="text" placeholder="Password" name="teams[' +
        teamName+'][' + student_count +'][password]">';
    $(this).parent().parent().parent().prepend('<tr><td>' + studentFirstNameInput + '</td><td>' + studentPassword +'</td></tr>');
});

/*
 * This function defines how to handle adding a new team group to the screen
 */
$('#signUpModal').on("click", ".add_team", function (ev) {
    ev.preventDefault(); // prevent navigation
    $('#workflow_2').append('<div class="team">' +
              '<div class="input-append">' +
                '<input class="input-large" type="text" placeholder="Team" id="team_name_1">' +
                '<span class="add-on"><span class="caret"></span></span>' +
              '</div>'+
              '<table>'+
                  '<tr>' +
                      '<td colspan="2">' +
                          '<label class="add_student">+ Add a student to this team</label>' +
                      '</td>' +
                  '</tr>' +
              '</table>' +
          '</div><!-- team -->')
    //prevent click propagation
    return false;
});



//$('#myTable tr:last').after('<tr>...</tr><tr>...</tr>');
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
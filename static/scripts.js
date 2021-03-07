var element = document.querySelector(".door");
element.addEventListener("click", toggleDoor);

function toggleDoor() {
  element.classList.toggle("doorOpen");
}
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//      $(document).ready(function(){
//
//        $('#searchbar').focus();
//
//        $('#donate-buttons').on('click', '.btn-blue', function(e) {
//          e.preventDefault();
//          $('.active').removeClass('active');
//          $('#other-input').hide().siblings('#other').show();
//          $(this).filter('.btn-blue').addClass("active");
//          var value = $(this).data('impact');
//          $(this).closest('div').find('p').text("" + value);
//          $('#other-input').find('input').val('');
//        });
//
//        $('.btn-green').on('click', function() {
//          var dollar;
//          var input = $('#other-input').find('input').val();
//          if ( !input ) {
//            dollar = $('.active').data('dollars');
//           } else if ( $.trim(input) === '' || isNaN(input)) {
//            // empty space leaves value = 'undefined'.
//            // Have to fix $.trim(input) == '' above so that it works.
//            console.log('Yes');
//            dollar = "Please enter a number.";
//          } else {
//            dollar = input;
//          }
//          $('#price').text(""+dollar);
//        });
//
//        $('#other').on('click', function(e) {
//          e.preventDefault();
//          var buttons = $(this).parent('#donate-buttons');
//          buttons.find('.active').removeClass('active');
//          var other = $(this).hide().siblings('#other-input');
//          other.show();
//          other.find('input').focus();
//          var pText = buttons.siblings('p');
//          pText.text("Thank you!");
//          var oValue = other.find('input');
//          oValue.keyup(function() {
//            if ( oValue.val() > 50 ) {
//              pText.text("Thank you!" + " You\'re donation covers housing and counseling services for " + oValue.val()/25 + " people.");
//            } else {
//              pText.text("Thank you!");
//            }
//          });
//        });
//
//      });
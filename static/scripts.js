var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
   console.log("modal click:" + donation);
  document.getElementById("price").innerHTML = donation;
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

// For donation buttons
// Get the button that opens the modal
var donation = 0;
var donation5 = document.getElementById("fiveDollars");
var donation10 = document.getElementById("tenDollars");
var donation25 = document.getElementById("twentyfiveDollars");

donation5.onclick = function() {
 donation10.style.backgroundColor = "#58C0ED";
    donation25.style.backgroundColor = "#58C0ED";
    donation5.style.backgroundColor = "#00739C";
    donation = 5;
};

donation10.onclick = function() {
    donation5.style.backgroundColor = "#58C0ED";
    donation25.style.backgroundColor = "#58C0ED";
    donation10.style.backgroundColor = "#00739C";
    donation = 10;
};

donation25.onclick = function() {
 donation5.style.backgroundColor = "#58C0ED";
    donation10.style.backgroundColor = "#58C0ED";
    donation25.style.backgroundColor = "#00739C";
    donation = 25;
};





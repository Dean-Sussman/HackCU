var element = document.querySelector(".door");
element.addEventListener("click", toggleDoor);

var tt = document.getElementById("tt");
var impactNum = document.getElementById("impact");
var egg1 = document.getElementById("eggs1");
var egg2 = document.getElementById("eggs2");
var egg3 = document.getElementById("eggs3");
var egg4 = document.getElementById("eggs4");
var egg5 = document.getElementById("eggs5");
var egg6 = document.getElementById("eggs6");
var egg7 = document.getElementById("eggs7");
var egg8 = document.getElementById("eggs8")

var clicks = 0;

function toggleDoor() {
  clicks++;
  element.classList.toggle("doorOpen");
  if (clicks %2 == 1) { //when door is opened
    tt.style.display = "none";
    if (impactEggs > 7) {
     egg1.style.display = "block";
     egg2.style.display = "block";
     egg3.style.display = "block";
     egg4.style.display = "block";
     egg5.style.display = "block";
     egg6.style.display = "block";
     egg7.style.display = "block";
     egg8.style.display = "block";
    } else if(impactEggs > 2) {
     egg1.style.display = "block";
     egg2.style.display = "block";
     egg3.style.display = "block";
    } else if(impactEggs > 0) {
      egg1.style.display = "block";
    }
  } else {
  setTimeout(function(){
    tt.style.display = "block";
    egg1.style.display = "none";
     egg2.style.display = "none";
     egg3.style.display = "none";
     egg4.style.display = "none";
     egg5.style.display = "none";
     egg6.style.display = "none";
     egg7.style.display = "none";
     egg8.style.display = "none";
}, 500);

  }
}
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
var impactEggs = 0;

btn.onclick = function() {
  modal.style.display = "block";
  console.log("modal click:" + donation);
  document.getElementById("price").innerHTML = donation;
  impactEggs = Math.floor(donation / 3);
 document.getElementById("impact").innerHTML = impactEggs;
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





var modal;

function openMod(which) {
	if (which == "in") {
		var form = document.getElementById("form");
		var action = form.setAttribute("action", "/LogIn");
		
		var h2 = document.getElementById("sign");
		h2.innerHTML = "Sign In";
		
		var button = document.getElementById("form");
		button.innerHTML = "Sign In";
	} else {
		var form = document.getElementById("form");
		var action = form.setAttribute("action", "/signUp");
		
		var h2 = document.getElementById("sign");
		h2.innerHTML = "Sign Up";
		
		var button = document.getElementById("form");
		button.innerHTML = "Sign Up";
	}
	modal = document.getElementById("myModal");
	modal.style.display = "block";
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

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
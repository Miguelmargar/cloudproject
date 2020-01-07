var modal;

function createEve() {
	modal = document.getElementById('creMod');
	modal.style.display='block';
}

function getOldDetails(eve) {
	modal = document.getElementById('edMod');
	modal.style.display='block';
	
	document.getElementById('ed_event').value = eve;
	
	document.getElementById('edName').value = eve[0];
	document.getElementById('edDate').value = eve[1];
	document.getElementById('edDesc').value = eve[2];
}

function shareWithDetails(eve) {
	modal = document.getElementById('shaMod');
	modal.style.display='block';
	
	document.getElementById('sha_event').value = eve;
}

function showArch() {
	document.getElementById("archform").submit()
}


function openMod(which) {
	if (which == "in") {
		var form = document.getElementById("form");
		form.setAttribute("action", "/logIn");
		
		var h2 = document.getElementById("sign");
		h2.innerHTML = "Log In";
		
		var button = document.getElementById("formbut");
		button.innerHTML = "Log In";
		
		var inName = document.getElementById("modU");
		inName.setAttribute("name", "logName");
		
		var inPass = document.getElementById("modP");
		inPass.setAttribute("name", "logPass");
		
	} else {
		var form = document.getElementById("form");
		form.setAttribute("action", "/signUp");
		
		var h2 = document.getElementById("sign");
		h2.innerHTML = "Sign Up";
		
		var button = document.getElementById("formbut");
		button.innerHTML = "Sign Up";
		
		var inName = document.getElementById("modU");
		inName.setAttribute("name", "signName");
		
		var inPass = document.getElementById("modP");
		inPass.setAttribute("name", "signPass");
	}
	var check = document.getElementById("form").getAttribute("value");
	modal = document.getElementById("myModal");
	modal.style.display = "block";
}

//Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var creClsBt = document.getElementById("creClsBt");
var edClsBt = document.getElementById("edClsBt");
var shClsBt = document.getElementById("shClsBt");

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

creClsBt.onclick = function() {
	modal.style.display = "none";
}

edClsBt.onclick = function() {
	modal.style.display = "none";
}

shClsBt.onclick = function() {
	modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$('#radAll').click(function() {
	$('#time').slideUp(500);
	$('#time').val('');
	  
})

$('#radSpe').click(function() {
	  $('#time').slideDown(500);
	  $('#time').val('00:00');
})


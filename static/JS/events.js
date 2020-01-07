var modal;

function createEve() {
	document.getElementById('modal').style.display='block';
	document.getElementById('moded').style.display='none';
	document.getElementById('share').style.display='none';
}

function getOldDetails(eve) {
	document.getElementById('share').style.display='none';
	document.getElementById('modal').style.display='none';
	document.getElementById('moded').style.display='block';

	document.getElementById('ed_event').value = eve;
	
	document.getElementById('edName').value = eve[0];
	document.getElementById('edDate').value = eve[1];
	document.getElementById('edDesc').value = eve[2];
}

function shareWithDetails(eve) {
	document.getElementById('share').style.display='block';
	document.getElementById('modal').style.display='none';
	document.getElementById('moded').style.display='none';
	
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
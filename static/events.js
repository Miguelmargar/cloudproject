var name;
var date;
var description;


function creEv() {
	document.getElementById("modal").style.display="none";
		
	name = document.getElementById("Name").value,
	date = document.getElementById("Date").value,
	description = document.getElementById("Desc").value
	
	$.getJSON($SCRIPT_ROOT + '/createEvent', {
		name,
		date,
		description
	 },
     function(response) {
     });
	
}
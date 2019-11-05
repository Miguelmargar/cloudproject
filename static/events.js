var name;
var date;
var description;
var editNum;


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

function delEv(num) {
	$.getJSON($SCRIPT_ROOT + '/deleteEvent', {
		num
	 },
     function(response) {
     });
}


function editEv(num) {
	document.getElementById('moded').style.display='block';
	editNum = num;
}

function edFrontEv() {
	
}
var name;
var date;
var description;
var ed_num;


function creEv() {
	document.getElementById("modal").style.display="none";
		
	name = document.getElementById("Name").value;
	date = document.getElementById("Date").value;
	description = document.getElementById("Desc").value;
	
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
	ed_num = num;
}

function edFrontEv() {
	ed_name = document.getElementById("edName").value;
	ed_date = document.getElementById("edDate").value;
	ed_description = document.getElementById("edDesc").value;
	
	$.getJSON($SCRIPT_ROOT + '/editEvent', {
		ed_num,
		ed_name,
		ed_date,
		ed_description
	 },
     function(response) {
     });
}
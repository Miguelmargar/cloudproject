var name;
var date;
var description;
var ed_num;
var frontSearch;

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
	window.location.reload();
}

function delEv(num) {
	$.getJSON($SCRIPT_ROOT + '/deleteEvent', {
		num
	 },
     function(response) {
     });
	window.location.reload();
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
	window.location.reload();
}


function search() {
	sear = document.getElementById("search").value;
	$.getJSON($SCRIPT_ROOT + '/searchEvent', {
		sear
	 },
     function(response) {
     });
	window.location.reload();
}

var name;
var date;
var description;
var ed_num;
var ed_num_sear;
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
	alert("Event Deleted");
}

function delEvSear(num) {
	$.getJSON($SCRIPT_ROOT + '/deleteEventSearch', {
		num
	 },
     function(response) {
     });
	window.location.reload();
	alert("Event Deleted");
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
	alert("Event changed");
}

function editEvSear(num) {
	document.getElementById('modese').style.display='block';
	ed_num_sear = num;
}

function edSearEv() {
	ed_se_na = document.getElementById("edSeNa").value;
	ed_se_da = document.getElementById("edSeDa").value;
	ed_se_des = document.getElementById("edSeDe").value;
	
	$.getJSON($SCRIPT_ROOT + '/editSeEvent', {
		ed_num_sear,
		ed_se_na,
		ed_se_da,
		ed_se_des
	 },
     function(response) {
     });
	window.location.reload();
	alert("Event changed");
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

function archEv(num) {
	$.getJSON($SCRIPT_ROOT + '/archiveEvent', {
		num
	 },
     function(response) {
     });
	window.location.reload();
	alert("Event archived");
}

function arEvSear(num) {
	$.getJSON($SCRIPT_ROOT + '/archSeEvent', {
		num
	 },
     function(response) {
     });
	window.location.reload();
	alert("Event archived");
}

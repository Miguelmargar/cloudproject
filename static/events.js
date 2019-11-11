function getOldDetails(eve) {
	document.getElementById('moded').style.display='block';
	old_name = eve["name"];
	old_date = eve["date"];
	old_desc = eve["desc"];
	
	$.getJSON($SCRIPT_ROOT + '/get_old_details', {
		old_name,
		old_date,
		old_desc
	 },
    function(response) {
    });	
}

function shareWithDetails(eve) {
	document.getElementById('share').style.display='block';
	sha_na = eve["name"];
	sha_da = eve["date"];
	sha_desc = eve["desc"];

	$.getJSON($SCRIPT_ROOT + '/get_sha_det', {
		sha_na,
		sha_da,
		sha_desc
	 },
    function(response) {
    });
}
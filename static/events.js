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
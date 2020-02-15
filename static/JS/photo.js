$("#myFile").change(function(e) {
	var fileName = e.target.files[0].name;
	var fileExt = fileName.slice(-3);
	
	if (fileExt == "jpg" || fileExt == "png") {
		var file = $("#myFile")[0].files[0];
		var reader = new FileReader();

		reader.onload = function (e) {
			$('.currImg img').attr('src', e.target.result);
			$('.currImg img').css('border-radius', '100%');
			$('#imgYes').slideDown('slow');
		};
		reader.readAsDataURL(file);
	} else {
		alert("File extension not accepted - jpg and png file needed.")
	}
})



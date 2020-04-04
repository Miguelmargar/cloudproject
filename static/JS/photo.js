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

// check for image in user's main screen if it's not the default leave as is otherwise round corners
var mainImgSrc = $(".nav img").attr('src');
if (mainImgSrc != "../static/assets/userDefault.png") {
	$(".nav img").css('border-radius', '100%');
} else {
	$(".nav img").css('border-radius', '0%');
}

// check for image inside modal if it's not the default leave as is otherwise round corners
var imgSrc = $(".currImg img").attr('src');
if (imgSrc != "../static/assets/userDefault.png") {
	$(".currImg img").css('border-radius', '100%');
}
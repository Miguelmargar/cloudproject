$("#myFile").change(function() {
	var file = $("#myFile")[0].files[0];
	var reader = new FileReader();

	reader.onload = function (e) {
    	$('.currImg img')
        	.attr('src', e.target.result)
            };
            reader.readAsDataURL(file);
	
})
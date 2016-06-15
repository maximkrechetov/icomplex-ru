var landing = {
	init: function(){
		var $phoneInputs = $('input.lp-input_data_phone')
		$phoneInputs.inputmask('+79999999999');
	}
}

$(document).ready(function(){
    landing.init();
});
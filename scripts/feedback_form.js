var feedbackForm = {
    init: function(){
        var $fileInput = $('#id_file');
        $('#id_phone').inputmask('+79999999999');
        $('.feedback__add-files').click(function(){
            $fileInput.click();
        });

        $(':file').change(function () {
            $('.files__selected_count').text(this.files.length);
        });

    }
};

$(document).ready(function(){
    feedbackForm.init();
});
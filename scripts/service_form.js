var ServiceFeedback = {
    $form: $('#service_feedback'),

    close_form: function() {
        $('.form-layout').hide();
        window.location = location.origin + location.pathname;
    },

    open_form: function() {
        $('.form-layout').show();
        $('title').html(addition_page_title);
    },

    send_feedback: function() {
        var data = {
            name: $('input[name="name"]').val(),
            phone: $('input[name="phone"]').val(),
            email: $('input[name="email"]').val(),
            service_url: $('input[name="service_url"]').val()
            };

        $('.form-block__body__item__error').html('');

        $.ajax({
            url: ServiceFeedback.$form.attr('data-url'),
            type: 'POST',
            data: data,
            success: function(response) {
                alert('Письмо успешно отправлено.');
                ServiceFeedback.close_form();
            },
            error: function(response) {
                var errors = response.responseJSON;
                if (errors) {
                    for (var name in errors) {
                        var msg = errors[name][0];
                        ServiceFeedback.$form.find('.'+ name + ' .error').html(msg);
                    }
                }
            }
        })
    },

    init: function() {
        var me = this;
        $('#open_form').bind('click', me.open_form);
        $('#send_feedback').bind('click', me.send_feedback);
        $('html').bind('click', function() {
            if (me.$form.is(':visible')) me.close_form()
        });
        $('#close_form').bind('click', me.close_form);
        $('#open_form, #service_feedback').bind('click', function(event){event.stopPropagation()});
        $('input[name="service_url"]').val(window.location.href);
    }

};

ServiceFeedback.init();
/*jslint unparam: true */
/*global window, $ */
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$(function () {
    'use strict';
    // Change this to the location of your server-side upload handler:
    var url = '/';
    var csrftoken = $.cookie('csrftoken');
    $('#id_image').fileupload({
        url: url,
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }

            $('.upload-icon').removeClass('fa-cloud-upload').addClass('fa-refresh fa-spin');
        },
        dataType: 'json',
        done: function (e, data) {
            // window.location = data.result.url;
        }
    }).prop('disabled', !$.support.fileInput)
        .parent().addClass($.support.fileInput ? undefined : 'disabled');
});

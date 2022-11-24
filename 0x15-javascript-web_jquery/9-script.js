$(function () {
    $.get('https://fourtonfish.com/hellosalut/' + $('html').attr('lang'), function (data) {
        $('div#hello').text(data.hello);
    });
});

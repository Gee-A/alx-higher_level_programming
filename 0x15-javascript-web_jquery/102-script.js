$(addEventListener('DOMContentLoaded', function () {
    $('INPUT').eq(1).click(function () {
        const lang = $('INPUT').eq(0).val();
        $.get('https://fourtonfish.com/hellosalut/' + $('html').attr('lang'), function (data) {
            $('div#hello').text(data.hello);
        });
    });
}));

addEventListener('DOMContentLoaded', function () {
    $('input#language_code').keypress(function (event) {
        let code = event.keycode || event.which;
        if (code === 13) {
            const lang = $('input#language_code').val();
            $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
                $('div#hello').text(data.hello);
            });
        }
    });
    $('input#bin_translate').click(function () {
        const lang = $('input#language_code').vall();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
            $('div#hello').text(data.hello);
        });
    });
});

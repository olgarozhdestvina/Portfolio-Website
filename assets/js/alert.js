/* Alert timeout
Aparted from https://stackoverflow.com/questions/50365291/auto-closing-bootstrap-alerts-after-form-submission */

window.setTimeout(function () {
    $(".alert").fadeTo(2000, 10000).slideUp(5000, function () {
        $(this).hide();
    }); 10000
});
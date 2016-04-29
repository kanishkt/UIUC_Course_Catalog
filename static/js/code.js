/**
 * Created by kanishk on 4/26/16.
 */
$('.ui-autocomplete').addClass('f-dropdown');

function submitDetailsForm() {
    event.preventDefault();
    $input = $('#tags').val();
    location.href = "/"+$input;
    closeSearch();
}
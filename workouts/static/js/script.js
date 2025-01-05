document.addEventListener('DOMContentLoaded', function() {
    //sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialisation
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Confirm"}
     });

     // is urgent initialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);


    //modal intialisation
        //var elems = document.querySelectorAll('.modal');
        //var instances = M.Modal.init(elems, options);
});
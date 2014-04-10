
var Wine = {

};

Wine.Initialize = function() {

	Wine.backdrop = new Wine.Maps.BackdropMap("map-element");

    $('.form_datetime').datetimepicker({
        //language:  'fr',
        weekStart: 1,
        todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		forceParse: 0,
        showMeridian: 1,
        minuteStep: 30
    });

}

Wine.Maps = {

};

Wine.Maps.BackdropMap = function( element ) {

	var map;
	function initialize() {
	  var mapOptions = {
	    zoom: 8,
	    center: new google.maps.LatLng(-34.397, 150.644),
	    
	    panControl: false,
	    streetViewControl: false,
	    mapTypeControl: false,
	    scrollwheel: false,
	    zoomControl: false,
	    draggable: false

	  };
	  map = new google.maps.Map(document.getElementById(element),
	      mapOptions);
	}

	google.maps.event.addDomListener(window, 'load', initialize);

}
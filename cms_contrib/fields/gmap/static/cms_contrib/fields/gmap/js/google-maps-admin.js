django.jQuery(function($){
	
	$.fn.cms_contrib_gmap_widget = function(options){
		var defaults = {	
			'zoom':8,	
			'lat':'53.311',
			'lng':'-6.24',
			'map_elem' : '#id_map',
			'delete_elem' : '#id_delete',
		};
		
		var options = $.extend(defaults, options);
		var value = null;
		var marker = null;
		var map = null;
		var latlng = null;
		var that = this;
		
		var set_field = function(latlng){
		    if(marker){
		        $(that).val(latlng.lat()+","+latlng.lng());
    		}
		};
		
		var get_field = function(){
		    if($(that).val()){
    			return $(that).val().split(",");
    		}else{
    			return "";
    		}
		};
		
		var remove_field = function(){
		    if(marker!==""){
    			$(that).removeAttr("value");
    		}
		};
		
		var remove_marker = function(){
		    marker.setMap(null);
    		marker = null;
		};
		
		var set_marker = function(latlng){
		    if(!marker){
		        marker = new google.maps.Marker({
    				map:map,
    				draggable:true,
    				position: latlng,
    			});
    			google.maps.event.addListener(marker, 'click', function(new_location) {
    			    map.setZoom(13);
    				map.setCenter(new_location.latLng);
    			});
    			google.maps.event.addListener(marker, 'dragend', function(new_location) {
    				set_field(new_location.latLng);
    			});
    		}else{
    		    marker.setPosition(latlng)
    		}
		};	
		
		latlng = new google.maps.LatLng(options.lat,options.lng);
        map = new google.maps.Map(document.getElementById($(options.map_elem).attr('id')),{
			zoom: options.zoom,
			center : latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
		});
		// If there is a value in the field, load it onto the map
		if(get_field()!==""){
			set_marker(new google.maps.LatLng(get_field()[0],get_field()[1]));
		}
		/* Listeners */
		google.maps.event.addListener(map, 'rightclick', function(new_location) {
		    set_marker(new_location.latLng);
			set_field(new_location.latLng);
		});
		$(options.delete_elem).click(function(){
			if(marker!==""){
				remove_marker();
				remove_field();
			}
		});
		
	};
});
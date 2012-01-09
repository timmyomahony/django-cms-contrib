from django.conf import settings
from django.forms import widgets
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
import settings as gmap_settings

class GoogleMapsWidget(widgets.HiddenInput):
    
	class Media:
		js = [
			'http://maps.google.com/maps/api/js?sensor=false',
			'cms_contrib/fields/gmap/js/google-maps-admin.js',
	        ]

	def render(self, name, value, attrs=None):
		if value is None:
			value = ""
		final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
		if value != "":
			final_attrs['value'] = force_unicode(self._format_value(value))
		html = u"""
					<input%(attrs)s />
					<div class="map_canvas_wrapper" style="display:inline-block;">
						<div id="%(map_id)s" style="width:%(width)spx;height:%(height)spx"></div>
						<script>
							django.jQuery(function($) {
							    $("#%(field_id)s").cms_contrib_gmap_widget({
    								'zoom': %(zoom)s,
    							    'lat': '%(center_lat)s',
    							    'lng': '%(center_lng)s',
    							    'map_elem': '#%(map_id)s',
    							    'delete_elem' : '#%(delete_id)s',
    							});
							});
						</script>
					</div>
					<p><a id="%(delete_id)s" href="javascript:void(0)">Remove Marker</a></p>
					<p class="help">Double click to zoom in and center on a location. Right click to set the marker on  a position. You can also drag and drop the marker</p>
				""" % { 
				        'field_id' : attrs['id'],
				        'delete_id' : 'map_delete_%s'%attrs['id'],
				        'map_id' : 'map_%s'%attrs['id'],
						'attrs' : flatatt(final_attrs),
						'height': gmap_settings.HEIGHT,
						'width':  gmap_settings.WIDTH,
						'zoom' : gmap_settings.ZOOM,
						'center_lng' : gmap_settings.DEFAULT_LNG,
						'center_lat' : gmap_settings.DEFAULT_LAT,
					}
		return mark_safe(html)
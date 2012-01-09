from django import forms
from django.template import Context, Template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.forms.util import flatatt
from django.forms import widgets

from cms_contrib import settings

class MediaMixin(object):
	pass
	
	class Media:
		# These will only be imported if an existing django.jquery and jquery UI is not found 
		css = {
			'screen':(
				settings.JQUERY_UI_CSS_URL,
				'cms_contrib/admin/widgets/slider/css/slider.css',
			),}
		js = (settings.JQUERY_UI_JS_URL,)
	
class SliderWidget(widgets.HiddenInput, MediaMixin):

	def __init__(self, min=0, max=100, min_label=None, max_label=None, unit=None, classname="admin_slider", *args,  **kwargs):
		self.min = min
		self.max = max
		self.min_label = min_label
		self.max_label = max_label
		self.unit = unit
		self.classname = classname
		super(SliderWidget, self).__init__(*args, **kwargs)
		
	def render(self, name, value, attrs=None):
		"""
		Figures out whether it is a widget for a textarea or for an input. 
		"""
		if value is None:
			value = 0
		final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
		if value != '':
			final_attrs['value'] = force_unicode(self._format_value(value))
		html = u"""
			<div class="{{ classname }}_wrapper">
				<div class="{{ classname }}" id="{{ slider_id }}"></div>
				<div class="{{ classname }}_value">
					<span class="value">{{ value }}</span>
					{% if unit %}
					<span class="unit">{{ unit }}</span>
					{% endif %}
				</div>
				<div class="{{ classname }}_details">
					<div class="min">{{ min }} {% if min_label %}({{ min_label }}){% endif %}</div>
					<div class="max">{{ max }} {% if max_label %}({{ max_label }}){% endif %}</div>
				</div>
			</div>			
			{{ original }}
			<script type="text/javascript">
				(function($){
					$('#{{ slider_id }}').slider({
						min : {{ min }},
						max : {{ max }},
						slide: function(event, ui) {
							$('#{{ input_id }}').val(ui.value);
							$('.{{ classname }}_value span.value').text(ui.value);
						},
						value: {{ value }},
					});
				})(jQuery)
			</script>
		"""
		return Template(html).render(Context({
            'classname' : self.classname, 
			'original' : super(SliderWidget, self).render(name, value, attrs),
			'min' : self.min, 
			'max' : self.max,
			'min_label' : self.min_label, 
			'max_label' : self.max_label, 
			'unit' : self.unit, 
			'slider_id' : "slider_%s" % final_attrs.get('id', ''),
			'input_id' : final_attrs.get('id', ''),
			'value' : value,
        }))
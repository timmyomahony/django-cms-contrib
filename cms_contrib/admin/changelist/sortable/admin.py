from django.contrib import admin

from cms_contrib import settings

class SortableChangeListAdmin(admin.ModelAdmin):
	
	def __init__(self, *args, **kwargs):
		if not self.list_editable:
			self.list_editable = ()
		self.list_editable = self.list_editable + ('ordering', )
		if not self.list_display:
			self.list_display = ()
		self.list_display = self.list_display + ('ordering', )		
		super(SortableChangeListAdmin, self).__init__(*args, **kwargs)
		
	class Media:
		js = [	settings.JQUERY_JS_URL,
				settings.JQUERY_UI_JS_URL,
				'cms_contrib/admin/changelist/sortable/js/sortable_changelist.js']
		css = { 'all':(settings.JQUERY_UI_CSS_URL,) }
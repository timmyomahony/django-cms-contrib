from django.conf import settings

JQUERY_JS_URL = getattr(settings, 'CMS_CONTRIB_JQUERY_JS_URL', 'cms_contrib/js/jquery.min.js')
JQUERY_UI_JS_URL = getattr(settings, 'CMS_CONTRIB_JQUERY_UI_JS_URL', 'cms_contrib/js/jquery.ui.min.js')
JQUERY_UI_CSS_URL = getattr(settings, 'CMS_CONTRIB_JQUERY_UI_CSS_URL', 'cms_contrib/css/jquery.ui.css')
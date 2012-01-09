from django.conf import settings

WIDTH = getattr(settings, 'GMAP_WIDTH', 500)
HEIGHT = getattr(settings, 'GMAP_HEIGHT', 300)
ZOOM = getattr(settings, 'GMAP_ZOOM', 8)
DEFAULT_LAT = getattr(settings, 'GMAP_DEFAULT_LAT', 53.311)
DEFAULT_LNG = getattr(settings, 'GMAP_DEFAULT_LAT', -6.24)
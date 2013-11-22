import os

from django_assets import Bundle, register
from django.conf import settings


_JS_ASSETS = ('js/jquery.js',)
JS_ASSETS = (
    'bootstrap/js/bootstrap.js',
    'js/jquery-ui-1.8.18.custom.min.js'
    'js/select2.min.js',
    'js/main.js',
)
if settings.DEBUG:
    JS_ASSETS = _JS_ASSETS + JS_ASSETS


CSS_ASSETS = (
    'bootstrap/css/bootstrap.css',
    'bootstrap/css/bootstrap-responsive.css',
    'css/bootstrap-ui/jquery-ui-1.8.16.custom.css',
    'css/select2/select2.css',
    'css/main.css',
)

js = Bundle(*JS_ASSETS, filters='jsmin', output='packed.js')
css = Bundle(*CSS_ASSETS, filters='cssmin', output='packed.css')

register('js', js)
register('css', css)

from django.conf import settings

def paths(request):
    return {
        'media_dir': settings.MEDIA_URL,
        'css_dir': settings.MEDIA_URL + 'css',
        'img_dir': settings.MEDIA_URL + 'images',
        'js_dir': settings.MEDIA_URL  + 'js',
        'plugin_dir': settings.MEDIA_URL + 'plugins',
        'DEBUG': settings.DEBUG,
    }


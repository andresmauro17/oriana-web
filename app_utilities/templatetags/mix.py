from django import template
from django.conf import settings
import json

register = template.Library()

@register.filter
def mix(value):
    static_base_dir = settings.STATICFILES_BASE_DIR
    env_name = 'prod' if not settings.DEBUG else 'dev'
    static_dir = static_base_dir / env_name 
    fd = open(static_dir/"manifest.json", "r")
    manifest = json.load(fd)
    if(value in manifest):
        return str(env_name)+'/'+manifest[value]["file"]
    else:
        return ""
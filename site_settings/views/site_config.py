"""site_settings > views > site_config.py"""
# IMPORTS PYTHON
import logging
# DJANGO IMPORTS

# APP IMPORTS
from site_settings.models import SiteSettings

logger = logging.getLogger(__name__)


def site_info(request):
    host = request.get_host()
    try:
        site = SiteSettings.objects.get(
            domain=host, is_active=True
        )
    except Exception as e:
        logger.warning(e)
        site = SiteSettings.objects.create(
            domain=host,
            name="'*****Please update the object in the Site Settings model*****'", # noqa
            short_name="'*****Please update the object in the Site Settings model*****'", # noqa
            is_active=True
        )
    context = {
        'site': site
    }
    return context

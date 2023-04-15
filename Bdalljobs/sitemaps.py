from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from jobs.models import JobsPost


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'http'

    def items(self):
        return [
            'index',
            'jobs:search',
        ]

    def location(self, item):
        return reverse(item)


class JobsPostSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return JobsPost.objects.all()

    def lastmod(self, obj):
        return obj.published_date

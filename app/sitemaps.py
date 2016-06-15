from __future__ import absolute_import

from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from .models import Service


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        defined = [{'name': x,
                    'args': []} for x in ['about', 'contacts', 'feedback-page', 'vacancies-list', 'service_list']]

        services = [{'name': 'service',
                     'args': [url, ]} for url in Service.objects.all().values_list('url', flat=True)]

        return defined + services

    def location(self, item):
        return reverse(item['name'], args=item['args'])

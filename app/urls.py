from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap
from .views import (IndexPageView, VacancyListView, FeedbackFormView, ServiceDetail, ServiceList,
                    ContactsView,  AboutView, ServiceFeedbackFormView, LandingView)

sitemaps = {
    'static': StaticViewSitemap,
}

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexPageView.as_view(), name='home'),
    url(r'^vacancies/$', cache_page(0)(VacancyListView.as_view()), name='vacancies-list'),
    url(r'^feedback/$', cache_page(0)(FeedbackFormView.as_view()), name='feedback-page'),
    url(r'^price/$', cache_page(0)(ServiceList.as_view()), name='service_list'),
    url(r'^price/(?P<url>[-_!0-9a-zA-Z]{1,200})/$', cache_page(0)(ServiceDetail.as_view()), name='service'),
    url(r'^contacts/$', cache_page(0)(ContactsView.as_view()), name='contacts'),
    url(r'^about/$', cache_page(0)(AboutView.as_view()), name='about'),
    url(r'^landing/$', cache_page(0)(LandingView.as_view()), name='landing'),

    url(r'^service_feedback_form/$', ServiceFeedbackFormView.as_view(), name='service_form'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),
)

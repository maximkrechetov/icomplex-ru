# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
from random import shuffle
from django.conf import settings

from django.views.generic import ListView, TemplateView, DetailView, base, CreateView
from django.views.generic.edit import FormView
from django.utils.translation import ugettext as _
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Vacancy, Service, PageBlock, PhoneContact, EmailContact, Slide, FeedbackMessage, FeedbackMessageFile, ServiceFeedback, MainPageService

from .forms import FeedbackForm, ServiceFeedbackForm, LandingForm
from .handlers import handle_uploaded_file


class ContactsMixinView(base.ContextMixin):
    page_name = None

    def get_context_data(self, **kwargs):
        context = super(ContactsMixinView, self).get_context_data(**kwargs)
        context['phone_contacts'] = PhoneContact.objects.filter(pages=self.page_name)
        context['email_contacts'] = EmailContact.objects.filter(pages=self.page_name)
        return context


class IndexPageView(TemplateView):
    def get_template_names(self):
        return [_('index page')]

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['blocks'] = [p.code for p in PageBlock.objects.filter(show=True).only('code')]
        context['vacancies'] = Vacancy.objects.filter(actual=True).only('url', 'job_title')
        context['services'] = MainPageService.objects.filter(active=True)
        slides = list(Slide.objects.filter(show=True).only('out_url', 'banner_url'))
        shuffle(slides)
        context['slides'] = slides
        return context


class VacancyListView(ListView, ContactsMixinView):
    model = Vacancy
    template_name = 'vacancies_list.html'
    page_name = PhoneContact.pages.vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(actual=True).only('job_title',
                                                                        'job_conditions',
                                                                        'requirements',
                                                                        'job_functions')
        return context


class FeedbackFormView(FormView):
    template_name = 'feedback_page.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
        new_feedback_message = FeedbackMessage.create_feedback(self.request.POST)
        if new_feedback_message:
            files = self.request.FILES.getlist('file', [])
            for f in files:
                handled = handle_uploaded_file(f)
                if handled.get('created'):
                    FeedbackMessageFile.create_feedback_message_file(new_feedback_message, handled.get('file_name'))

            context = {'message': u'Письмо успешно отправлено',
                       'form': form,
                       'redirect_url': self.request.META.get('HTTP_REFERER', '/')}

            return self.render_to_response(self.get_context_data(**context))

        return super(FeedbackFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FeedbackFormView, self).get_context_data(**kwargs)
        if self.request.GET:
            reason = self.request.GET.get('reason', 5)
            if reason == 1:
                context['page_title'] = u'Напишите нам'
            context['form'] = FeedbackForm({'reason': reason})
        return context


class ServiceList(ListView, ContactsMixinView):
    template_name = 'service_list.html'
    queryset = Service.objects.filter(parent__isnull=True, show=True)
    page_name = PhoneContact.pages.service


class ServiceDetail(DetailView, ContactsMixinView):
    template_name = 'service.html'
    model = Service
    slug_field = 'url'
    slug_url_kwarg = slug_field
    page_name = PhoneContact.pages.service

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super(ServiceDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        return context


class ContactsView(TemplateView, ContactsMixinView):
    template_name = 'contacts.html'
    page_name = PhoneContact.pages.contacts


class AboutView(TemplateView):
    template_name = 'about.html'


class ServiceFeedbackFormView(CreateView):
    form_class = ServiceFeedbackForm
    model = ServiceFeedback
    http_method_names = ['post']

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        return self.render_to_json_response(form.errors, status=400)

    def form_valid(self, form):
        super(ServiceFeedbackFormView, self).form_valid(form)
        return self.render_to_json_response({'ok': True})


class LandingView(FormView):
    template_name = 'landing.html'
    form_class = LandingForm
    success_url = '/'

    def form_valid(self, form):
        new_feedback_message = FeedbackMessage.create_feedback(self.request.POST)
        if new_feedback_message:
            print 'here'
            context = {'message': u'Мы приняли вашу заявку. В сокором времени с вами свяжется наш менеджер',
                'form': form,
                'redirect_url': self.request.META.get('HTTP_REFERER', '/')}
            return self.render_to_response(self.get_context_data(**context))
        return super(LandingView, self).form_valid(form)
        pass

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        slides = list(Slide.objects.filter(show=True).only('out_url', 'banner_url'))
        shuffle(slides)
        context['slides'] = slides
        return context
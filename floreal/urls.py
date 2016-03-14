#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
    url(r'^$', views.active_deliveries, name='index'),
    url(r'^edit/dv-(?P<delivery>[^/]+)$', views.edit_delivery, name='edit_delivery'),
    url(r'^network-admin/nw-(?P<network>[^/]+)$', views.network_admin, name='network_admin'),

    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^accounts/register$', views.user_register, name="user_register"),
    url(r'^accounts/registration_post.html$', views.user_register_post, name="registration_post"),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^create-delivery/nw-(?P<network>[^/]+)$', views.create_delivery, name='create_delivery'),
    url(r'^delivery-state/dv-(?P<delivery>[^/]+)/(?P<state>[A-Za-z]+)$', views.set_delivery_state, name='set_delivery_state'),
    url(r'^subgroup-state/dv-(?P<delivery>[^/]+)/sg-(?P<subgroup>[^/]+)/(?P<state>[^/]+)$', views.set_subgroup_state_for_delivery, name='set_subgroup_state_for_delivery'),

    url(r'^adjust/dv-(?P<delivery>[^/]+)$', views.adjust_subgroup, name='adjust_subgroup'),
    url(r'^adjust/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+)$', views.adjust_subgroup, name='adjust_subgroup'),
    url(r'^edit-products/dv-(?P<delivery>[^/]+)$', views.edit_delivery_products, name='edit_delivery_products'),
    url(r'^edit-membership/nw-(?P<network>[^./]+)$', views.edit_user_memberships, name='edit_user_memberships'),
    url(r'^edit-membership/nw-(?P<network>[^./]+).json$', views.json_memberships, name='json_memberships'),
    url(r'^edit-purchases/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+)$', views.edit_subgroup_purchases, name='edit_subgroup_purchases'),
    url(r'^edit-purchases/dv-(?P<delivery>[^/]+)$', views.edit_user_purchases, name='edit_user_purchases'),

    url(r'^edit-candidacy/cd-(?P<candidacy>[^/]+)$', views.candidacy, name='candidacy'),
    url(r'^set-candidacy/cd-(?P<candidacy>[^/]+)/(?P<response>[YN])$', views.apply_candidacy, name='apply_candidacy'),
    url(r'^validate-candidacy/cd-(?P<candidacy>[^/]+)/(?P<response>[YM])$', views.validate_candidacy, name='validate_candidacy'),

    url(r'^view/dv-(?P<delivery>[^/]+).html$', views.view_purchases_html, name='view_all_purchases_html'),
    url(r'^view/dv-(?P<delivery>[^/]+)/table.pdf$', views.view_purchases_latex, name='view_all_purchases_latex'),
    url(r'^view/dv-(?P<delivery>[^/]+)/cards.pdf$', views.view_cards_latex, name='view_all_cards_latex'),
    url(r'^view/dv-(?P<delivery>[^/]+).xlsx$', views.view_purchases_xlsx, name='view_all_purchases_xlsx'),
    url(r'^view/dv-(?P<delivery>[^/]+).html$', views.view_purchases_html, name='view_all_purchases_html'),
    url(r'^view/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+).html$', views.view_purchases_html, name='view_subgroup_purchases_html'),
    url(r'^view/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+).xlsx$', views.view_purchases_xlsx, name='view_subgroup_purchases_xlsx'),
    url(r'^view/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+)/table.pdf$', views.view_purchases_latex, name='view_subgroup_purchases_latex'),
    url(r'^view/sg-(?P<subgroup>[^/]+)/dv-(?P<delivery>[^/]+)/cards.pdf$', views.view_cards_latex, name='view_subgroup_cards_latex'),
    url(r'^emails/nw-(?P<network>[^/]+)$', views.view_emails, name='emails_network'),
    url(r'^emails/sg-(?P<subgroup>[^/]+)$', views.view_emails, name='emails_subgroup'),
    url(r'^history$', views.view_history, name='view_history'),

    url(r'^charte.html$', TemplateView.as_view(template_name='charte.html'), name='charte'),

)

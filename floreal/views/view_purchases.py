#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from ..models import Delivery, Subgroup
from . import latex
from .spreadsheet import spreadsheet
from .delivery_description import delivery_description


def get_subgroup(request, network):
    if 'subgroup' in request.GET:
        return Subgroup.objects.get(network=network, name__iexact=request.GET['subgroup'])
    else:
        return network.subgroup_set.get(staff__in=[request.user])


def _non_html_response(name_bits, name_extension, mime_type, content):
    """Common helper to serve PDF and Excel content."""
    filename = ("_".join(name_bits) + "." + name_extension).replace(" ", "_")
    response = HttpResponse(content_type=mime_type)
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    response.write(content)
    return response


@login_required()
def view_purchases_html(request, delivery, subgroup=None):
    """View all purchases for a given delivery. Network staff only."""
    delivery = Delivery.objects.get(id=delivery)
    subgroups = [Subgroup.objects.get(id=subgroup)] if subgroup else delivery.network.subgroup_set.all()
    return render_to_response('view_purchases.html', delivery_description(delivery, subgroups))


@login_required()
def view_purchases_xlsx(request, delivery, subgroup=None):
    """View all purchases for a given delivery in an MS-Excel spreadsheet. Network staff only."""
    delivery = Delivery.objects.get(id=delivery)
    subgroups = [Subgroup.objects.get(id=subgroup)] if subgroup else delivery.network.subgroup_set.all()
    return _non_html_response((delivery.network.name, delivery.name), "xlsx",
                              "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                              spreadsheet(delivery, subgroups))


@login_required()
def view_purchases_pdf(request, delivery, subgroup=None):
    """View the purchases of each subgroup as an Adobe PDF file."""
    delivery = Delivery.objects.get(id=delivery)
    if subgroup:
        subgroup = Subgroup.objects.get(id=subgroup)
        content = pdf.subgroup(delivery, subgroup)
        name_bits = (delivery.network.name, delivery.name, subgroup.name)
    else:
        content = pdf.all(delivery)
        name_bits = (delivery.name, subgroup.name)
    return _non_html_response(name_bits, "pdf", "application/pdf",content)


@login_required()
def view_purchases_latex(request, delivery, subgroup=None):
    """View the purchases of each subgroup as an Adobe PDF file."""
    delivery = Delivery.objects.get(id=delivery)
    if subgroup:
        subgroup = Subgroup.objects.get(id=subgroup)
        content = latex.subgroup(delivery, subgroup)
        name_bits = (delivery.network.name, delivery.name, subgroup.name)
    else:
        content = latex.delivery_table(delivery)
        name_bits = (delivery.network.name, delivery.name)
    return _non_html_response(name_bits, "pdf", "application/pdf", content)


@login_required()
def view_cards_latex(request, delivery, subgroup=None):
    """View the purchases of a subgroup as an Adobe PDF file. Subgroup staff only."""
    delivery = Delivery.objects.get(id=delivery)
    if subgroup:
        subgroup = Subgroup.objects.get(id=subgroup)
        content = latex.cards(delivery, subgroup)
        name_bits = (delivery.network.name, delivery.name, subgroup.name)
    else:
        content = latex.delivery_cards(delivery)
        name_bits = (delivery.network.name, delivery.name)
    return _non_html_response(name_bits, "pdf", "application/pdf", content)

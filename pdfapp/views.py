from django.shortcuts import render

import os, sys;
from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


def pdf(request):
    return render(request, 'pdf.html')

def render_to_pdf(template_src,context_dic={}):
    template=get_template(template_src)
    html=template.render(context_dic)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("utf-8")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None

def pdf_create(requests):
    pdf = render_to_pdf('pdf.html')
    if pdf:
        response=HttpResponse(pdf,content_type="applications/pdf")
        content="inline; filename=contact.pdf"
        response['Content-Disposition']=content
        return response
    return HttpResponse("not Found")
from django.shortcuts import render, render_to_response

def index_view(request):
    context = {"email_number": 21}
    return render_to_response(template_name="djstarter.html", context=context)
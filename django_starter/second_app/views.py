from django.shortcuts import render_to_response

__author__ = 'travisknop'

def index_view(request):
    context = {"name": "Travis Knop", "age": 31}
    return render_to_response(template_name="travis_first_django.html", context=context)
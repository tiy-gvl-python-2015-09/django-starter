from django.shortcuts import render, render_to_response


# Create your views here.


def index_view(request):
    return render_to_response(template_name="cool_stuff.html")
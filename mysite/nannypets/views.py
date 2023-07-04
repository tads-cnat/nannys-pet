from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render (request, 'nannypets/index.html')



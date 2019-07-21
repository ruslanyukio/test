from django.shortcuts import render
from django.views.generic import TemplateView


class Page(TemplateView):
	def get(self, request, **kwargs):
		return render(request, "page.html", {"hi": "hi"})

	def post(self, request, **kwargs):

		pass


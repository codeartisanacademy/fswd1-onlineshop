from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name= 'home.html'

    def get(self, request):
        counter = 0
        if 'counter_session' in request.session:
            counter = request.session['counter_session'] + 1
            request.session['counter_session'] = counter
        else:
            request.session['counter_session'] = counter

        return render(request, self.template_name, {'counter':counter})


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        if 'counter_session' in request.session:
            counter = request.session['counter_session']

        return render(request, self.template_name, {'counter':counter})
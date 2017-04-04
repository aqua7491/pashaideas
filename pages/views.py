from django.shortcuts import render
from django.views.generic import View, FormView, CreateView, DetailView
from newsletter.forms import JoinForm
from .models import Page
from django.contrib.messages.views import SuccessMessageMixin
# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})


class HomeView(SuccessMessageMixin, CreateView):
    template_name = "pages/home.html"
    form_class = JoinForm
    success_url = '/'

    def get_success_message(self, cleaned_data):
        return "Thank you for joining!"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['object'] = Page.objects.filter(featured=True).first()
        return context
    # def form_valid(self, form):
    #     email = form.cleaned_data.get("email")
    #     return super(HomeView, self).form_valid(form)


class PageDetailView(DetailView):
    queryset = Page.objects.filter(active=True)
    model = Page
    template_name = 'pages/home.html'

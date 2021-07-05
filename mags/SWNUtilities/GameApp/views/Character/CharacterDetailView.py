from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from GameApp.models import Character


class CharacterDetail(DetailView):
    model = Character
    template_name = "detail_template.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'fragment_character_detail.html'
        return context

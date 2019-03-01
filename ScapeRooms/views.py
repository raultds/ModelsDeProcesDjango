from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from ScapeRooms.models import ScapeRoom


class ScapeRoomDetail(DetailView):
    model = ScapeRoom
    template_name = 'scapeRoom/scapeRoom_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ScapeRoomDetail, self).get_context_data(**kwargs)
        context['RATING CHOICES'] = ScapeRoomDetail.RATING_CHOICES


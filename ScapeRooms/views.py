from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from ScapeRooms.models import ScapeRoom, Opinion, Reservation

def homePage(request):
    context = None
    return render(request, 'ScapeRooms/home.html', context)

class ScapeRoomDetail(DetailView):
    model = ScapeRoom
    template_name = 'scapeRoom/scapeRoom_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ScapeRoomDetail, self).get_context_data(**kwargs)
        context['RATING CHOICES'] = ScapeRoomDetail.RATING_CHOICES
        return context


class ScapeRoomCreate(CreateView):
    model = ScapeRoom
    template_name = 'scapeRoom/scapeRoom_detail.html'
    form_class = Opinion

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ScapeRoomCreate, self).form_valid(form)


def opinion(request, pk):
    scaperoom = get_object_or_404(ScapeRoom, pk=pk)
    review = Opinion(
        comment=request.POST['Comment'],
        user=request.user,
        scaperoom=scaperoom)
    review.save()
    return HttpResponseRedirect(reverse('ScapeRoom:scapeRoom_detail'))


def reservation(request, pk):
    scaperoom = get_object_or_404(ScapeRoom, pk=pk)
    review = Reservation(
        date=request.POST['DATE'],
        user=request.user,
        scaperoom=scaperoom)
    review.save()
    return HttpResponseRedirect(reverse('ScapeRoom:scapeRoom_detail'))

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
        return context


class ScapeRoomCreate(CreateView):
    model = ScapeRoom
    template_name = 'scapeRoom/scapeRoom_detail.html'
    form_class = ScapeRoomForm

    def form_valid(self,form):
        from.instance.user = self.request.user
        return super(ScapeRoomCreate,self).form_valid(form)

def opinion(request,pk):
    scaperoom = get_object_or_404(ScapeRoom,pk=pk)
    review = ScapeRoomReview(
        rating = request.POST['Rating'],
        comment = request.POST['Comment'],
        user = request.user,
        scaperoom = scaperoom)
    review.save()
    return HTTPResponseRedirect(reverse('ScapeRoom:scapeRoom_detail'))

def reservation(request,pk):
    scaperoom = get_object_or_404(ScapeRoom,pk=pk)
    review = ScapeRoomReview(
        rating = request.POST['Rating'],
        comment = request.POST['Comment'],
        user = request.user,
        scaperoom = scaperoom)
    review.save()
    return HTTPResponseRedirect(reverse('ScapeRoom:scapeRoom_detail'))
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from ScapeRooms.models import ScapeRoom, Opinion, Reservation, CustomUser


def homePage(request):
    context = None
    return render(request, 'ScapeRooms/home.html', context)


def scapeRoomList(request):
    context = {
        'title': 'ScapeRoom List',
        'llista': ScapeRoom.objects.all(),
    }
    return render(request, 'ScapeRooms/ScapeRooms_list.html', context)


def scapeRoomPage(request, pk):
    opinions = []
    room = get_object_or_404(ScapeRoom, pk=pk)
    for object in Opinion.objects.filter(pk=room.id):
        opinions.append(object)
    context = {
        'room': room,
        'title': room.name,
        'opinions': opinions,
    }
    return render(request, 'ScapeRooms/ScapeRoom_detail.html', context)


def opinion(request, pk):
    # model = Opinion
    # review = Opinion(
    #     comment=request.POST['Comment'],
    #     user=request.user,
    #     scaperoom=ScapeRoom)
    # review.save()

    opinion = get_object_or_404(Opinion, pk=pk)

    user = get_object_or_404(User, pk=opinion.userID_id)

    context = {
        'opinion': opinion,
        'user': user.id,
    }
    return render(request, 'ScapeRooms/opinion.html', context)



# def reservation(request, pk):
#     scaperoom = get_object_or_404(ScapeRoom, pk=pk)
#     review = Reservation(
#         date=request.POST['DATE'],
#         user=request.user,
#         scaperoom=scaperoom)
#     review.save()
#     return HttpResponseRedirect(reverse('ScapeRoom:scapeRoom_detail'))

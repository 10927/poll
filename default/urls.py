from django.urls import path
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    #path('poll/', poll_list),
    path('', RedirectView.as_view(url='poll/')),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),
    path('vote/<int:oid>/',PollVote.as_view()),
    path('poll/create/', PollCreate.as_view()),
    path('poll/<int:pk>/update/', PollUpdate.as_view()),
    path('poll/<int:pk>/delete/', PollDelete.as_view()),
    path('option/create/<int:pid>/', OptionCreate.as_view()),
    path('option/<int:pk>/update/', OptionUpdate.as_view()),
    path('option/<int:pk>/delete/', OptionDelete.as_view()),
]
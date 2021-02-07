from django.urls import path
from Twit_app.views import *

urlpatterns = [
    path('msg/', Messages.as_view()),
    path('dial/', Dialogue.as_view())
]

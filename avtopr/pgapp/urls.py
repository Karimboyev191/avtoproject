from django.urls import path
from pgapp.views import *

urlpatterns=[

    path('xizmatlar/',XizmatView.as_view(),name='hizmatl'),

    path('xizdetail/<a>/',XizDetailView.as_view(),name='xizdetail')
]



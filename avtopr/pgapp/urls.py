from django.urls import path
from pgapp.views import *

urlpatterns=[

    path('xizmatlar/',XizmatView.as_view(),name='hizmatl'),
    path('aloqa/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about'),
    path('xizdetail/<a>/',XizDetailView.as_view(),name='xizdetail')
]



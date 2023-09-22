from django.urls import path

from school.views import students_list
import debug_toolbar
from django.urls import path, include


urlpatterns = [
    path('', students_list, name='students'),
    peth('__debug__/', include(debug_toolbar.urls)),
]

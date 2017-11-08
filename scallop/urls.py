
from django.conf.urls import url
from . import apply
urlpatterns = [
    url(r'^activityapply/', apply.activity_apply),
]

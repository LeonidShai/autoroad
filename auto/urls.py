from django.urls import path
from auto.views import *

urlpatterns = [
    path('', IndexView.as_view(), name=""),
    path('about/', AboutView.as_view(), name="about"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog-single/', BlogSingleView.as_view(), name="blog-single"),
    path('car/', CarView.as_view(), name="car"),
    path('car-single/', CarSingleView.as_view(), name="car-single"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('pricing/', PricingView.as_view(), name="pricing"),
]

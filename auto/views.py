from django.shortcuts import render
from django.views.generic import View
from .setting.base import *
from django.http import HttpResponse
import json
from .models import *

# Create your views here.


class IndexView(View):
    def get(self, request):

        mash = [
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-1.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-2.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-3.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-4.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-5.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-6.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-7.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
            {
                'title': 'Mercedez-Benz C217',
                'company': 'Mercedez-Benz',
                'img': 'images/car-8.jpg',
                'price': 10.99,
                'when_day': '/day'
            },
        ]

        if not request.is_ajax():
            return render(request, 'auto/index.html',
                          {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                           'email_address': EMAIL_MAIL, 'web_site': WEBSITE})
        else:
            return HttpResponse(json.dumps({'mash': mash}),
                                content_type='application/json')


class AboutView(View):
    def get(self, request):
        return render(request, 'auto/about.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class BlogView(View):
    def get(self, request):
        return render(request, 'auto/blog.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class BlogSingleView(View):
    def get(self, request):
        return render(request, 'auto/blog-single.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class CarView(View):
    def get(self, request):
        return render(request, 'auto/car.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class CarSingleView(View):
    def get(self, request):
        return render(request, 'auto/car-single.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class ContactView(View):
    def get(self, request):
        return render(request, 'auto/contact.html',
                      {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                       'email_address': EMAIL_MAIL, 'web_site': WEBSITE})


class PricingView(View):
    def get(self, request):

        # car = [
        #     {
        #         'title': 'Mercedez-Benz C217',
        #         'img': 'images/car-1.jpg',
        #         'currency': '$',
        #         'time_price': '10.99',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '60.99',
        #         'when_day': '/per day',
        #         'month_price': '995.99',
        #         'when_month': '/per month'
        #     },
        #     {
        #         'title': 'Range Rover Evoque',
        #         'img': 'images/car-2.jpg',
        #         'currency': '$',
        #         'time_price': '15.30',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '80.50',
        #         'when_day': '/per day',
        #         'month_price': '990.00',
        #         'when_month': '/per month'
        #     },
        #     {
        #         'title': 'Audi RS6',
        #         'img': 'images/car-3.jpg',
        #         'currency': '$',
        #         'time_price': '10.50',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '55.60',
        #         'when_day': '/per day',
        #         'month_price': '900.65',
        #         'when_month': '/per month'
        #     },
        #     {
        #         'title': 'Ford Mustang',
        #         'img': 'images/car-4.jpg',
        #         'currency': '$',
        #         'time_price': '20.25',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '100.00',
        #         'when_day': '/per day',
        #         'month_price': '1200.00',
        #         'when_month': '/per month'
        #     },
        #     {
        #         'title': 'BWW F22',
        #         'img': 'images/car-5.jpg',
        #         'currency': '$',
        #         'time_price': '12.30',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '65.20',
        #         'when_day': '/per day',
        #         'month_price': '950.50',
        #         'when_month': '/per month'
        #     },
        #     {
        #         'title': 'Alfa Romeo 4C',
        #         'img': 'images/car-6.jpg',
        #         'currency': '$',
        #         'time_price': '17.80',
        #         'when_time': '/per hour',
        #         'fuel': '$3/hour fuel surcharges',
        #         'day_price': '78.20',
        #         'when_day': '/per day',
        #         'month_price': '980.60',
        #         'when_month': '/per month'
        #     },
        # ]

        car_model = PriceCar.objects.all().values()
        car = list(car_model)

        if not request.is_ajax():
            return render(request, 'auto/pricing.html',
                          {'phone_number': PHONE_NUMBER, 'address': ADDRESS,
                           'email_address': EMAIL_MAIL, 'web_site': WEBSITE})
        else:
            return HttpResponse(json.dumps({'car': car}),
                                content_type='application/json')

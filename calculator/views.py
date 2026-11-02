from json import loads

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AddView(View):
    def post(self, request):
        request_body = request.body  #type of request body is json
        form_data = loads(request_body)  # type of form_data is dict
        #converted json to dict using loads method of json module
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 + n2
        #print(request_body)

        data = {
            'messages': 'addition api called successfully',
            'sum': result
            }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name="dispatch")
class SubstractView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 - n2

        return JsonResponse(
            {'messages': 'substraction api is working',
              'difference': result}
        )

@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 * n2

        return JsonResponse(
            {
                'message: multi api working fine'
                'difference': result
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get('num2')
        result = n1 / n2

        return JsonResponse(
            {
                'message: multi api working fine'
                'division': result
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('h')
        n2 = form_data.get('w')
        result = n2/ (n1 ** 2)

        return JsonResponse(
            {
                'BMI': result,
                "hieght" : n1,
                'wieght' : n2
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class Age(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('b_year')
        n2 = form_data.get('c_year')
        result = n1 - n2

        return JsonResponse(
            {
                'age': result
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class Mark(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('obtained_mark')
        n2  = form_data.get('total_mark')
        result = (n1 / n2) * 100

        return JsonResponse(
            {
                'percentage': result
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class Area(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('length')
        n2 = form_data.get('width')
        result = n1 * n2

        return JsonResponse(
            {
                "widht": result
            }
        )
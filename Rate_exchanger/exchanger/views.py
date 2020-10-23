import requests

from django.shortcuts import render
from django.http import JsonResponse
from .models import Currency
# Create your views here.


def index(request):
    currency = list(Currency.objects.values())
    return render(request, 'exchanger/index.html', context={'currency': currency})

def exchange_rate_calculator(request):
    if request.method == 'POST':
        code_1 = request.POST['exchange_1'].strip()
        code_2 = request.POST['exchange_2'].strip()
        value_1 = request.POST['value_1']
        print("Exchange rate api is taking longer to response exchange rates!!")
        url = f"https://api.exchangeratesapi.io/latest?symbols={code_1},{code_2}"
        response = requests.get(url)

        currency = dict(response.json())
        #{'rates': {'INR': 87.3745, 'CAD': 1.5557}, 'base': 'EUR', 'date': '2020-10-21'}
        rate_1 = currency['rates'][code_1]
        rate_2 = currency['rates'][code_2]
        print(value_1)

        value_2 = float(value_1) * (rate_2/rate_1)
        print(value_2)
        data = {
            'result': value_2,
        }
        return JsonResponse(data)
    else:
        return JsonResponse(status=500)

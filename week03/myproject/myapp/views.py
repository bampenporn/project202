from django.shortcuts import render
from myapp.models import Customer

# Create your views here.
def index(request):
    context={
        'products':[
            {
                'name':'product_a',
                'price':100,
                'weight': 1.5
            },
            {
                'name':'product_b',
                'price':150,
                'weight': 0.8
            }
        ],
        'customers': Customer.objects.all()
    }
    return render(
        request,
        template_name='index.html',
        context=context
    )


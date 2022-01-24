from django.shortcuts import render

from rest_framework import viewsets

from centre.models import ShoppingCentre
from centre.serializers import ShoppingCentreSerializer

class ShoppingCentreViewSets(viewsets.ModelViewSet):
    queryset = ShoppingCentre.objects.all()
    serializer_class = ShoppingCentreSerializer
    permission_classes = []

def shopping_list(request):
    product = ShoppingCentre.objects.all().order_by('date');
    return render(request, 'centre_list.html', { 'product': product })

def shopping_detail(request, product):
    # return HttpResponse(slug)
    product = ShoppingCentre.objects.get(product=product)
    return render(request, 'centre_detail.html', { 'product': product })
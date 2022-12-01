from .models import Category
from os import link
from sre_constants import CATEGORY

#function that will create a link to all of the categories saved in datas
def categoryMenu(request):
    links=Category.objects.all()
    return dict(links=links)
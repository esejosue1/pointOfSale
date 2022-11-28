from .models import Category

#function that will create a link to all of the categories saved in datas
def categoryMenu(request):
    links=Category.objects.all()
    return dict(links=links)
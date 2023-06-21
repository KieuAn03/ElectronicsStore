from django.shortcuts import render
from home.models import Product
# Create your views here.
def index(request):
    if 'que' in request.GET:
        que = request.GET['que']
        products = Product.objects.filter(Name__icontains=que)
    else:
        products = Product.objects.all()
    context = {'products' : products}

    return render(request , 'home/index.html',context)

def checkouts(request):
    return render(request, 'checkout.html')
def deltail(request):
    """
    hàm lấy dữ liệu thể loại, tên truyện, số chương, chương truyện, để đưa lên web
    """
    id = request.GET.get('id','') 
    truyens = truyen.objects.filter(id=id) 
    tr = truyen.objects.get(id=id)
    tr.view_count=tr.view_count+1
    tr.save()   
    ct = truyen_category.objects.filter(Truyen = id)
    chapters = chapter.objects.filter(truyen = id)
    num_chap = chapter.objects.filter(truyen = id).count()
    num_cmt = comment.objects.filter(truyen=id).count()
    context = {
        'truyens' : truyens,
        'cts': ct,
        'chapters' : chapters,
        'num_cmt' : num_cmt,
        'num_chap' : num_chap,
    }
    return render(request, 'detail.html',context)

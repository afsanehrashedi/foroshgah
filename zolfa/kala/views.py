from django.shortcuts import render,HttpResponse

# Create your views here.
def kala(request):
    return HttpResponse("<b>شما با موفقیت  به قسمت کالا ها وارد شده اید </b>")
def filterr(request):
    return HttpResponse("<h1>  گزینه های فیلتر را مشاهده کنید </h1>")
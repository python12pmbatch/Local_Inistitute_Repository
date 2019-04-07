from django.shortcuts import render

from Curd_App1.models import Product
from Curd_App1.forms import ProductForm,UpdateForm,DeleteForm
from django.http import HttpResponse


def homeview(request):
    return render(request,'curdhome.html')


def insertview(request):
    if request.method=='POST':
        iform=ProductForm(request.POST)
        if iform.is_valid():
            pnum=request.POST.get('Product_Number','')
            pname=request.POST.get('Product_Name','')
            pcost=request.POST.get('Product_Cost','')
            pcolr=request.POST.get('Product_Color','')
            pclass=request.POST.get('Product_Class','')
            npd=request.POST.get('Number_Of_Products','')
            cname =request.POST.get('Customer_Name','')
            cnum =request.POST.get('Customer_Number','')
            email =request.POST.get('Email_Id','')

            data = Product(
                Product_Number = pnum,
                Product_Name  = pname,
                Product_Cost = pcost,
                Product_Color = pcolr,
                Product_Class = pclass,
                Number_Of_Products = npd,
                Customer_Name = cname,
                Customer_Number = cnum,
                Email_Id = email

            )

            data.save()

            iform = ProductForm()
            return render(request,'curdinserting.html',{'iform':iform})
        else:
            return HttpResponse('form not valid')


    else:
        iform = ProductForm()
        return render(request,'curdinserting.html',{'iform':iform})


def Updateview(request):
    if request.method=='POST':
        uform = UpdateForm(request.POST)
        if uform.is_valid():
            pid = request.POST.get('Product_Number','')
            pcost = request.POST.get('Product_Cost','')
            Product_Id = Product.objects.filter(Product_Number = pid)

            if not Product_Id:
                return HttpResponse("<h1>Data is Not Available</h1>")
            else:
                Product_Id.update(Product_Cost = pcost)
                uform = UpdateForm()
                return render(request,'curdupdating.html',{'uform':uform})
        else:
            return HttpResponse('Invalid From')
    else:
        uform =UpdateForm()
        return render(request,'curdupdating.html',{'uform':uform})


def retrieveview(request):
    rdata = Product.objects.all()
    return render(request,'curdretrieve.html',{'rdata':rdata})


def deleteview(request):
    if request.method=="POST":
        dform = DeleteForm(request.POST)
        if dform.is_valid():
            pid = request.POST.get('Product_Number','')
            proid = Product.objects.filter(Product_Number=pid)
            if not proid:
                return HttpResponse('<h1> Data is Not Available<h1>')
            else:
                proid.delete()
                dform = DeleteForm()
                return render(request,'deleteview.html',{'dform':dform})

        else:
            return HttpResponse('Form Invalid')
    else:
        dform = DeleteForm()
        return render(request,'deleteview.html',{'dform':dform})

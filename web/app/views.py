from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")



def res(request):
    fn=request.POST.get("fn")
    ln=request.POST.get('ln')
    if 'add' in request.POST:
        res=int(fn)+int(ln)
        return render(request,'index.html',{'data':res})
    elif 'sub' in request.POST:
        res=int(fn)-int(ln)
        return render(request,'index.html',{'data':res})
    elif 'mul' in request.POST:
        res=int(fn)*int(ln)
        return render(request,'index.html',{'data':res})
    elif 'div' in request.POST:
        try:
            res=int(fn)/int(ln)
        except ZeroDivisionError:
            res="invalid input"
        return render(request,'index.html',{'data':res})

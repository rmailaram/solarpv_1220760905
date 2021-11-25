from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm as userCreationform, AuthenticationForm as authform
from django.contrib.auth import login
from backend import models
from django.db.models import Q

from backend import forms
# from solarpvsite.backend.models import Teststandard
# from solarpvsite.backend.forms import ClientForm


def index(request):
    return render(request, 'solarpv/index.html')


def loginview(request):
    if request.method == 'POST':
        form = authform(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('/admin/')
            login(request, user)
            return redirect('index')
    else:
        form = authform()
    return render(request, 'solarpv/login.html', {'form': form})


def portal(request):
    return render(request, 'solarpv/portal.html')


def register(request):
    if request.method == 'POST':
        form = userCreationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = userCreationform()
    return render(request, 'solarpv/register.html', {'form': form})


def registerUser(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        clientData = {'clientname': "new client",
                      'clienttype': "new type"}
        clientForm = forms.ClientForm(clientData)
        clientForm.save()
        print(form)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    else:
        form = forms.UserForm()
    return render(request, 'index.html', {'form': form})


def addclientsView(request):
    return render(request, 'solarpv/clientView/addclients.html')


def addClient(request):
    if request.method == "POST":
        clients = forms.ClientForm(request.POST)
        if clients.is_valid():
            try:
                clients.save()
            except:
                pass
    else:
        clients = forms.ClientForm()
    return redirect("/clients")


def listClient(request):
    clients = models.Client.objects.all()
    return render(request, "clientView/clientlist.html", {'clients': clients})


def editClient(request, id):
    clients = models.Client.objects.get(id=id)
    return render(request, 'clientView/clientedit.html', {'clients': clients})


def updateClient(request, id):
    Clients = models.Client.objects.get(id=id)
    ClientsEditform = forms.ClientForm(request.POST, instance=Clients)
    if ClientsEditform.is_valid():
        ClientsEditform.save()
    return render(request, 'clientView/clientlist.html', {'Clients': Clients})


def destroyClient(request, id):
    Clients = models.Client.objects.get(id=id)
    Clients.delete()
    return redirect("clientView/clientlist.html")

# //Location


def addlocationsView(request):
    return render(request, 'solarpv/locationView/addlocations.html')


def addLocation(request):
    if request.method == "POST":
        locationForm = forms.LocationForm(request.POST)
        print(locationForm)
        if locationForm.is_valid():
            try:
                locationForm.save()
            except:
                pass

    return redirect("/locations")


def listLocation(request):
    locations = models.Location.objects.all()
    return render(request, "locationView/locationslist.html", {'locations': locations})


def editLocation(request, id):
    locations = models.Location.objects.get(locationid=id)
    return render(request, 'locationView/locationslist.html', {'locations': locations})


def updateLocation(request, id):
    locations = models.Location.objects.get(locationid=id)
    locationEditform = forms.LocationForm(request.POST, instance=locations)
    if locationEditform.is_valid():
        locationEditform.save()
    return render(request, 'locationView/locationslist.html', {'locations': locations})


def destroyLocation(request, id):
    location = models.Location.objects.get(locationid=id)
    location.delete()
    return redirect("/locations")

# //Product


def addproductsView(request):
    return render(request, 'solarpv/productsView/addproducts.html')


def addProduct(request):
    if request.method == "POST":
        productForm = forms.ProductForm(request.POST)
        if productForm.is_valid():
            try:
                productForm.save()
            except:
                pass
    else:
        form = forms.ProductForm()
    return redirect("/products")


def listProduct(request):
    products = models.Product.objects.all()
    return render(request, "productsView/productslist.html", {'products': products})


def editProduct(request, id):
    products = models.Product.objects.get(id=id)
    return render(request, 'productedit.html', {'products': products})


def updateProduct(request, id):
    products = models.Product.objects.get(id=id)
    productEditform = forms.ProductForm(request.POST, instance=products)
    if productEditform.is_valid():
        productEditform.save()
    return render(request, 'productsView/productslist.html', {'products': products})


def destroyProduct(request, id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return redirect("/products")

# Test Standard


def addtestStandardView(request):
    return render(request, 'solarpv/testStandardView/addTestStandard.html')


def addTestStandard(request):
    if request.method == "POST":
        testStandardForm = forms.TestStandardForm(request.POST)
        if testStandardForm.is_valid():
            try:
                testStandardForm.save()
            except:
                pass
    else:
        form = forms.TestStandardForm()
        return redirect("/teststandards")


def listTestStandard(request):
    Teststandard = models.Teststandard.objects.all()
    return render(request, "testStandardView/testStandardlist.html", {'Teststandard': Teststandard})


def editTestStandard(request, id):
    Teststandard = models.Teststandard.objects.get(standardid=id)
    return render(request, 'testStandardView/testStandardlist.html', {'Teststandard': Teststandard})


def updateTestStandard(request, id):
    Teststandard = models.Teststandard.objects.get(standardid=id)
    testStandardEditform = forms.TestStandardForm(
        request.POST, instance=Teststandard)
    if testStandardEditform.is_valid():
        testStandardEditform.save()
    return render(request, 'testStandardView/testStandardlist.html', {'Teststandard': Teststandard})


def destroyTestStandard(request, id):
    testStandard = models.Teststandard.objects.get(id=id)
    testStandard.delete()
    return redirect("/teststandards")


# Certification
def addcertificationView(request):
    return render(request, 'solarpv/certificationsView/addcertifications.html')


def addCertification(request):
    if request.method == "POST":
        testStandardForm = forms.CertificateForm(request.POST)
        print(testStandardForm)
        if testStandardForm.is_valid():
            try:
                testStandardForm.save()
            except:
                pass
    # else:
        # form = forms.CertificateForm()
    return redirect("/certification")


def listCertification(request):
    certifications = models.Certificate.objects.all()
    for cert in certifications:
        print(cert)
    return render(request, "certificationsView/certification.html", {'certifications': certifications})


def editCertification(request, id):
    certifications = models.Certificate.objects.get(id=id)
    return render(request, 'certificationsView/certificationedit.html', {'certifications': certifications})


def updateCertification(request, id):
    certifications = models.Certificate.objects.get(id=id)
    certificationsEditform = forms.CertificateForm(
        request.POST, instance=certifications)
    if certificationsEditform.is_valid():
        certificationsEditform.save()
    return render(request, 'certificationsView/certification.html', {'certifications': certifications})


def destroyCertification(request, id):
    certifications = models.Certificate.objects.get(id=id)
    certifications.delete()
    return redirect("/certification.html")

# def addCertificate(request):
#     if request.method == "POST":
#         form = forms.CertificateForm(request.POST)
#         # clientData = {'clientname': "new client",
#         #               'clienttype': "new type"}
#         # clientForm = forms.ClientForm(clientData)
#         # clientForm.save()
#         print(form)
#         if form.is_valid():
#             try:
#                 form.save()
#             except:
#                 pass
#     else:
#         form = forms.CertificateForm()
#     return render(request, 'certification.html', {'form': form})


# def certification(request):
#     query = request.GET.get('q'.strip().lstrip())
#     if request.method == "GET" and query is not None:
#         if query.isdigit():
#             queryset = models.Certificate.objects.filter(
#                 Q(report_number__exact=query))
#         else:
#             queryset = models.Certificate.objects.filter(
#                 Q(product__model_number__icontains=query))

#         context = {"certificates": queryset}
#         return render(request, 'search.html', context)
#     else:
#         queryset = models.Certificate.objects.all()
#         context = {"certificates": queryset}
#         return render(request, 'solarpv/certification.html', context)

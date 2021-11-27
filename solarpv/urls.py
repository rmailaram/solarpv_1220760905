from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('registerUser', views.registerUser, name='registeruser'),
    path('portal/', views.portal, name='portal'),

    path('clients/', views.listClient, name='clients'),
    path('clients/addclients',
         views.addclientsView, name='addclients'),
    path('clients/add', views.addClient, name='clientsadd'),
    path('clients/edit/<int:id>', views.editClient, name='clientsedit'),
    path('clients/update/<int:id>', views.updateClient, name='clientsupdate'),
    path('clients/delete/<int:id>', views.destroyClient, name='clientsdestroy'),

    path('locations/', views.listLocation, name='locations'),
    path('locations/addlocations',
         views.addlocationsView, name='addlocations'),
    path('locations/add', views.addLocation, name='locationsadd'),
    path('locations/edit/<int:id>', views.editLocation, name='locationsedit'),
    path('locations/update/<int:id>',
         views.updateLocation, name='locationsupdate'),
    path('locations/delete/<int:id>',
         views.destroyLocation, name='locationsdestroy'),

    path('products/', views.listProduct, name='products'),
    path('products/addproducts',
         views.addproductsView, name='addproducts'),
    path('products/add', views.addProduct, name='productsadd'),
    path('products/edit/<int:id>', views.editProduct, name='productsedit'),
    path('products/update/<int:id>', views.updateProduct, name='productsupdate'),
    path('products/delete/<int:id>', views.destroyProduct, name='productsdestroy'),

    path('teststandards/', views.listTestStandard, name='teststandards'),
    path('teststandards/addteststandards',
         views.addtestStandardView, name='addteststandards'),
    path('teststandards/add', views.addTestStandard, name='teststandardsadd'),
    path('teststandards/edit/<int:id>',
         views.editTestStandard, name='teststandardsedit'),
    path('teststandards/update/<int:id>',
         views.updateTestStandard, name='teststandardsupdate'),
    path('teststandards/delete/<int:id>',
         views.destroyTestStandard, name='teststandardsdestroy'),


    path('certification/', views.listCertification, name='certification'),
    path('certification/addcertifications',
         views.addcertificationView, name='addcertifications'),
    path('certification/add', views.addCertification, name='certificationadd'),
    path('certification/edit/<int:id>',
         views.editCertification, name='certificationedit'),
    path('certification/update/<int:id>',
         views.updateCertification, name='certificationupdate'),
    path('certification/delete/<int:id>',
         views.destroyCertification, name='certificationdestroy'),




]

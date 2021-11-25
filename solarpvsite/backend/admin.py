from django.contrib import admin
from .models import Certificate, Client, Location, Product, Teststandard


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificatenumber', 'certid', 'userid',
                    'reportnumber', 'issuedate', 'standardid', 'locationid', 'modelnumber')
    list_filter = ('certid', 'reportnumber', 'issuedate')


admin.site.register(Certificate, CertificateAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'clientname', 'clienttype')
    list_filter = ('clientname', 'clienttype')


admin.site.register(Client, ClientAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'address1', 'address2', 'city', 'state',
                    'postalcode', 'country', 'phonenumber', 'faxnumber', 'clientid')
    list_filter = ('address1', 'address2', 'city', 'state',
                   'postalcode', 'country', 'phonenumber', 'faxnumber')


admin.site.register(Location, LocationAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('modelnumber', 'productname', 'celltechnology', 'cellman', 'numcells', 'numcellsinseries', 'numseriesstrings', 'numdiodes', 'productlength', 'productwidth', 'productweight',
                    'superstratetype', 'superstrateman', 'substratetype', 'substrateman', 'frametype', 'frameadhesive', 'encapsulanttype', 'encapsulantman', 'junctionboxtype', 'junctionboxman')
    list_filter = ('productname', 'celltechnology', 'cellman', 'numcells', 'numcellsinseries', 'numseriesstrings', 'numdiodes', 'productlength', 'productwidth', 'productweight',
                   'superstratetype', 'superstrateman', 'substratetype', 'substrateman', 'frametype', 'frameadhesive', 'encapsulanttype', 'encapsulantman', 'junctionboxtype', 'junctionboxman')


admin.site.register(Product, ProductAdmin)


class TeststandardAdmin(admin.ModelAdmin):
    list_display = ('standardid', 'standardname',
                    'description', 'publisheddate')
    list_filter = ('standardname', 'description', 'publisheddate')


admin.site.register(Teststandard, TeststandardAdmin)

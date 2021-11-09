from rest_framework import serializers
from ..models import Client, User, Product, Certificate, Service

class Serializers:
    class ProductSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Product
            fields = ['modelNum', 'name', 'cell_technology', 'cell_manufacturer', 'number_of_cells', 'number_of_cells_in_series', 'number_of_series_strings', 'number_of_diodes', 'product_length', 'product_width', 'product_weigtht', 'superstrate_type', 'Superstrate_manufacturer', 'substrate_type', 'Substrate_manufacturer', 'frame_type', 'Frame_adhesive', 'encapsulant_type', 'encapsulant_manufacturer', 'junction_box_type', 'Junction_box_manufacturer']

    class CertificateSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Certificate
            fields = ['cert_number', 'report_number', 'location_id', 'user_id', 'test_standard_id', 'product_id', 'issue_date']

    class ServiceSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Service
            fields =  ['description',  'is_FI_required',  'FI_frequency',  'service_name',  'test_standard_id']
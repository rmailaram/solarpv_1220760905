from django.db import models

# Create your models here.
class Client(models.Model):   
    clientId = models.CharField(max_length=50)
    client_code = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name
    
    class Meta:  
        db_table = "clients"

class User(models.Model):   
    User = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client, null=True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.EmailField()
    officephone = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    isstaff = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

    class Meta:  
        db_table = "users"


class Location(models.Model):
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)

    def __str__(self):
        return self.state

    class Meta:  
        db_table = "locations"

class TestStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    published_date = models.CharField(max_length=50)

    class Meta:  
        db_table = "test_standard"

class Service(models.Model):
    description = models.CharField(max_length=50)
    is_FI_required = models.CharField(max_length=50)
    FI_frequency = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    test_standard_id = models.ForeignKey(TestStandard, on_delete = models.CASCADE)

    class Meta:  
        db_table = "services"


class TestSequence(models.Model):
    sequence_id = models.CharField(max_length=50)
    sequence_name = models.CharField(max_length=50)

    class Meta:
        db_table = "test_sequence"

class Product(models.Model):
    modelNum = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    cell_technology = models.CharField(max_length=50)
    cell_manufacturer = models.CharField(max_length=50)
    number_of_cells = models.CharField(max_length=50)
    number_of_cells_in_series = models.CharField(max_length=50)
    number_of_series_strings = models.CharField(max_length=50)
    number_of_diodes = models.CharField(max_length=50)
    product_length = models.CharField(max_length=50)
    product_width = models.CharField(max_length=50)
    product_weigtht = models.CharField(max_length=50)
    superstrate_type = models.CharField(max_length=50)
    Superstrate_manufacturer = models.CharField(max_length=50)
    substrate_type = models.CharField(max_length=50)
    Substrate_manufacturer = models.CharField(max_length=50)
    frame_type = models.CharField(max_length=50)
    Frame_adhesive = models.CharField(max_length=50)
    encapsulant_type = models.CharField(max_length=50)
    encapsulant_manufacturer = models.CharField(max_length=50)
    junction_box_type = models.CharField(max_length=50)
    Junction_box_manufacturer = models.CharField(max_length=50)
    class Meta:  
        db_table = "products"

class PerformanceData(models.Model):
    model_num = models.ForeignKey(Product, on_delete = models.CASCADE)
    test_sequence_id = models.ForeignKey(TestSequence, on_delete = models.CASCADE)
    max_system_voltage = models.CharField(max_length=50)
    open_circuit_voltage = models.CharField(max_length=50)
    short_circuit_current = models.CharField(max_length=50)
    voltage_at_max_power = models.CharField(max_length=50)
    current_at_max_power = models.CharField(max_length=50)
    Max_power_output = models.CharField(max_length=50)
    fill_factor = models.CharField(max_length=50)

    class Meta:  
        db_table = "performance_data"


class Certificate(models.Model):
    cert_number = models.CharField(max_length=50)
    report_number = models.CharField(max_length=50)
    location_id = models.ForeignKey(Location, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    test_standard_id = models.ForeignKey(TestStandard, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    issue_date = models.CharField(max_length=50)

    class Meta:
        db_table = "certificates"
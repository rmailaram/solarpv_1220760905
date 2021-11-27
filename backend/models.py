from django.db import models


class Client(models.Model):
    clientid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=200)
    clienttype = models.CharField(max_length=200)

    def __str__(self):
        return self.clientname


class Testsequence(models.Model):
    sequence_id = models.AutoField(primary_key=True)
    sequence_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sequence_name


class Teststandard(models.Model):
    standardid = models.AutoField(primary_key=True)
    standardname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    publisheddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.standardname


class Product(models.Model):
    modelnumber = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=200)
    celltechnology = models.CharField(max_length=200)
    cellman = models.CharField(max_length=200)
    numcells = models.IntegerField()
    numcellsinseries = models.IntegerField()
    numseriesstrings = models.IntegerField()
    numdiodes = models.IntegerField()
    productlength = models.FloatField()
    productwidth = models.FloatField()
    productweight = models.FloatField()
    superstratetype = models.CharField(max_length=200)
    superstrateman = models.CharField(max_length=200)
    substratetype = models.CharField(max_length=200)
    substrateman = models.CharField(max_length=200)
    frametype = models.CharField(max_length=200)
    frameadhesive = models.CharField(max_length=200)
    encapsulanttype = models.CharField(max_length=200)
    encapsulantman = models.CharField(max_length=200)
    junctionboxtype = models.CharField(max_length=200)
    junctionboxman = models.CharField(max_length=200)

    def __str__(self):
        return self.productname


class Service(models.Model):
    serviceid = models.AutoField(primary_key=True)
    servicename = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isfirequired = models.CharField(max_length=3)
    fifrequency = models.CharField(max_length=200)
    standardid = models.ForeignKey(Teststandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.servicename


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    officephone = models.BigIntegerField()
    cellphone = models.BigIntegerField()
    prefix = models.CharField(max_length=200)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.userid


class Location(models.Model):
    locationid = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=200)
    phonenumber = models.BigIntegerField()
    faxnumber = models.BigIntegerField()
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1


class Performancedata(models.Model):
    modelnumber = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequenceid = models.ForeignKey(Testsequence, on_delete=models.CASCADE)
    maxsystemvoltage = models.IntegerField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()


class Certificate(models.Model):
    certificatenumber = models.AutoField(primary_key=True)
    certid = models.CharField(max_length=200)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    reportnumber = models.CharField(max_length=200)
    issuedate = models.DateField(auto_now_add=True)
    standardid = models.ForeignKey(Teststandard, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelnumber = models.CharField(max_length=200)

    def __str__(self):
        return self.certid

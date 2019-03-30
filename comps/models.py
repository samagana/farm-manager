from django.db import models

class Worker(models.Model):
    WorkerTypes = (
        ('W', 'Weekly Wage'),
        ('D', 'Daily Wage'),
        ('M', 'Monthly Wage'),
        ('H', 'Hourly Wage'),
    )
    name = models.CharField(max_length = 30)
    role = models.CharField(max_length = 30)
    wtype = models.CharField(max_length = 30, choices = WorkerTypes)
    salary = models.IntegerField()
    duration = models.IntegerField()
    is_active = models.BooleanField(default = False)


class Crop(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = False)
    date = models.DateField()

class Fertilizer(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    crop = models.ForeignKey(Crop, related_name='uses_f', on_delete=models.CASCADE)
    is_active = models.BooleanField(default = False)

class Insecticide(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    crop = models.ForeignKey(Crop, related_name='uses_i', on_delete=models.CASCADE)
    is_active = models.BooleanField(default = False)

class Pesticide(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    crop = models.ForeignKey(Crop, related_name='uses_p', on_delete=models.CASCADE)
    is_active = models.BooleanField(default = False)

class Loan(models.Model):
    amount = models.IntegerField()
    address = models.CharField(max_length = 255)
    loan_type = models.CharField(max_length = 20)
    loan_id = models.CharField(max_length = 20)
    emi = models.IntegerField()

class Sale(models.Model):
    crop = models.ForeignKey(Crop, related_name='sell_crop', on_delete = models.CASCADE)
    rate = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()

class History(models.Model):
    month = models.DateField()
    expenditure = models.IntegerField()
    income = models.IntegerField()
    profit = models.IntegerField()
    date = models.DateField()





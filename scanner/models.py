from django.db import models
from employees.models import UserModel
from stores.models import WarehouseModel
from datetime import datetime
import pytz
# Create your models here.
class Timesheet(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    enter_time = models.DateTimeField()
    leave_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        print(type(self.enter_time))
        print(type(self.leave_time))
        if self.enter_time and self.leave_time:
            if isinstance(self.leave_time, str):
                self.leave_time = datetime.strptime(self.leave_time, '%Y-%m-%d %H:%M:%S')
                print(type(self.leave_time))
                self.leave_time = pytz.timezone('Africa/Accra').localize(self.leave_time)
                print(type(self.leave_time))
            self.duration = self.leave_time - self.enter_time

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enter_time}"

class ToolCheckoutModel(models.Model):
    CONDITION_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]
    tool = models.ForeignKey(WarehouseModel, on_delete=models.CASCADE)
    employee = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_rating = models.IntegerField(choices=CONDITION_CHOICES, null=True, blank=True)
    condition_comment = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        print(type(self.checkout_date))
        print(type(self.return_date))
        if self.checkout_date and self.return_date:
            if isinstance(self.return_date, str):
                self.return_date = datetime.strptime(self.return_date, '%Y-%m-%d %H:%M:%S')
                print(type(self.return_date))
                self.return_date = pytz.timezone('Africa/Accra').localize(self.return_date)
                print(type(self.return_date))
            self.duration = self.return_date - self.checkout_date

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tool}{self.checkout_date}{self.employee}"
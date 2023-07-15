from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import qrcode
from io import BytesIO
from django.core.files import File
import os

import pytz
# Create your models here.
class UserModel(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    employeeID = models.CharField(max_length=20,unique=True)
    date_joined = models.DateField()
    dob = models.DateField()
    job_title = models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone_number = PhoneNumberField(blank=False,region="ZA",unique=True)
    emergency_contact = PhoneNumberField(blank=False,region="ZA",unique=True)
    contractHours = models.DecimalField(decimal_places=2,max_digits=100)
    salary = models.DecimalField(decimal_places=2, max_digits=100)
    profileImage = models.ImageField(upload_to='identification/profiles/')
    working_status = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_security = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_employeeID = self.employeeID

    def save(self, *args, **kwargs):
        # Only generate a new QR code if the employeeID has changed
        if self.employeeID != self.__original_employeeID:
            # Generate QR code data based on first name and employee ID
            qr_data = f"{self.employeeID}"

            # Create a QR code instance and add the data
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Generate the QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Prepare the file name and path for QR code
            qr_filename = f"{self.employeeID}_qr.png"
            qr_filepath = os.path.join('qr_codes/profiles', qr_filename)

            # Save the QR code image to a BytesIO stream
            temp_qr_image = BytesIO()
            qr_image.save(temp_qr_image, format='PNG')
            temp_qr_image.seek(0)

            # Set the user's qr_code field with the saved QR code image file
            self.qr_code.save(qr_filepath, File(temp_qr_image), save=False)

            # Update the original employeeID
            self.__original_employeeID = self.employeeID

        # Proceed with the rest of the save method as usual
        super().save(*args, **kwargs)
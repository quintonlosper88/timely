from django.db import models
import qrcode
from django.core.files import File
from io import BytesIO
import os
# Create your models here.
class WarehouseModel(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    item_photo = models.ImageField(upload_to='identification/item_photos/')
    qr_code = models.ImageField(upload_to='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name + ' ' + self.manufacturer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_serial_number = self.serial_number

    def save(self, *args, **kwargs):
        # Only generate a new QR code if the serial_number has changed
        if self.serial_number != self.__original_serial_number:
            # Generate QR code data based on manufacturer + serial_number + created_date
            qr_data = f"{self.manufacturer}{self.serial_number}{self.created_at}"

            # Create a QR code instance and add the data
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Generate the QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Prepare the file name and path for QR code
            qr_filename = f"{self.manufacturer}{self.serial_number}{self.created_at}_qr.png"
            qr_filepath = os.path.join('qr_codes/item_qr_codes', qr_filename)

            # Save the QR code image to a BytesIO stream
            temp_qr_image = BytesIO()
            qr_image.save(temp_qr_image, format='PNG')
            temp_qr_image.seek(0)

            # Set the user's qr_code field with the saved QR code image file
            self.qr_code.save(qr_filepath, File(temp_qr_image), save=False)

            # Update the original serial_number
            self.__original_serial_number = self.serial_number

        # Check if profile image exists, and if it does, save it to the user's profileImage field
        # Note: It seems you might be referencing a non-existing field 'profileImage'. Should it be 'item_photo'?
        if os.path.exists('profiles/item_photos'):
            profile_filename = f"{self.manufacturer}{self.serial_number}{self.created_at}_itemprofile.png"
            profile_filepath = os.path.join('profiles/item_photos', profile_filename)
            with open(profile_filepath, 'rb') as f:
                self.item_photo.save(profile_filename, File(f), save=False)

        super().save(*args, **kwargs)
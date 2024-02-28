from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doc = models.BooleanField(default=False)
    image = models.URLField(max_length=1000, default=False)
    phone_number = models.IntegerField(max_length = 10,default="0000000000")

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='online_medic_users',
        blank=True,
        help_text='The groups this user belongs to. A user may belong to multiple groups.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='online_medic_users',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    pass

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    specification = models.TextField()  
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Price: {self.price})"

class Prescription(models.Model):
    patient = models.ManyToManyField(User, related_name="prescriptions")
    meds = models.ManyToManyField(Medicine, related_name="prescribed_to")
    doctor = models.ManyToManyField(User, related_name="prescriptions_written")

    def __str__(self):
        patients = ', '.join([patient.username for patient in self.patient.all()])
        doctors = ', '.join([doctor.username for doctor in self.doctor.all()])
        return f"Prescription for Patients: {patients} - Doctors: {doctors}"

from django.db import models

from user.models import Doctor, Patient


class WeekDay(models.TextChoices):
    MONDAY = 'MON', 'Monday'
    TUESDAY = 'TUE', 'Tuesday'
    WEDNESDAY = 'WED', 'Wednesday'
    THURSDAY = 'THU', 'Thursday'
    FRIDAY = 'FRI', 'Friday'
    SATURDAY = 'SAT', 'Saturday'
    SUNDAY = 'SUN', 'Sunday'


class CurrencyType(models.TextChoices):
    USD = 'USD', 'US Dollars'
    UZB = 'UZB', 'Uzbek Soums',
    EUR = 'EUR', 'Euro'


class PaymentType(models.TextChoices):
    CASH = 'CASH', 'Via Cash'
    CARD = 'CARD', 'Via Card'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'appointment'


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=WeekDay)

    class Meta:
        db_table = 'schedule'


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    medicines = models.ManyToManyField('Medicine', related_name='medicines')
    tests = models.ManyToManyField('MedicalTest', related_name='tests')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'prescription'


class PrescriptionComment(models.Model):
    prescription = models.OneToOneField(Prescription, on_delete=models.DO_NOTHING)
    comment = models.TextField()

    class Meta:
        db_table = 'prescription_comment'


class Payment(models.Model):
    payment_type = models.CharField(max_length=4, choices=PaymentType, default=PaymentType.CASH.value)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    currency_type = models.CharField(max_length=3, choices=CurrencyType, default=CurrencyType.USD.value)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payment'


class MedicalTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'medical_test'


class Notification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey('MedicineGroup', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'medicine'


class MedicineGroup(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'medicine_group'


class HospitalInventory(models.Model):
    medicine = models.OneToOneField(Medicine, on_delete=models.DO_NOTHING, related_name='medicine')
    supplier = models.ForeignKey('Pharmacy', on_delete=models.DO_NOTHING, related_name='medicine_supplier')
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'hospital_inventory'


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'pharmacy'

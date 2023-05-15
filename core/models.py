from django.db import models

from user.models import Doctor, Patient


class WeekDay(models.TextChoices):
    MONDAY = ('MON', 'Monday')
    TUESDAY = ('TUE', 'Tuesday')
    WEDNESDAY = ('WED', 'Wednesday')
    THURSDAY = ('THU', 'Thursday')
    FRIDAY = ('FRI', 'Friday')
    SATURDAY = ('SAT', 'Saturday')
    SUNDAY = ('SUN', 'Sunday')


class CurrencyType(models.TextChoices):
    USD = 'USD', 'US Dollars'
    UZB = 'UZB', 'Uzbek Soums'
    EUR = 'EUR', 'Euro'


class PaymentType(models.TextChoices):
    CASH = 'CASH', 'Via Cash'
    CARD = 'CARD', 'Via Card'


class AppointmentStatus(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    CANCELLED = 0, 'Cancelled'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    scheduled_at = models.ForeignKey('Schedule', on_delete=models.DO_NOTHING)
    appointment_time = models.DateTimeField(null=True)
    status = models.IntegerField(choices=AppointmentStatus.choices, null=True)

    class Meta:
        db_table = 'appointment'
        managed = False

    def __str__(self):
        return 'Doctor %s -> %s' % (self.doctor.user.get_full_name(), self.patient.name)


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=WeekDay.choices)
    from_time = models.TimeField()
    to_time = models.TimeField()
    time_per_patient = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'schedule'
        managed = False

    def __str__(self):
        return "%s's schedule on %s" % (self.doctor.user.get_full_name(), self.day)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    medicines = models.ManyToManyField('Medicine', related_name='medicines')
    tests = models.ManyToManyField('MedicalTest', related_name='tests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    medical_record = models.ForeignKey('MedicalRecord', on_delete=models.DO_NOTHING, related_name='medical_record')
    comments = models.TextField()

    class Meta:
        db_table = 'prescription'
        managed = False

    def __str__(self):
        return 'Prescription for %s' % self.patient.name


class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.DO_NOTHING)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Medical record of %s' % self.patient.name

    class Meta:
        managed = False


class PaymentHistory(models.Model):
    payment_type = models.CharField(max_length=4, choices=PaymentType.choices, default=PaymentType.CASH.value)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    currency_type = models.CharField(max_length=3, choices=CurrencyType.choices, default=CurrencyType.USD.value)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payment_history'
        managed = False


class MedicalTest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'medical_test'
        managed = False

    def __str__(self):
        return self.title


class Notification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'
        managed = False

    def __str__(self):
        return 'Notification to %s' % self.patient.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey('MedicineGroup', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'medicine'
        managed = False

    def __str__(self):
        return self.name


class MedicineGroup(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'medicine_group'
        managed = False

    def __str__(self):
        return self.title


class HospitalInventory(models.Model):
    title = models.CharField(max_length=100)
    supplier = models.ForeignKey('Pharmacy', on_delete=models.DO_NOTHING, related_name='medicine_supplier')

    class Meta:
        db_table = 'hospital_inventory'
        managed = False

    def __str__(self):
        return self.title


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'pharmacy'
        managed = False

    def __str__(self):
        return self.name


class MedicineInStock(models.Model):
    inventory = models.ForeignKey(HospitalInventory, on_delete=models.DO_NOTHING)
    medicine = models.OneToOneField(Medicine, on_delete=models.CASCADE)
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'medicine_in_stock'
        managed = False

    def __str__(self):
        return '%s in stock' % self.medicine.name.title()

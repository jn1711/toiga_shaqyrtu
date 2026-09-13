from django.db import models


class RSVPResponse(models.Model):
    class Attendance(models.TextChoices):
        ATTENDING = 'yes', 'Иә, әрине'
        MAYBE = 'maybe', 'Жұбайыммен келемін'
        DECLINE = 'no', 'Келе алмаймын'

    full_name = models.CharField(max_length=200, verbose_name='Аты-жөні')
    attendance = models.CharField(max_length=10, choices=Attendance.choices, verbose_name='Қатысуым')
    guest_count = models.PositiveIntegerField(default=1, verbose_name='Қонақтар саны')
    notes = models.TextField(blank=True, verbose_name='Қосымша ақпарат')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} - {self.get_attendance_display()}'


class Wish(models.Model):
    name = models.CharField(max_length=200, verbose_name='Аты')
    message = models.TextField(verbose_name='Тілегі')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Тілек'
        verbose_name_plural = 'Тілектер'

    def __str__(self):
        return f'{self.name}: {self.message[:40]}'

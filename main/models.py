from django.db import models


class LampPost(models.Model):

    lamp_id = models.IntegerField(verbose_name='Lamp number', unique=True)
    ON_OFF = [(1, 'ON',),
              (0, 'OFF',)]
    is_on = models.IntegerField(verbose_name='Power', choices=ON_OFF, default=0)
    brightness = models.IntegerField(verbose_name='brightness percent', default=50)
    on_time = models.DateTimeField(verbose_name='Time the power on', blank=True, null=True)
    off_time = models.DateTimeField(verbose_name='Time the power off', blank=True, null=True)

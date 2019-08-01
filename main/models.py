from django.db import models


class LampPost(models.Model):

    lamp_id = models.IntegerField(verbose_name='Lamp number', null=False, blank=False)
    is_on = models.BooleanField(verbose_name='Power is on', default=False)
    brightness = models.IntegerField(verbose_name='brightness percent', default=0)
    on_time = models.DateTimeField(verbose_name='Time the power on', blank=True)
    off_time = models.DateTimeField(verbose_name='Time the power off', blank=True)

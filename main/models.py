from django.db import models


class LampPost(models.Model):

    is_on = models.BooleanField(verbose_name='Power is on', default=False)
    brightness = models.IntegerField(verbose_name='brightness percent', default=0)
    on_time = models.DateTimeField(verbose_name='Time the power on', blank=True)
    off_time = models.DateTimeField(verbose_name='Time the power off', blank=True)

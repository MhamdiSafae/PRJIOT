
import os
from datetime import datetime

from django.core.mail import send_mail
from django.db import models
from django.forms import forms


class dht (models.Model):
    temp= models.FloatField(null=True)
    dt= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):return str(self.temp)




def save(self, *args, **kwargs):
    if self.temp > 8:
        import telepot
        token = '5970971360:AAGb-JSJPtbnZaK7GZsdOkkIcS5vQbRB0PY'
        rece_id = 22078417449
        bot = telepot.Bot(token)
        bot.sendMessage(rece_id, 'température  crtique dépasse la normale')
        print(bot.sendMessage(rece_id, 'température critique dépasse la normale,'))
        send_mail(
        'température est critique :' + str(self.temp),

        'mhamdisafae4gmail.com',
        ['safaem99@gmail.com'],
        fail_silently=False,)

    return super().save(*args, **kwargs)
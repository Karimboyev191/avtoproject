from django.db import models


class Yonalishlar(models.Model):
    nomi=models.CharField(max_length=200)
    xizmatlar=models.CharField(max_length=200)
    picture=models.ImageField(default='def.jpg')

    def __str__(self):
        return self.nomi

class Ustalar(models.Model):
    fio=models.CharField(max_length=200)
    tel=models.CharField(max_length=200)

    def __str__(self):
        return self.fio

class Usta_yonalishi(models.Model):
    usta_id=models.ForeignKey(Ustalar,on_delete=models.CASCADE)
    yonalish_id=models.ForeignKey(Yonalishlar,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usta_id} - {self.yonalish_id}"

class Zakaz(models.Model):
    mijoz_fio=models.CharField(max_length=200)
    avtosi=models.CharField(max_length=200)
    rangi=models.CharField(max_length=200)
    diagnostika=models.CharField(max_length=200)

    def __str__(self):
        return self.mijoz_fio

class Diagnostikalar(models.Model):
    zakaz_id=models.ForeignKey(Zakaz,on_delete=models.CASCADE)
    usta_id=models.ForeignKey(Ustalar,on_delete=models.CASCADE)
    usta_haqqi=models.DecimalField(max_digits=10,decimal_places=2)
    servis=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.zakaz_id}"

class TugallanganIshlar(models.Model):
    zakaz_id=models.IntegerField()
    usta_id=models.IntegerField()
    usta_haqqi=models.DecimalField(max_digits=10,decimal_places=2)
    servis = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.zakaz_id}"
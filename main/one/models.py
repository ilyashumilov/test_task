from django.db import models


roles = (
    ("seller","seller"),
    ("buyer","buyer"),
)

types = (
    ("rose","rose"),
    ("tulip","tulip"),
)

colors = (
    ("red","red"),
    ("white","white"),
)

class user(models.Model):
    role = models.CharField(max_length=10,choices=roles)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)

class lot(models.Model):
    seller = models.ForeignKey(user,on_delete=models.CASCADE)

    flower_type = models.CharField(max_length=50,choices=types)
    flower_color = models.CharField(max_length=50, choices=colors)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return str(self.flower_type) + ' ' + str(self.flower_color)+ ' ' + str(self.amount)

class reviews(models.Model):

    reviewed = models.CharField(max_length=50) # may be either user's or lot's name
    review = models.TextField(max_length = 500)

    def __str__(self):
        return str(self.reviewed) + ' ' + str(self.review)

class deal(models.Model):
    buyer = models.ForeignKey(user, on_delete=models.CASCADE)
    lot = models.ForeignKey(lot,on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=50)
    comment = models.TextField(max_length = 500)

    def __str__(self):
        return str(self.buyer) + ' ' + str(self.lot)


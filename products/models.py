from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]

    def votes_total(self):
        votes = 0
        for upvote in Upvote.objects.all():
            if upvote.product == self:
                votes += 1
        return votes


class Upvote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

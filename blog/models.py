# All lines starting with from or import are lines that add some bits from other files. So instead of copying
# and pasting the same things in every file, we can include some parts with from ... import ....

from django.db import models
from django.utils import timezone

# this line defines our model (it is an object)
# 'Post' is the name of our model. Always start a class name with an uppercase letter.
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
    # models.ForeignKey – this is a link to another model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # models.CharField – this is how you define text with a limited number of characters
    title = models.CharField(max_length=200)
    # models.TextField – this is for long text without a limit
    text = models.TextField()
    # models.DateTimeField – this is a date and time
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # def means that this is a function/method and publish is the name of the method
    # we use lowercase and underscores instead of spaces
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # when we call __str__() we will get a text (string) with a Post title
    def __str__(self):
        return self.title

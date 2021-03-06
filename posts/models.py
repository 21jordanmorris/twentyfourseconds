from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
import os

# Change
def upload_location(instance, filename):
    return os.path.join('%s' % instance.slug, filename)

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, default="")
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    writer = models.CharField(max_length=255, default="")
    content = models.TextField()
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_location,
        null=True, blank=True, 
        width_field="width_field", 
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    SPORT_CHOICES = (
        ("NBA", "NBA"),
        ("CFB", "CFB"),
        ("NFL", "NFL"),
    )

    sport = models.CharField(max_length=25, choices=SPORT_CHOICES, default="Null")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-pk")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
    
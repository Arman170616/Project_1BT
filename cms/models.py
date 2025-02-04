# from django.db import models
# from django.utils.translation import gettext_lazy as _

# class HomePageContent(models.Model):
#     title_en = models.CharField(max_length=255, verbose_name=_("Title (English)"))
#     title_fr = models.CharField(max_length=255, verbose_name=_("Title (French)"))
#     description_en = models.TextField(verbose_name=_("Description (English)"))
#     description_fr = models.TextField(verbose_name=_("Description (French)"))
#     # Add more fields as needed

#     def __str__(self):
#         return self.title_en

from django.db import models

class HomePageContent(models.Model):
    page_name = models.CharField(max_length=255, default="home", verbose_name="Page Name")
    title_en = models.CharField(max_length=255, verbose_name="Title (English)")
    title_fr = models.CharField(max_length=255, verbose_name="Title (French)")
    description_en = models.TextField(verbose_name="Description (English)")
    description_fr = models.TextField(verbose_name="Description (French)")

    def __str__(self):
        return f"{self.page_name} - {self.title_en}"


# from django.db import models

# class HomePageContent(models.Model):
#     title_en = models.CharField(max_length=255, verbose_name="Title (English)")
#     title_fr = models.CharField(max_length=255, verbose_name="Title (French)")
#     description_en = models.TextField(verbose_name="Description (English)")
#     description_fr = models.TextField(verbose_name="Description (French)")

#     def __str__(self):
#         return self.title_en
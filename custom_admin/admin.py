from django.urls import re_path
from django.contrib import admin

from .views import my_view


# def get_admin_urls(urls):
#     def get_urls():
#         my_urls = [re_path(r"^my_view/$", admin.site.admin_view(my_view))]
#         return my_urls + urls

#     return get_urls


# admin_urls = get_admin_urls(admin.site.get_urls())
# admin.site.get_urls = admin_urls

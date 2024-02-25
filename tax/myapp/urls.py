from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:num>",views.calc, name="anyNumber"),
    path("taxrate/",views.tax_rate, name="taxrate"),
    ]
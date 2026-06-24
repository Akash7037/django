from . import views
from django.urls import path
urlpatterns = [path("",views.home,name=""),path("viewer/<int:post>",views.show,name="viewer"),path("new",views.new,name="new"),path("viewer/delete/<int:bi>",views.delete,name="delete")]

from django.urls import path
from . import views

urlpatterns = [
  path("books/",views.book_list,name="book_list"),
    path("updatee/<int:id>/",views.update_book,name="update_book"),
    path("deletee/<int:id>/",views.delete_book,name="delete_book"),
    path("dashboard/",views.dashboard,name="dashboard"),
]
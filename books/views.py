from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from .models import Book
from .forms import BookForm


def book_list(request):

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
        form = BookForm()

    books = Book.objects.all()
    return render(request,"books.html",{"form": form,"books": books})


def update_book(request, id):

    book = Book.objects.get(id=id)

    if request.method == "POST":

        form = BookForm(request.POST,instance=book)

        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
       form = BookForm(instance=book)

    return render(request,"update.html",{"form": form})


def delete_book(request, id):

    book = Book.objects.get(id=id)
    book.delete()
    return redirect("book_list")


def dashboard(request):

    search = request.GET.get("author")
    books = Book.objects.all()

    if search:

        books = books.filter(author__icontains=search)

    available_books = Book.objects.filter(is_available=True)
    ordered_books = Book.objects.order_by("-price")
    category_count = (Book.objects.values("category").annotate(total=Count("id")))
    avg_price = ( Book.objects.aggregate(Avg("price")))
    total_books = (Book.objects.count())
    latest_books = (Book.objects.order_by("-published_date")[:5])
    return render(request,"dashboard.html",{
            "books": books,
            "available_books": available_books,
            "ordered_books": ordered_books,
            "category_count": category_count,
            "avg_price": avg_price,
            "total_books": total_books,
            "latest_books": latest_books
        }
    )

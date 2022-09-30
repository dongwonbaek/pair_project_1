from django.shortcuts import redirect, render
from .models import Review

# Create your views here.


def index(request):
    review = Review.objects.all()

    context = {
        "reviews": review,
    }

    return render(request, "articles/index.html", context)


def create(request):
    return render(request, "articles/create.html")


def write(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)

    return redirect("articles:index")


def detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        "review": review,
    }
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    Review.objects.get(id=pk).delete()

    return redirect("articles:index")


def edit(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        "review": review,
    }
    return render(request, "articles/edit.html", context)


def update(request, pk):
    review = Review.objects.get(id=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content

    review.save()

    return redirect("articles:detail", review.pk)

from django.shortcuts import render
from django.http import HttpResponse
from Customer.forms import UserForm, FilmForm
from Customer.models import Film, Ticket, User
from django.shortcuts import redirect

# Create your views here.

class Films():

    def get_film(film):
        context = Film.objects.get(title = film)
        return context
    
    def get_filmList():
        context = Film.objects.all()
        return context
    
    def update_film(self, film, title, age, descritopn, duration):
        context = Film.objects.get(title = film)

        context.title = title
        context.ageRating = age
        context.description = descritopn
        context.duration = duration
        context.save()

        return context

    def create_film(request):
        form = FilmForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                message = form.save(commit=True)
                return redirect("home")
        else:
            return render(request, "home.html", {"form": form})

    def remove_film(film):
        context = Film.objects.get(title = film)
        context.delete()


def home(request):
    Movie = Films
    return render(
        request,
        'home.html',
        {
            'lines' : Movie.get_filmList
        }
    )

def UserDetails(request):
    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=True)
            return redirect("home")
    else:
        return render(request, "user.html", {"form": form})


def TicketView(request, film):
    Movie = Films
    return render(
        request,
        'ticket.html',
        {
            'films' : Movie.get_film(film),
        }
    )
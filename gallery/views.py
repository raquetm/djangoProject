from django.shortcuts import render, get_object_or_404
from .models import Artwork

# Create your views here.
def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'home.html', {'artworks': artworks})

def artwork_detail(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    return render(request, 'artworkDetail.html', {'artwork': artwork})

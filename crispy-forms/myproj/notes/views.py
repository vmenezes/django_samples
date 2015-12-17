from django.shortcuts import render
from django.views.generic import View

from .forms import NoteForm


class HomeView(View):
    def get(self, request):
        note_form = NoteForm()
        context = {'form': note_form}
        return render(request, 'notes/home.html', context)
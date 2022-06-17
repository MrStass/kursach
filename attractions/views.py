from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CommentForm
from .models import Attractions, Comments
from django.shortcuts import render, redirect


def AttractionsView(request, attractions_id):
    return render(request, "attractions/attractions_list.html", {"Attractions": Attractions.objects.filter(country=attractions_id)})


class AddCommentView(CreateView):
    model = Comments
    template_name = "attractions/add_comments.html"
    form_class = CommentForm
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.instance.attraction_id = self.kwargs['pk']
        form_u = form.save(commit=False)
        form_u.author = self.request.user
        form_u.save()
        return super().form_valid(form)


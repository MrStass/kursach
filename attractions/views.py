from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CommentForm
from .models import Attractions, Comments
from django.shortcuts import render, redirect


def AttractionsView(request, attractions_id):
    p = Paginator(Attractions.objects.filter(country=attractions_id), 3)
    page = request.GET.get('page')
    attractions = p.get_page(page)
    return render(request, "attractions/attractions_list.html", {"Attractions": attractions})


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


#def delete_comment(request, comment_id):
    #comment = Comments.objects.get(pk=comment_id)
   # comment.delete()
   # return redirect()

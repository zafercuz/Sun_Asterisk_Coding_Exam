from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from article.forms import ArticleForm
from article.models import Article


class ArticleListView(ListView):
    template_name = 'article_home.html'
    model = Article
    context_object_name = "articles"
    queryset = Article.objects.order_by('-created_date').all()


class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article
    context_object_name = "article"


class ArticleCreateView(SuccessMessageMixin, CreateView):
    template_name = "article_form.html"
    form_class = ArticleForm
    model = Article
    context_object_name = 'article'
    success_message = "Article successfully created!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['method'] = "POST"
        return context

    def get_success_url(self):
        return reverse('article_detail', args=[self.object.pk])


class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "article_form.html"
    form_class = ArticleForm
    model = Article
    context_object_name = 'article'
    success_message = "Article successfully updated!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['method'] = "PUT"
        return context

    def get_success_url(self):
        return reverse('article_detail', args=[self.object.pk])


class ArticleDeleteView(SuccessMessageMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    context_object_name = "article"
    success_message = "Article successfully deleted!"
    success_url = reverse_lazy('article_home')


def vote(request):
    id_pk = request.GET['id']
    type_vote = request.GET['vote']

    if type_vote == "up":
        obj = Article.objects.get(pk=id_pk)
        obj.votes = obj.votes + 1
        obj.save()
    elif type_vote == "down":
        obj = Article.objects.get(pk=id_pk)
        if obj.votes == 0:
            obj.votes = 0
        else:
            obj.votes = obj.votes - 1
        obj.save()

    return JsonResponse({"votes": obj.votes}, status=200, safe=False)

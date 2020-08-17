from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.utils import timezone
from django.contrib.postgres.search import SearchVector


from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.views.generic import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article, Category
from .models import Article, Category
from .forms import ArticleCreateForm, ArticleUpdateForm





import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_lists.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            Article.objects.select_related('author', "category")
            .prefetch_related("tags")
            .filter(published="P")
            .order_by("-date_added")
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by("title")
        context["latest_article"] = Article.objects.filter(published='P').order_by("-date_added")[:5]
        return context


class CategoryListView(ListView):
    model = Article
    context_object_name = "category_list"
    template_name = "articles/category_list.html"
    paginate_by = 10

    def get_queryset(self):
        articles = Article.objects.select_related("category", 'author').prefetch_related("tags")
        articles = articles.filter(category__title=self.kwargs["title"], published="P").order_by(
            "-date_added"
        )
        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = Article.objects.filter(published='P').order_by("-date_added")[:5]
        return context


class ArticleTagView(ListView):
    model = Article
    template_name = "tag.html"
    context_object_name = "article_tags"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.select_related('author', 'category').prefetch_related('tags').filter(tags__slug=self.kwargs["tag_slug"]).order_by(
            "-date_added"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = Article.objects.filter(published='P').order_by("-date_added")[:5]
        # context["tagged"] = (
        #     self.get_queryset()
        #     .filter(tags__slug__icontains=self.kwargs["tag_slug"])
        #     .only("tags__slug")
        #     .first()
        # )
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    query_pk_and_slug = True
    context_object_name = "article"


    def get_object(self):
        article = get_object_or_404(
            Article.objects.select_related("category", "author").prefetch_related(
                "tags"
            ),
            slug=self.kwargs.get("slug"),
            pk=self.kwargs.get("pk"),
        )
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # object_tags = self.get_object().tags.values_list('name', flat=True)
        # print(object_tags)
        # articles = Article.objects.select_related('author', 'category').prefetch_related('tags')
        # context['related_articles'] = articles.filter(published='P', tags__name__in=object_tags).distinct()[:3]
        return context


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = "articles/article_new.html"
    login_url = "login"
    redirect_field_name = "next"
    success_message = "Article created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = "articles/article_update.html"
    context_object_name = "article"
    login_url = "login"
    redirect_field_name = "next"
    query_pk_and_slug = True
    success_message = "Article updated successfully"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# LoginRequiredMixin
class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("articles:article_lists")
    login_url = "login"
    redirect_field_name = "next"
    context_object_name = "article"
    query_pk_and_slug = True
    success_message = "Article deleted successfully"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class SearchView(ListView):
    model = Article
    template_name = "search.html"
    context_object_name = 'search_list'

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is None:
            return None
        # search_articles = Article.objects.filter(
        #     Q(title__icontains=q) | Q(body__icontains=q)
        # )
        search_articles = Article.objects.annotate(
            search=SearchVector('title', 'body'),
        ).filter(search=q)
        return search_articles

    # def get(self, request, *args, **kwargs):
    #     articles = Article.objects.all()
    #     q = request.GET.get("q", None)
    #     if q is None:
    #         search_list = None
    #     elif not q:
    #         search_list = []
    #     else:
    #         search_list = articles.filter(Q(title__icontains=q) | Q(body__icontains=q))

    #     context = {"search_list": search_list}
    #     return render(request, "search.html", context)


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == "POST" and request.is_ajax():
        if "markdown-image-upload" in request.FILES:
            image = request.FILES["markdown-image-upload"]
            image_types = [
                "image/png",
                "image/jpg",
                "image/jpeg",
                "image/pjpeg",
                "image/gif",
            ]
            if image.content_type not in image_types:
                data = json.dumps(
                    {"status": 405, "error": _("Bad image format.")}, cls=LazyEncoder
                )
                return HttpResponse(data, content_type="application/json", status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps(
                    {
                        "status": 405,
                        "error": _("Maximum image file is %(size) MB.")
                        % {"size": to_MB},
                    },
                    cls=LazyEncoder,
                )
                return HttpResponse(data, content_type="application/json", status=405)

            img_uuid = "{0}-{1}".format(
                uuid.uuid4().hex[:10], image.name.replace(" ", "-")
            )
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(
                f"https://jokotoye-blog.s3.us-east-2.amazonaws.com{settings.MEDIA_URL}",
                def_path,
            )
            data = json.dumps({"status": 200, "link": img_url, "name": image.name})
            return HttpResponse(data, content_type="application/json")
        return HttpResponse(_("Invalid request!"))
    return HttpResponse(_("Invalid request!"))

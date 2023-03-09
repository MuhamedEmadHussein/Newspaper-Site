from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin)
# update the rest of our articles views since we don’t want a user to be able to create,
# read, update, or delete a message if they aren’t logged in
# Make sure that the mixin is to the left of CreateView so it will be read first.
# We want the CreateView to already know we intend to restrict access.

from django.views.generic import (ListView,DetailView,CreateView)
from django.views.generic.edit import (UpdateView,DeleteView,FormView)
from django.views.generic.detail import SingleObjectMixin
from django.views import View
# master class-based view upon which all the others classes are built
from .models import Article
from django.urls import reverse,reverse_lazy
from .forms import CommentForm

# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"
    #  ListView returns an object with <model_name>_list 
    #  that we can iterate over using a for loop.


#  separate the GET and POST variations into their own dedicated views.
#  We can then transform ArticleDetailView into a wrapper view that combines them. T
class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        # add information to a template by updating the context
        # context -> a dictionary object containing all the variable names
        #  and values available in our template
        context = super().get_context_data(**kwargs) # we pulled all existing information into the context by using super()
        context['form'] = CommentForm # we added the variable name form with the value of CommmentForm(),
        return context # return the updated context.
        # anything we want available in the template must be loaded 
        # from the beginning into the context

class CommentPost(SingleObjectMixin,FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # from SingleObjectMixin lets us grab the article pk from the URL
        return super().post(request, *args, **kwargs)
    
    # this will grab the 4 so that our comment is saved to the article with a pk of 4 
    # called when form validation has succeeded
    def form_valid(self, form) :
        #  Before we save our comment to the database
        #  we have to specify the article it belongs.
        comment = form.save(commit = False)
        comment.article = self.object 
        # associate the correct article with the form object then save
        comment.save()
        return super().form_valid(form)
    
    # called after the form data is saved
    def get_success_url(self):
        article = self.get_object() # lets us grab the article pk from the URL
        return reverse("article_detail",kwargs={"pk":article.pk})
        # redirect the user to the current page

class ArticleDetailView(LoginRequiredMixin,View):
   
    def get(self,request,*args,**kwargs):
        view = CommentGet.as_view()
        return view(request,*args,**kwargs)
        
    def post(self,request,*args,**kwargs):
        view = CommentPost.as_view()
        return view(request,*args,**kwargs)
   
class ArticleCreateView(LoginRequiredMixin,CreateView):
#  Make sure that the mixin is to the left of CreateView so it will be read first.
# We want the CreateView to already know we intend to restrict access.    
    model = Article
    template_name = "article_new.html"
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user # whoever is logged inand trying to make the change
        return super().form_valid(form)
        # author should be automatically set to the current logged-in user 
        # not any existing user

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ['title','body']
    def test_func(self):
        obj = self.get_object() # variable obj to the current object returned by the view using get_object()
        return obj.author == self.request.user # whoever is logged inand trying to make the change
        # if the author on the current object matches the current user on the webpage, allow it

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    def test_func(self):
        obj = self.get_object() # variable obj to the current object returned by the view using get_object()
        return obj.author == self.request.user # whoever is logged inand trying to make the change
        # if the author on the current object matches the current user on the webpage, allow it

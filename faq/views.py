from django.shortcuts import render
from .models import Question
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.
def faq_view(request):

    questions = Question.objects.all()
    
    context = {

        'objects':questions,
        

    }
    return render(request,'faq_view.html',context)



class SearchResultsView(ListView):
    model = Question
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Question.objects.filter(
            Q(question__icontains=query) 
        )
        return object_list
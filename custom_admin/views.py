from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from core.models import *
# Create your views here.
@staff_member_required
def my_view(request):
    """
    If you're using multiple admin sites with independent views you'll need to set
    current_app manually and use correct admin.site
    # request.current_app = 'admin'
    """
    # template = "scoreboard.html"
    context = admin.site.each_context(request)
    context.update(
        {
            "title": "Custom view",
        }
    )

    return render(request, template, context)

class Scoreboard(TemplateView):
    template_name = "scoreboard.html"
    model = Applicant

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        app = Applicant.objects.all()
        category = CompanyCategory.objects.all()
        print(category)
        context['category'] = category
        return self.render_to_response(context)
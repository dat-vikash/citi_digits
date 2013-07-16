from django.template.response import TemplateResponse

def index(request):
    """
     Loads base index
    """
    return TemplateResponse(request,'index.html')
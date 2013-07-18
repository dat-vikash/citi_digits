from django.template.response import TemplateResponse
import forms


def index(request):
    """
     Loads base index
    """
    return TemplateResponse(request,'index.html')

def signUp(request):
    """
      Sign up
    """
    #Process Registration information
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        #Load Sign up form
        form = forms.SignUpForm()
        return TemplateResponse(request,'signup.html',{'form':form})
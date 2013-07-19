from django.http import HttpResponse
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
        #bound the form
        form  = forms.SignUpForm(request.POST)
        if form.is_valid(): # All validation rules pass
            print("FORM VALID")
            return HttpResponse(200) # Redirect after POST
        else:
            print("FORM NOT VALID")
            for field in form.errors.keys():
                print "ValidationError: %s[%s] <- \"%s\" %s" % (
                    '',
                    field,
                    form.data[field],
                    form.errors[field].as_text()
                )
        pass
    elif request.method == 'GET':
        #Load Sign up form
        form = forms.SignUpForm()
        return TemplateResponse(request,'signup.html',{'form':form})
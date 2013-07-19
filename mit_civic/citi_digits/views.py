import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
import forms


def index(request):
    """
     Loads base index
    """
    return render_to_response('index.html', {},
                   context_instance=RequestContext(request))

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
            json_data = json.dumps({"HTTPRESPONSE":200})
            # json data is just a JSON string now.
            return HttpResponse(json_data, mimetype="application/json")
        else:
            print("FORM NOT VALID")
            for field in form.errors.keys():
                print "ValidationError: %s[%s] <- \"%s\" %s" % (
                    '',
                    field,
                    '',
                    form.errors[field].as_text()
                )
            return render_to_response('signup.html', {'form': form},
                   context_instance=RequestContext(request))
        pass
    elif request.method == 'GET':
        #Load Sign up form
        form = forms.SignUpForm()
        return render_to_response('signup.html', {'form': form},
                   context_instance=RequestContext(request))
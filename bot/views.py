from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import os
# Create your views here.from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bot import cc
import po
import aiml
import sys
import json

#from translate import Translator
from deep_translator import MyMemoryTranslator
from textblob import TextBlob
from langdetect import detect
# Create your views here.

def index(request):
    x= [1,2,3]
    output ='hello'

    return render(request,'bot/index.html',{'output':output})


def search_form(request):

  return render(request, 'bot/publisher.html')



def search(request):
    req=''
    pp=''
    ppp=''
    #print(request.GET['input'])
    if request.method == 'GET':
        req = request.GET['input']
        
        #pp="hii how r u"
        #xx = xx + "robo"
        print ('You: ',req)
        print('Bot: ',pp)
        #text=req
        text=req
        language=detect(text)
       # lang=TextBlob(text)
        #language=lang.detect_language()
        print(language)
        
        if language=='fi':
            pp = po.ab(str(req))
            ppp = MyMemoryTranslator(source="en", target="en").translate(text=pp)
            print(ppp)
        elif language=='te':
            old= MyMemoryTranslator(source="te", target="en").translate(text=req)
            pp= po.ab(str(old))
            ppp = MyMemoryTranslator(source="en", target="te").translate(text=pp)
        elif language=='ta':
            old= MyMemoryTranslator(source="ta", target="en").translate(text=req)
            pp= po.ab(str(old))
            ppp = MyMemoryTranslator(source="en", target="ta").translate(text=pp)
        elif language=='ml':
            old= MyMemoryTranslator(source="ml", target="en").translate(text=req)
            pp= po.ab(str(old))
            ppp = MyMemoryTranslator(source="en", target="ml").translate(text=pp)
        elif language=='kn':
            old= MyMemoryTranslator(source="kn", target="en").translate(text=req)
            pp= po.ab(str(old))
            ppp = MyMemoryTranslator(source="en", target="kn").translate(text=pp)
        elif language=='hi':
            old= MyMemoryTranslator(source="hi", target="en").translate(text=req)
            pp= po.ab(str(old))
            ppp = MyMemoryTranslator(source="en", target="hi").translate(text=pp)
        else:
            pp = po.ab(str(req))
            #ppp = MyMemoryTranslator(source="en", target="en").translate(text=pp)
            ppp=pp
            print(ppp)
       # res="""You: """+xx+"""\n\n"""+"""Bot: """+pp
        return HttpResponse('<b>You: ''</b>'+req+'<br><b>Bot: </b>'+ppp)


    else:
            message = 'You searched for: %s' % request.GET['q']
            xx=request.GET['q']
           # print xx

    #else:
       #  message = 'Form is not submitted properly.'


    print ("i am in search and my value is")
    print (xx)



    #pp="currently in testing mode"



    #y=request.GET['p']
   # return render(request,'../templates/'+y+'',{'message':pp})


# Create your views here.

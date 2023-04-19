from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import openai
# Create your views here.
def Index(request):
    # API = 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
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'html', 'javascript', 'markup','python']
    # print(sorted(lang_list))   
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        
        #make sure that they have used a programming language
        if lang=="Select a Programming Language":
            messages.success(request, "Pickup a Programming Language....")
            return render(request, 'website/home.html',{'lang_list': lang_list,'code':code,'lang':lang})
            
        else:
        
            # Setup OPENAI
            openai.api_key = "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"
            # create openai instance
            openai.Model.list()
            # Make openAI Request
            try:
                response = openai.Completion.create(
                    model = 'text-davinci-003',
                    prompt = f"Respond only with code. Fix this {lang} code: {code}",
                    temprature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty=0.0,
                    presence_penalty= 0.0,
                )

                #Parse the response
                response = (response["choices"][0]["text"]).strip()
                return render(request, 'website/home.html',{'lang_list': lang_list,'response':response,'lang':lang})


            except Exception as e:
                return render(request, 'website/home.html',{'lang_list': lang_list,'response':e,'lang':lang})
                



    return render(request, 'website/home.html',{'lang_list': lang_list})
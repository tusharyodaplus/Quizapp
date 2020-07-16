from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.urls import reverse
from django.http import HttpResponseRedirect 
from .models import Question,UserTracker,AccountData,QuizTaker,Quiz
#for login and logout feature
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#for rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import quizSerializer




class quizList(APIView):
    def get(self,request):
        quiz1=Quiz.objects.all()
        serializer= quizSerializer(quiz1, many=True)
        
        return Response(serializer.data)

    def post(self):
        pass

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request,user)
            s = SessionStore()
            s.create()
            a=s.session_key
            print (a)
            s = SessionStore(session_key='a')
            print (s)
            
            return HttpResponseRedirect(reverse('user_success'))

            
            
        else:
            context["error"] = "Provide valid credentials"
            return render(request,'quiz/login.html',context)
    else:
         return render(request,'quiz/login.html',context)
def success(request):
    context ={}
    context['user'] = request.user
    return render(request,'quiz/success.html',context)            
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))            
    
       




def about(request):
    return render(request,'quiz/about.html')

def contact(request):
    return render(request,'quiz/contact.html')
        
def home(request):
    choices = Question.CAT_CHOICES
    print(choices)
    return render(request,'quiz/home.html', {'choices':choices})

def questions(request , choice):
    print(choice)
    ques = Question.objects.filter(category__exact = choice)
    return render(request,'quiz/questions.html',{'ques':ques})

def result(request):
    print("result page")
    
    if request.method == 'POST':
        
        data = request.POST
        x=UserTracker.objects.create(data.user_answer)
        x.save()
        print (x)
        
        datas = dict(data)
        
        qid = []
        qans = []
        ans = []
        score = 0

        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        
        for q in qid:
            ans.append((Question.objects.get(id = q)).answer)
            print(ans)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score+=1
                
        print(score) 
            
                   
                      
    return render(request, 'quiz/result.html',{'score':score,'total':total})



#
#
#
#
#
#
#
    
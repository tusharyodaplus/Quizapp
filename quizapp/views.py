from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect 
from .models import Questions,UserTracker,account_data

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
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
        
def home(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,'quiz/home.html', {'choices':choices})

def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,'quiz/questions.html',{'ques':ques})

def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST

        datas = dict(data)
        qid = []
        qans = []
        ans = []
       
        ans1 = []
        a=[]
        dummy='Correct'
        dummy1='InCorrect'
        score = 0

        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        T1= UserTracker( user_answer=qans)
        T1.save()
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
            ans1.append((UserTracker.objects.get(id = q)).user_answer)
            print (ans1)
            print(ans)
            total = len(ans)
                 
                   
            for i in range(total):
                if ans[i] == ans1[i] :
                    print(dummy)
                
                else:
                    print(dummy1)        

            total = len(ans)
            for i in range(total):
            
                   if ans[i] == qans[i]:
                      score+=1
                      print(score)      
        
                    
 

def getSessionOrAccountData(request, key):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            record = account_data.objects.get(username=username, key=key)
            return record.value
        except:
            return None
    else:
        if key in request.session.keys():
            return request.session[key]
        else:
            return None

def setSessionOrAccountData(request, key, value):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            record = account_data.objects.get(username=username, key=key)
            record.value = value
            record.save()
        except account_data.DoesNotExist:
            record = account_data(username=username, key=key, value=str(value))
            record.save()
    else:
        request.session[key] = value

def deleteSessionOrAccountData(request, key):
    if request.user.is_authenticated():
        username = request.user.username
        account_data.objects.filter(username=username).filter(key=key).delete()
    else:
        del request.session[key]          
                   
            




           
           
                
        
            

        
            
        
        return render(request, 'quiz/result.html',{'score':score,'total':total})

def about(request):
    return render(request,'quiz/about.html')

def contact(request):
    return render(request,'quiz/contact.html')



#
#
#
#
#
#
#
    
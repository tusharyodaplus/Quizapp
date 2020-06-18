from django.shortcuts import render
from .models import Questions,UserTracker

# Create your views here.
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
        dummy='Correct'
        dummy1='InCorrect'
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
            ans1.append((UserTracker.objects.get(id = q)).user_answer)
            print (ans1)
            print(ans)
            if ans == ans1 :
                print(dummy)
            else:
                print(dummy1)

        total = len(ans)
        for i in range(total):
            
            if ans[i] == ans1[i]:
                score+=1
            
        
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
    
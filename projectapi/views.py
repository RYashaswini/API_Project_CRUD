
from urllib import response
from django.shortcuts import render,redirect
import requests



# Create your views here.


def index(request):
    return render(request,'index.html')

def create(request):

    if request.method == 'POST':
        print("-------------------POST--------------")
        title = request.POST['title']
        author = request.POST['author']
        email = request.POST['email']
        shipping = request.POST['shipping']
        journal = request.POST['journal']
        myimage = request.FILES.get('myimage')

        data = {'title': title, 'author' : author, 'email': email, 'shipping' : shipping, 'journal' : journal}
        file = {'myimage' : myimage}
        response = requests.post('http://127.0.0.1:8000/class_article/',data=data, files=file)
        print(response)
        print(response.text)
        return redirect('retrieve')
    print("-------------------POST refresh--------------")
    return render(request,'create.html')

     

def retrieve(request):
    print("-------------------list--------------")
    response = requests.get('http://127.0.0.1:8000/class_article/').json()
    print(response)
    return render(request,'retrieve.html',{'response' : response})






def updateobj(request,id):
    print("--------******************************************")
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        email = request.POST['email']
        shipping = request.POST['shipping']
        journal = request.POST['journal']
        myimage = request.FILES.get('myimage')


        data = {'title': title, 'author' : author, 'email': email, 'shipping' : shipping, 'journal' : journal}
        file = {'myimage' : myimage}
        print('************************************************')
        print('update data:', data, file)
        response = requests.put('http://127.0.0.1:8000/class_detail/{pk}/'.format(pk=id), data=data, files=file)
        print(response)
        print(response.text)
        return redirect('retrieve')
    #response = requests.get('http://127.0.0.1:8000/class_detail/{pk}/'.format(pk=id))
    #print(response)
    #print(response.text)
    return render(request,'update.html',{'response' : response})



def deleteobj(request,id):
    print("-------------------delete--------------")
    response = requests.delete('http://127.0.0.1:8000/class_detail/{pk}/'.format(pk=id))
    print(response.text)
    return redirect('retrieve')
    


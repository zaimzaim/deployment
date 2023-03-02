from django.shortcuts import render, redirect
from stock.models import Staff, Product, StocksManagement, AskQuestion
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.

#Login
def login(request):
    if request.method == 'GET':
        s_id = request.GET.get('staff_id')
        s_password = request.GET.get('password')
        staffdata=Staff.objects.filter(staffID=s_id, password=s_password).values()
        for idpass in staffdata:
            id = idpass['staffID']
            name = idpass['staffName']
            password = idpass['password']
            if s_password == '':
                print('error')
            elif s_id == id:
                if s_password == password:
                    request.session['staffID'] = id
                    request.session['staffName'] = name
                    dict = {
                        'staffname':name,
                        'staffid':id
                        }
                    return render(request, 'home.html',dict)
    return render(request, 'index.html')

#Sign Up
def sign_up(request):
   if request.method == 'POST':
        s_id = request.POST['s_id']
        s_name = request.POST['s_name']
        s_pass1 = request.POST['s_pass1']
        s_pass2 = request.POST['s_pass2']
        allstaff = Staff.objects.filter(staffID=s_id)
        print(allstaff)
        for data in allstaff:
            if data.staffID == s_id:
                print(data.staffID)
                if data.password == '':
                    if s_pass1 == s_pass2:
                            data = Staff(staffID=s_id, staffName=s_name, password=s_pass1)
                            data.save()
                            dict = {
                                'message':'Sign Up Success'
                            }
                else:
                    message = 'Account already exists'
                    dict = {
                        'message':message
                    }
                    return render (request, 'sign_up.html', dict)
        return render (request, 'sign_up.html', dict)
   else:
        return render (request, 'sign_up.html')

#Home
def home(request):
  if request.session.has_key('staffID'):
    s_name = request.session['staffName']
    s_id = request.session['staffID']
    dict = {
            'staffname':s_name,
            'staffid':s_id,
          }
    print(s_id)
    print(s_name)
    return render(request, 'home.html', dict)
  else:
    return render(request, 'index.html')
  
#Change Password
def change_password(request):
   if request.session.has_key('staffID'):
    s_name = request.session['staffName']
    s_id = request.session['staffID']
    dict = {
       'staffname':s_name,
       'staffid':s_id,
       }
    allstaff = Staff.objects.filter(staffID=s_id).values()
    print(allstaff)
    print(s_id)
    print(s_name)
    for data in allstaff:
        if data['staffID'] == s_id:
           if request.method == 'POST':
            c_password = request.POST['pass']
            n_password = request.POST['pass1']
            cn_password = request.POST['pass2']
            if data['password']==c_password:
                if n_password==cn_password:
                    Staff.objects.filter(password=c_password).update(password=n_password)
                    dict = {
                       'message':'Change Password Success'
                    }
        return render(request,'change_password.html', dict)
   else:
      return render(request,'change_password.html')

#-------------------------------------------------------------------------------------------------------------------------------------------------#

#Product List with Search by Category
def product_list(request):
    allproduct=Product.objects.all()
    dict={
                'allproduct': allproduct,
            }
    if request.method == 'GET':
        p_category = request.GET.get('p_category')
        if p_category == 'All':
            allproduct = Product.objects.all()
            print(allproduct)
            dict={
                'allproduct': allproduct,
            }
            return render (request,'product_list.html', dict)
        elif p_category != None:
            allproduct = Product.objects.filter(category=p_category)
            print(allproduct)
            dict={
                'allproduct': allproduct,
            }
            return render (request,'product_list.html', dict)
    return render (request,'product_list.html', dict)

#Add products in database.
def add_product(request):
    allproduct=Product.objects.all()
    if request.method == 'POST':
        p_id = request.POST['p_id']
        p_name = request.POST['p_name']
        p_category = request.POST['p_category']
        p_price = request.POST['p_price']
        find =0
        for search in allproduct:
            if search.productID == p_id:
                find =1

        if find ==0:
            data=Product(productID=p_id, productName=p_name, category=p_category, price=p_price)
            data.save()
            msg = "Data Save"
        else:
            msg = "Product already exist"

        dict = {
            'message': msg
        }
    else:
        dict = {
            'message':''
        }

    return render (request , "add_product.html", dict)

#Update Product List
def update_product(request,productID):
    data=Product.objects.get(productID=productID)
    dict = {
        'data':data
    }
    return render (request , "update_product.html", dict) 
   
def save_update_product(request,productID):
    p_name= request.POST['productName']
    p_category= request.POST['category']
    p_price = request.POST['price']
    data=Product.objects.get(productID=productID)
    data.productName = p_name
    data.category = p_category
    data.price = p_price
    data.save()
    return HttpResponseRedirect(reverse("product_list"))

#Delete Product from List
def delete_product(request,productID):
    data = Product.objects.get(productID=productID)
    data.delete()
    return HttpResponseRedirect(reverse('product_list'))

#-------------------------------------------------------------------------------------------------------------------------------------------------#

#Stock In/Out and Add/Minus quantity
def stock_in_out(request):
    if request.session.has_key('staffID'):
       s_id = request.session['staffID']
       data_s = Staff.objects.filter(staffID=s_id).values()
       print(data_s)
       data_p = Product.objects.all()
       print(data_p)
       print(s_id)
       dict = {
          'staffid':s_id,
          "product_id":data_p,
          "staff_id":data_s
          }
       allstock = StocksManagement.objects.all().values()
       print(allstock)
       if request.method == 'POST':
        s_id = request.POST.get('s_id')
        p_id = request.POST.get('p_id')
        date = request.POST.get('date')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        stock = StocksManagement(staffID_id=s_id, productID_id=p_id, date=date, quantity=quantity, status=status)
        stock.save()
        dict={
           'message':'Data saved'
        }
        afterstock = StocksManagement.objects.all().values()
        print(afterstock)
        pr_id = Product.objects.filter(productID=p_id)
        print(pr_id)
        for data in pr_id:
           totalQuantity = data.totalQuantity
           print(totalQuantity)
           if status == 'In':
              totQuantity = totalQuantity + int(quantity)
              print(totQuantity)
              Product.objects.filter(productID=p_id).update(totalQuantity = totQuantity)
           elif status == 'Out':
              totQuantity = totalQuantity - int(quantity)
              print(totQuantity)
              Product.objects.filter(productID=p_id).update(totalQuantity = totQuantity)
    return render(request, 'stock_in_out.html', dict)

#Stock In/Out History
def stock_in_out_history(request):
   if request.session.has_key('staffID'):
       s_id = request.session['staffID']
       s_name = request.session['staffName']
       data_history = StocksManagement.objects.all()
       print(data_history)
       dict = {
          'data_history': data_history,
          'staffname': s_name,
          'staffid': s_id
       }
       if request.method == 'GET':
        h_status = request.GET.get('h_status')
        if h_status == 'All':
            data_history = StocksManagement.objects.all()
            print(data_history)
            dict={
                'data_history': data_history,
                'staffname': s_name,
                'staffid': s_id
            }
            return render (request,'stock_in_out_history.html', dict)
        elif h_status != None:
            data_history = StocksManagement.objects.filter(status=h_status).values()
            print(data_history)
            dict={
                'data_history': data_history,
                'staffname': s_name,
                'staffid': s_id
            }
            return render (request,'stock_in_out_history.html', dict)
       return render(request, 'stock_in_out_history.html', dict)

#-------------------------------------------------------------------------------------------------------------------------------------------------#

#Asked Question List 
def asked_question(request):
    if request.session.has_key('staffID'):
       s_id = request.session['staffID']
       s_name = request.session['staffName']
       data_ask_question = AskQuestion.objects.filter(staffID=s_id).values()
       print(data_ask_question)
       allaskquestion=AskQuestion.objects.filter(~Q(answer='Pending')).values()
       dict = {
          'data_ask_question': data_ask_question,
          'staffname': s_name,
          'staffid': s_id,
          'allaskquestion': allaskquestion
       }
    return render(request, 'asked_question.html',dict)

#Add Question
def add_question(request):
    if request.session.has_key('staffID'):
        s_id = request.session['staffID']
        data_s = Staff.objects.filter(staffID=s_id).values()
        print(data_s)
        print(s_id)
        dict = {
            'staffid':s_id,
            "staff_id":data_s
            }
        if request.method == 'POST':
            question = request.POST.get('question')
            data = AskQuestion(staffID_id=s_id, question=question)
            data.save()
            dict = {
                'message':"Question Sent"
            }
        return render(request, 'add_question.html', dict)
    return render(request, 'add_question.html', dict)

def my_pending_question(request):
    if request.session.has_key('staffID'):
        s_id = request.session['staffID']
        data_s = Staff.objects.filter(staffID=s_id).values()
        print(data_s)
        print(s_id)
        allmyquestion = AskQuestion.objects.filter(staffID_id=s_id, answer='Pending').values()
        dict = {
            'staffid':s_id,
            'staff_id':data_s,
            'allmyquestion':allmyquestion
            }
        return render(request, 'my_pending_question.html', dict)
    return render(request, 'my_pending_question.html')

def delete_my_question(request):
    if request.session.has_key('staffID'):
        s_id = request.session['staffID']
        data = AskQuestion.objects.filter(staffID_id=s_id)
        data.delete()
        return HttpResponseRedirect(reverse('my_question'))
#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.db.models import Q
from misa.models import Member, Courserecord, News, Discussion, Jkuser, Jkmooc, Jkother, Jkcollection, Jkinterest
#from runningbear.forms import PhotoForm
import datetime
import json
import time
import random
import os
# Create your views here.

def home(request):
    return render_to_response('index.html')

def introduction(request):
    return render_to_response('Introduction.html')

def news(request):
    return render_to_response('News.html')

def resources(request):
    return render_to_response('Resources.html')

def sponsor(request):
    return render_to_response('Sponsor.html')

def loginpage(request):
    return render_to_response('Login.html')

def uploadpage(request):
    return render_to_response('Upload.html')

def jike_index(request):
    return render_to_response('jike_index.html')

def jike_login(request):
    return render_to_response('jike_login.html')

def jike_moocUpload(request):
    return render_to_response('jike_moocUpload.html')

def jike_otherUpload(request):
    return render_to_response('jike_otherUpload.html')

def jike_search(request):
    return render_to_response('jike_search.html')

def login(request):  #front end: username,password
    errors = []
    out_data = ''
    if request.method == 'POST':
        Username=request.POST.get('username')
        #phone_number = request.POST.get('phone', '')
        if not Username:
            errors.append('username post error')
        Password=request.POST.get('password')
        #password_md5 = request.POST.get('password', '')
        if not Password:
            errors.append("password post error")
        if len(errors) > 0:
            out_data = '0'
        login_usr = Member.objects.filter(name = Username)
        if len(login_usr) == 0:
            out_data = '0'
        else:
            login_usr_obj = login_usr[0]
            if login_usr_obj.password == Password:
                login_usr_obj.save()
                out_data = '1'
            else:
                out_data = '0'
    print(out_data)
    return HttpResponse(out_data)

def userlogin(request):
    errors = []
    out_data = ''
    if request.method == 'POST':
        Username=request.POST.get('username')
        #phone_number = request.POST.get('phone', '')
        if not Username:
            errors.append('username post error')
        Password=request.POST.get('password')
        #password_md5 = request.POST.get('password', '')
        if not Password:
            errors.append("password post error")
        if len(errors) > 0:
            out_data = '0'
        login_usr = Jkuser.objects.filter(username = Username)
        if len(login_usr) == 0:
            out_data = '0'
        else:
            login_usr_obj = login_usr[0]
            if login_usr_obj.password == Password:
                login_usr_obj.save()
                out_data = '1'
            else:
                out_data = '0'
    print(out_data)
    return HttpResponse(out_data)


def register(request): #front end: username, password, email
    out_data = ''
    errors = []
    if request.method == 'POST':
        Username = request.POST.get('username')
        if not Username:
            errors.append('username post error')
        Email=request.POST.get('email')
        if not Email:
            errors.append("email post error")
        Password = request.POST.get('password')
        if not Password:
            errors.append("password post error")
        if len(errors) > 0:
            out_data = '0'
        register_user = Member.objects.filter(name = Username)
        if len(register_user) != 0:
            print ('user existed')
            out_data = '2'
        else:
            new_user = Member(name = Username, password = Password, email = Email)
            new_user.save()
            out_data = '1'
    return HttpResponse(out_data)

def userregister(request): #front end: username, password, email, phone
    out_data = ''
    errors = []
    if request.method == 'POST':
        print("zongzongzong!")
        Username = request.POST.get('username')
        if not Username:
            errors.append('username post error')
        Email=request.POST.get('email')
        if not Email:
            errors.append("email post error")
        Phone=request.POST.get('phone')
        if not Phone:
            errors.append("phone post error")
        Password = request.POST.get('password')
        if not Password:
            errors.append("password post error")
        print(Username, Email, Phone, Password)
        if len(errors) > 0:
            out_data = '0'
        register_user = Jkuser.objects.filter(username = Username)
        if len(register_user) != 0:
            print ('user existed')
            out_data = '2'
        else:
            new_user = Jkuser(username = Username, password = Password, email = Email, phone = Phone)
            new_user.save()
            out_data = '1'
    return HttpResponse(out_data)

def up(request):
    out_data = {}
    if request.method == 'POST':
        print("zongzongzong!")
        CID = request.POST.get('cID',None)
        CNAME = request.POST.get('cname',None)
        UPLOADER = request.POST.get('uploader', None)
        FILE = request.FILES.get('file',None)
        print(CID, CNAME, UPLOADER)
        if not FILE:
            out_data['ret']='0'
        else:
#            os.mknod(os.path.join("/root/rb_server/server/static/resource/",FILE.name)
            destination = open(os.path.join("/root/rb_server/server/static/resource/",FILE.name),'wb+')
            for chunk in FILE.chunks():
                destination.write(chunk)
            destination.close()
            now = datetime.datetime.now()
            x=now.strftime('%Y-%m-%d %H:%M:%S')
            new_upload = Courserecord(cID=CID, cName=CNAME, uploadername=UPLOADER, fileAddress="http://123.56.26.95/static/resource/"+FILE.name,uploadTime=x)
            new_upload.save()
            out_data['ret']='1'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def otherupload(request):
    out_data = {}
    if request.method == 'POST':
        print("zongzongzong!")
        CID = request.POST.get('cID',None)
        CNAME = request.POST.get('cname',None)
        UPLOADER = request.POST.get('uploader', None)
        LINK = request.POST.get('link',None)
        INTRODUCTION = request.POST.get('introduction',None)
        FILE = request.FILES.get('file',None)
        print(CID, CNAME, UPLOADER)
        if not CID:
            out_data['ret']='0'
        if not CNAME:
            out_data['ret']='0'
        else:
#            os.mknod(os.path.join("/root/rb_server/server/static/resource/",FILE.name)
            destination = open(os.path.join("/root/rb_server/server/static/resource/",FILE.name),'wb+')
            for chunk in FILE.chunks():
                destination.write(chunk)
            destination.close()
            now = datetime.datetime.now()
            x=now.strftime('%Y-%m-%d %H:%M:%S')
            new_upload = Jkother(typeID=CID, name=CNAME, content=INTRODUCTION, link=LINK, uploader=UPLOADER, fileAddress="http://123.56.26.95/static/resource/"+FILE.name,uploadtime=x)
            new_upload.save()
            out_data['ret']='1'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def moocupload(request):
    out_data = {}
    if request.method == 'POST':
        print("zongzongzong!")
        CID = request.POST.get('cID',None)
        CNAME = request.POST.get('cname',None)
        LINK = request.POST.get('link',None)
        SCHOOL = request.POST.get('school',None)
        TEACHER = request.POST.get('teacher',None)
        INTRODUCTION = request.POST.get('introduction',None)
        UPLOADER = request.POST.get('uploader', None)
        print(CID, CNAME, UPLOADER)
        if not CNAME:
            out_data['ret']='0'
        if not CID:
            out_data['ret']='0'
        if not LINK:
            out_data['ret']='0'
        else:
            now = datetime.datetime.now()
            x=now.strftime('%Y-%m-%d %H:%M:%S')
            new_upload = Jkmooc(typeID=CID, name=CNAME, school=SCHOOL, teacher=TEACHER, content=INTRODUCTION, link=LINK, uploader=UPLOADER, uploadtime=x, clicktime=0)
            new_upload.save()
            out_data['ret']='1'
    return HttpResponse(json.dumps(out_data), content_type="application/json")
	
def register21(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone=dict['phone']
        #phone_number = request.POST.get('phone', '')
        if not Phone:
            errors.append('phone number post error')
        PhotoID = dict['photoID']
        if not PhotoID:
            errors.append("photoID post error")
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
        register_user = User.objects.get(phone = Phone)
        register_user.photoID = PhotoID
        register_user.save()
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")	
	
def register22(request):  #front end:phone_number, photoID, username, localPermission, signature, gender
    out_data = {}
    errors = []
    print(request.body)
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone=dict['phone']
        #phone_number = request.POST.get('phone', '')
        if not Phone:
            errors.append('phone number post error')
        # PhotoID = dict['photoID']
        # if not photoID:
            # errors.append("photoID post error")
        Username=dict['username']
        #userName = request.POST['username']
        if not Username:
            errors.append("username post error")
        LocalPermission=dict['localPermission']
        #localPermission = request.POST['localPermission']
        if not LocalPermission:
            errors.append("localPermission post error")
        Signature=dict['signature']
        #signature = request.POST['signature']
        if not Signature:
            errors.append("signature post error")
        Gender=dict['gender']
        #gender = request.POST.get['username']
        if not Gender:
            errors.append("gender post error")
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
        register_user = User.objects.get(phone = Phone)
        register_user.username = Username
        register_user.localPermission = LocalPermission
        register_user.signature = Signature
        register_user.gender = Gender
        register_user.save()
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def forgetpassword(request):  #phone,password
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone=dict['phone']
        #phone_number = request.POST.get('phone', '')
        if not Phone:
            errors.append('phone number post error')
        Password=dict['password']
        #password_md5 = request.POST.get('password', '')
        if not Password:
            errors.append("password post error")
        if len(errors) > 0:
            out_data['ret'] = 'phone_invalid'
        register_user = User.objects.filter(phone = Phone)
        if len(register_user) == 0:
            print ('user not exist')
            out_data['ret'] = 'phone_invalid'
        else:
            register_user[0].password = Password
            register_user[0].save()
            out_data['ret'] = 'phone_valid'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def runworld(request): #from front end: phone
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone = dict['phone']
        if not Phone:
            errors.append('phone number post error')
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        register_user = User.objects.filter(phone = Phone)
        if len(register_user) == 0:
            print ('user not exist')
            out_list = '[user not exist]'
        else:
            if dict['appointmentRunType'] == 'unDo':
                out_list = serializers.serialize("json", AppointmentToDo.objects.filter(phone = Phone)) # 数据量大时可加约束条件，只返回最近几天的
            if dict['appointmentRunType'] == 'sendToMe':
                out_list = serializers.serialize("json", AppointmentToMe.objects.filter(phone = Phone))
            if dict['appointmentRunType'] == 'sendByMe':
                out_list = serializers.serialize("json", AppointmentByMe.objects.filter(phone = Phone))
    return HttpResponse(out_list, content_type="application/json")

# def logout(request): 
    # out_data = {}
    # if request.method == "POST":
        # if 'user' in request.session:
            # user_name = request.session['user']
            # del request.session['user']
            # out_data['ret'] = 'ok'
        # else:
            # out_data['ret'] = "logout_session_failed"
    # else:
        # out_data["ret"] = "logout_failed"
    # return HttpResponse(json.dumps(out_data), content_type="application/json")

        # out_data["ret"] = "logout_failed"


def setAppointmentRun(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        print(dict)
        Phone = dict['phone']
        if not Phone:
            errors.append('phone number post error')
        Topic = dict['topic']
        if not Topic:
            errors.append('topic post error')
        Description = dict['description']
        if not Description:
            errors.append('description post error')
        Date = dict['date']
        if not Date:
            errors.append('date post error')
        BeginTime =  dict['beginTime']
        if not BeginTime:
            errors.append('beginTime post error')
        EndTime = dict['endTime']
        if not EndTime:
            errors.append('endTime post error')
        Length = dict['length']
        if not Length:
            errors.append('length post error')
        Place = dict['place']
        if not Place:
            errors.append('place post error')
        #Selection = dict['selection']
        #if not selection:
        #    errors.append('selection post error')
        target = dict['target']
        if not target:
            errrors.append('target post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        #setid = appointmentrun.id
        you = User.objects.get(phone=Phone)
        print(type(target))
        print(dict)
        appointmentbyme=AppointmentByMe(phone=Phone, description = Description, topic = Topic, beginTime = datetime.datetime.strptime((Date + ' ' + BeginTime), "%Y-%m-%d %H:%M:%S"), endTime = datetime.datetime.strptime((Date + ' ' + EndTime), "%Y-%m-%d %H:%M:%S"), length = float(Length), place = Place)
        appointmentbyme.save()
        if target == 1:
            appointmentrun = AppointmentRun(phone=Phone, description = Description, topic = Topic, beginTime = datetime.datetime.strptime((Date + ' ' + BeginTime), "%Y-%m-%d %H:%M:%S"), endTime = datetime.datetime.strptime((Date + ' ' + EndTime), "%Y-%m-%d %H:%M:%S"), length = float(Length), place = Place)
            appointmentrun.save()
            out_data['ret'] = '1'
        if target == 2:
            print('type 2')
            allUser = User.objects.all().exclude(phone = Phone)
            print(len(allUser))
            out_list = [user for user in allUser if ((user.logoninLongitude - you.logoninLongitude) **2 + (user.logoninLatitude - you.logoninLatitude) **2 ) <= 1]
            print(len(out_list))
            for i in range(0, len(out_list)):
                aptome= AppointmentToMe(phone=out_list[i].phone, description = Description, topic = Topic, beginTime = datetime.datetime.strptime((Date + ' ' + BeginTime), "%Y-%m-%d %H:%M:%S"), endTime = datetime.datetime.strptime((Date + ' ' + EndTime), "%Y-%m-%d %H:%M:%S"), length = float(Length), place = Place)
                aptome.save()
            out_data['ret']='2'
        if target == 3:
            friendlist = dict['selectFriend']
            for i in range(0, len(friendlist)):
                aptome = AppointmentToMe(phone=friendlist[i], description = Description, topic = Topic, beginTime = datetime.datetime.strptime((Date + ' ' + BeginTime), "%Y-%m-%d %H:%M:%S"), endTime = datetime.datetime.strptime((Date + ' ' + EndTime), "%Y-%m-%d %H:%M:%S"), length = float(Length), place = Place)
                aptome.save()
            out_data['ret'] = '3'
    return HttpResponse(json.dumps(out_data), content_type="application/json")


def run(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone = dict['phone']
        if not Phone:
            errors.append('phone number post error')
        distance =  dict['distance']
        if not distance:
            errors.append('distance post error')
        time =  dict['time']
        if not time:
            errors.append('time post error')
        score = dict['score']
        if not score:
            errors.append('score post error')
        speed = dict['speed']
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        user = User.objects.filter(phone = Phone)
        bgt = str(datetime.datetime.today())
        bgt = bgt[0:-7]
        runrec = MyRun(phone=Phone, length=distance, timeLength=time, averageVelocity = speed, beginTime=bgt)
        if len(user) == 0:
            print ('user not exist')
            out_data['ret'] = 'user not exist'
        else:
            user = user[0]
            user.score = score
            user.save()
            runrec.save()
            out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")


def Farest(request):
    out_list = []
    alluser = Member.objects.all()
    alluser = alluser.order_by("-id")
    out_list = serializers.serialize("json", alluser)
    #print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def search(request):
    errors = []
    out_list = []
    if request.method == 'POST':
        CID=request.POST.get('cID',None)      
        if not CID:
            errors.append('cID post error')
        
        allcourse = Courserecord.objects.filter(cID=CID)
        allcourse = allcourse.order_by("-cID")
        out_list = serializers.serialize("json", allcourse)
        print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def mooclist(request):
    errors = []
    out_list = []
    if request.method == 'POST':
        CID=request.POST.get('cID',None)      
        if not CID:
            errors.append('cID post error')
        if CID=='000':
            allcourse = Jkmooc.objects.order_by('clicktime')[:6]
        else:
            allcourse = Jkmooc.objects.filter(typeID=CID)
            allcourse = allcourse.order_by('clicktime')[:6]
        out_list = serializers.serialize("json", allcourse)
        print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def resourcelist(request):
    errors = []
    out_list = []
    if request.method == 'POST':
        allcourse = Jkother.objects.order_by('clicktime')[:5]
        out_list = serializers.serialize("json", allcourse)
        print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def keysearch(request):
    errors = []
    out_list = []
    if request.method == 'POST':
        CID=request.POST.get('cID',None)     
        KEY=request.POST.get('keyword',None) 
        print(CID,KEY)
        if not CID:
            errors.append('cID post error')
        if not KEY:
            errors.append('key post error')
        if CID=='201':
            result = Jkmooc.objects.filter(name__contains=KEY)
        elif CID=='202':
            result = Jkmooc.objects.filter(school__contains=KEY)
        elif CID=='203':
            result = Jkmooc.objects.filter(teacher__contains=KEY)
        elif CID=='204':
            result = Jkother.objects.filter(name__contains=KEY)
        out_list = serializers.serialize("json", result)
        print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def typesearch(request):
    errors = []
    out_list = []
    if request.method == 'POST':
        CID=request.POST.get('cID',None)
        RID=request.POST.get('rID',None)
        if not CID:
            errors.append('cID post error')
        if not RID:
            errors.append('rID post error')
        if RID=='301':
            result = Jkmooc.objects.filter(typeID=CID)
        elif RID=='302':
            result = Jkother.objects.filter(typeID=CID)
        out_list = serializers.serialize("json", result)
        print(out_list)
    #print(type(out_list))
    return HttpResponse(out_list, content_type="application/json")

def public(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        dateRange = dict['dateRange']
        if not dateRange:
            errors.append('date post error')
        BeginTime = dict['beginTime']
        if not BeginTime:
            errors.append('beginTime post error')
        #endTime = dict['endTime']
        #if not endTime:
        #    errors.append('endTime post error')
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        begin = datetime.datetime.today()
        end1 = str(datetime.datetime.today())
        end2 = str(datetime.datetime.today()+datetime.timedelta(days=1))
        end3 = str(datetime.datetime.today()+datetime.timedelta(days=2))
        end4 = str(datetime.datetime.today()+datetime.timedelta(days=3))
        end5 = str(datetime.datetime.today()+datetime.timedelta(days=4))
        end6 = str(datetime.datetime.today()+datetime.timedelta(days=5))
        end7 = str(datetime.datetime.today()+datetime.timedelta(days=6))
        if dateRange == '1天内':
            out_list = serializers.serialize("json", AppointmentRun.objects.filter(Q(beginTime__startswith=end1[0:10])|Q(beginTime__startswith=end2[0:10])))
            return HttpResponse(out_list, content_type="application/json")
        elif dateRange == '3天内':
            out_list = serializers.serialize("json", AppointmentRun.objects.filter(Q(beginTime__startswith=end1[0:10])|Q(beginTime__startswith=end2[0:10])|Q(beginTime__startswith=end3[0:10])))
            return HttpResponse(out_list, content_type="application/json")
        elif dateRange == '5天内':
            out_list = serializers.serialize("json", AppointmentRun.objects.filter(Q(beginTime__startswith=end1[0:10])|Q(beginTime__startswith=end2[0:10])|Q(beginTime__startswith=end3[0:10])|Q(beginTime__startswith=end4[0:10])|Q(beginTime__startswith=end5[0:10])))
            return HttpResponse(out_list, content_type="application/json")
        #if dateRange == '一周内':
        out_list = serializers.serialize("json", AppointmentRun.objects.filter(Q(beginTime__startswith=end1[0:10])|Q(beginTime__startswith=end2[0:10])|Q(beginTime__startswith=end3[0:10])|Q(beginTime__startswith=end4[0:10])|Q(beginTime__startswith=end5[0:10])|Q(beginTime__startswith=end6[0:10])|Q(beginTime__startswith=end7[0:10])))
    #x=out_list[0]
    #y=x['fields']
    #z=y['id']
    #print(y,z)
    return HttpResponse(out_list, content_type="application/json")



def publicd(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        print('zzzzz',dict)
        id = dict['appointmentRunID']
        #print(id)
        if not id:
            errors.append('id post error')
        phone = dict['phone']
        #print(phone)
        if not phone:
            errors.append('phone post error')
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        ap = AppointmentRun.objects.filter(id = id)
        #print(len(ap))
        if len(ap) == 0:
            out_data['ret'] = 'Failed'
        else:
            ap_obj = ap[0]
            atm = AppointmentToDo(beginTime = ap_obj.beginTime, endTime = ap_obj.endTime, description = ap_obj.description, topic = ap_obj.topic, phone = phone, due = ap_obj.due, length = ap_obj.length, place = ap_obj.place)
            atm.save()
            #print(phone)
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def sendtodo(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        print('zzzzz',dict)
        id = dict['appointmentRunID']
        #print(id)
        if not id:
            errors.append('id post error')
        phone = dict['phone']
        #print(phone)
        if not phone:
            errors.append('phone post error')
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        ap = AppointmentToMe.objects.filter(id = id)
        #print(len(ap))
        if len(ap) == 0:
            out_data['ret'] = 'Failed'
        else:
            ap_obj = ap[0]
            atm = AppointmentToDo(beginTime = ap_obj.beginTime, endTime = ap_obj.endTime, description = ap_obj.description, topic = ap_obj.topic, phone = phone, due = ap_obj.due, length = ap_obj.length, place = ap_obj.place)
            atm.save()
            #print(phone)
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")

def Mine(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        Phone = dict['phone']
        if not Phone:
            errors.append('phone post error')
        if len(errors) > 0:
            out_data['ret'] = 'Failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        user = User.objects.get(phone = Phone)
        out_data['username']=user.username;
        out_data['score']=user.score;
        out_data['credit']=user.credit;
        out_data['photoID']=user.photoID;
        out_data['count']=getCount(Phone);
        out_data['totalTime']=getTotalTime(Phone);
        out_data['avgSpeed']=getAvgSpeed(Phone);
    return HttpResponse(json.dumps(out_data), content_type="application/json")


def addFriends(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        print(dict)
        Phone = dict['phone']
        if not Phone:
            errors.append('phone post error')
        Gender =  dict['gender']
        if not Gender:
            errors.append('gender post error')
        Score = dict['score']
        if not Score:
            errors.append('score post error')
        Credit =  dict['credit']
        if not Credit:
            errors.append('credit post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        if Score=='100以下':
            if  Credit=='50%以下':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt=100,credit__lt=0.5))
            elif Credit=='50%-70%':
                #out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt 100,credit__gte 0.5,credit__lt 0.7))
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt=100,credit__gte=0.5).filter(credit__lt=0.7))
            elif Credit=='70%-90%':
                #out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt 100,credit__gte 0.7,credit__lt 0.9))
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt=100,credit__gte=0.7).filter(credit__lt=0.9))
            else:
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__lt=100,credit__gte=0.9))
        elif Score=='100-200':
            if  Credit=='50%以下':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=100,credit__lt=0.5).filter(score__lt=200))
            elif Credit=='50%-70%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=100,credit__gte=0.5).filter(score__lt=200,credit__lt=0.7))
            elif Credit=='70%-90%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=100,credit__gte=0.7).filter(score__lt=200,credit__lt=0.9))
            else:
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=100,credit__gte=0.9).filter(score__lt=200))
        elif Score=='200-300':
            if  Credit=='50%以下':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=200,credit__lt=0.5).filter(score__lt=300))
            elif Credit=='50%-70%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=200,credit__gte=0.5).filter(score__lt=300,credit__lt=0.7))
            elif Credit=='70%-90%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=200,credit__gte=0.7).filter(score__lt=300,credit__lt=0.9))
            else:
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gt=200,credit__gte=0.9).filter(score__lt=300))
        else:
            if  Credit=='50%以下':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=300,credit__lt=0.5))
            elif Credit=='50%-70%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=300,credit__gte=0.5).filter(credit__lt=0.7))
            elif Credit=='70%-90%':
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=300,credit__gte=0.7).filter(credit__lt=0.9))
            else:
                out_list=serializers.serialize("json", User.objects.filter(gender=Gender,score__gte=300,credit__gte=0.9))
    return HttpResponse(out_list, content_type="application/json")


def addFriends2(request):
    out_data = {}
    errors = []
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        Sendphone=dict['sendphone']
        if not Sendphone:
            errors.append('sendphone post error')
        Acceptphone=dict['acceptphone']
        if not Acceptphone:
            errors.append('acceptphone post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        user1 = User.objects.filter(phone = Sendphone)
        user2 = User.objects.filter(phone = Acceptphone)
        if len(user1) == 0:
            print ('user1 not exist')
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        if len(user2) == 0:
            print ('user2 not exist')
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        Sendusername=user1[0].username
        Acceptusername=user2[0].username
        friendship=Friendship(friendshiptoken=False,sendphone=Sendphone,sendusername=Sendusername,acceptphone=Acceptphone,acceptusername=Acceptusername)
        friendship.save()
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")



def addFriends3(request):
    out_data = {}
    errors = []
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        print(dict)
        Acceptphone=dict['acceptphone']
        if not Acceptphone:
            errors.append('phone post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        out_list=serializers.serialize("json", Friendship.objects.filter(friendshiptoken=False,acceptphone=Acceptphone))
        return HttpResponse(out_list, content_type="application/json")


def addFriends4(request):
    out_data = {}
    errors = []
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        Sendphone=dict['sendphone']
        if not Sendphone:
            errors.append('sendphone post error')
        Acceptphone=dict['acceptphone']
        if not Acceptphone:
            errors.append('acceptphone post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        user1 = User.objects.filter(phone = Sendphone)
        user2 = User.objects.filter(phone = Acceptphone)
        if len(user1) == 0:
            print ('user1 not exist')
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        if len(user2) == 0:
            print ('user2 not exist')
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        fr = Friendship.objects.filter(sendphone=Sendphone, acceptphone=Acceptphone)
        p=fr[0]
        p.friendshiptoken=True
        p.save()
        print(fr[0].sendusername,fr[0].acceptusername,fr[0].friendshiptoken)
        Sendusername=user1[0].username
        Acceptusername=user2[0].username
        friendship=Friendship(friendshiptoken=True,sendphone=Acceptphone,sendusername=Acceptusername,acceptphone=Sendphone,acceptusername=Sendusername)
        friendship.save()
        out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")


def resetPassword(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        phone_number = dict['phone']
        if not phone_number:
            errors.append('phone number post error')
        password1=dict['oldPassword']
        if not password1:
            errors.append("password1 post error")
        password2 =dict['newPassword']
        if not password2:
            errors.append("password2 post error")
        if len(errors) > 0:
            out_data['ret'] = 'phone_invalid'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        register_user = User.objects.filter(phone = phone_number)
        if len(register_user) == 0:
            print ('user not exist')
            out_data['ret'] = 'phone_invalid'
        else:
            user = register_user[0]
            if user.password == password1:
                user.password = password2
                user.save()
                out_data['ret'] = 'phone_valid'
            else:
                out_data['ret'] = 'PasswordError'
    return HttpResponse(json.dumps(out_data), content_type="application/json")
    
'''def dateInfo(request):
    out_data={}
    errors=[]
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        if request.method == 'POST':
            dict=json.loads(request.body.decode())
            Phone=dict['phone']
        if not Phone:
            errors.append('phone number post error')
            photoID = request.FILES['photoID']
        if not photoID:
            errors.append("photoID post error")
            userName=dict['username']
        if not userName:
            errors.append("username post error")
            localPermission=dict['localPermission']
        if not localPermission:
            errors.append("localPermission post error")
            signature=dict['signature']
        if not signature:
            errors.append("signature post error")
            gender=dict['gender']
        if not gender:
            errors.append("gender post error")
        if len(errors) > 0:
            out_data['ret'] = 'failed'
        update_user = User.objects.filter(phone = Phone)
        if len(update_user) == 0:
            print ('user existed')
            out_data['ret'] = 'user_existed'
        else:
            update_user = User(phone = Phone, photoID = photoID, username = userName, localPermission = localPermission, signature = signature, gender = gender)
            update_user.save()
            out_data['ret'] = 'succeed'
    return HttpResponse(json.dumps(out_data), content_type="application/json")'''

def update(request):
    out_data={}
    errors=[]
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        print(dict)
        phone_number = dict['phone']
        if not phone_number:
            errors.append('phone number post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        user=User.objects.filter(phone=phone_number)
        if len(user)==0:
            print ('user not exist')
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        else:
            userneed=user[0]
            out_data['username']=userneed.username
            out_data['signature']=userneed.signature
    return HttpResponse(json.dumps(out_data), content_type="application/json")   
            

def MyFriends(request):
    out_data = {}
    errors = []
    if request.method == 'POST':
        dict=json.loads(request.body.decode())
        print(dict)
        phone_number = dict['phone']
        if not phone_number:
            errors.append('phone number post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        friends=Friendship.objects.filter(friendshiptoken=True,sendphone=phone_number)
        if len(friends)==0:
            print('friends not exist')
            out_list=['failed']
        else:
            out_list=serializers.serialize('json',friends)
        return HttpResponse(out_list, content_type="application/json")

def RunRecord(request):
    out_data={}
    errors=[]
    if request.method=='POST':
        dict=json.loads(request.body.decode())
        phone_number=dict['phone']
        if not phone_number:
            errors.append('phone number post error')
        if len(errors) > 0:
            out_data['ret'] = 'failed'
            return HttpResponse(json.dumps(out_data), content_type="application/json")
        out_list=serializers.serialize("json", MyRun.objects.filter(phone=phone_number))
    return HttpResponse(out_list, content_type="application/json")

def getCount(Phone):
    user = MyRun.objects.filter(phone=Phone)
    return len(user)
    
def getTotalTime(Phone):
    user = MyRun.objects.filter(phone=Phone)
    x = 0
    for i in range(0,len(user)):
        x = x+user[i].timeLength
    return x

def getAvgSpeed(Phone):
    user = MyRun.objects.filter(phone=Phone)
    x = 0
    for i in range(0,len(user)):
    #    if !user[i].averageVelocity:
            x = x+user[i].averageVelocity
    if len(user)!=0:
        v = x/len(user)
        v=round(v,1)
    else:
        v=0
    return v

def track(request):
    out_data = {}
    if request.method == 'GET':
        username = request.GET.get('username')
        x = request.GET.get('x')
        y = request.GET.get('y')
        speed = request.GET.get('speed')
        print('\033[1;32;40m')
        print(username, 'is in', x, ',', y, 'with speed', speed, 'm/s')
        print('\033[0m')
    return HttpResponse(json.dumps(out_data), content_type="application/json")
        


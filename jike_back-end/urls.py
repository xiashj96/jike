from django.conf.urls import include, url
from django.contrib import admin
import settings
from misa import views as rb_views
from misa.views import login, register, register21
from misa.views import register22
from misa.views import run, Farest, public, publicd, Mine, resetPassword
from misa.views import search, up
from misa.views import userregister, otherupload, moocupload, userlogin, mooclist, resourcelist, keysearch, typesearch
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', rb_views.home, name='Home'),
    url(r'^Introduction/', rb_views.introduction),
    url(r'^News/', rb_views.news),
    url(r'^Resources/', rb_views.resources),
    url(r'^Sponsor/', rb_views.sponsor),
    url(r'^Login/',rb_views.loginpage),
    url(r'^Upload/',rb_views.uploadpage),
    url(r'^jike_index/',rb_views.jike_index),
    url(r'^jike_login/',rb_views.jike_login),
    url(r'^jike_moocUpload/',rb_views.jike_moocUpload),
    url(r'^jike_otherUpload/',rb_views.jike_otherUpload),
    url(r'^jike_search/',rb_views.jike_search),
    url(r'^jike_login/',rb_views.jike_login),
    url(r'^userlogin/', userlogin),
    url(r'^up', up),
    url(r'^search', search),
#    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),   # database admin
    url(r'^log/', login),                       # user login
    url(r'^register/', register),            # user register
    url(r'^userregister/', userregister),
    url(r'^register21/', register21),
    url(r'^register22/', register22),
    url(r'^otherupload/', otherupload),
    url(r'^moocupload/', moocupload),
    url(r'^mooclist/',mooclist),
    url(r'^resourcelist/',resourcelist),
    url(r'^keysearch/',keysearch),
    url(r'^typesearch/',typesearch),
#    url(r'^forgetpassword/', forgetpassword),
#    url(r'^runworld/', runworld),
 #   url(r'^setappointmentrun/', setAppointmentRun),
 #   url(r'^run/', run),
    url(r'^farest/', Farest),
#    url(r'^public/', public),
#    url(r'^public2/', publicd),
    url(r'^mine/', Mine),
#    url(r'^addfriends/', addFriends),
#    url(r'^addfriends2/', addFriends2),
#    url(r'^addfriends3/', addFriends3),
#    url(r'^addfriends4/', addFriends4),
    url(r'^resetPassword/', resetPassword),
#    url(r'^updateinfo/', update),
#    url(r'^myfriends/', MyFriends),
#    url(r'^getcount/', getCount),
#    url(r'^getTotalTime/', getTotalTime),
#    url(r'^getAvgSpeed/', getAvgSpeed),
#    url(r'^run/',run),
#    url(r'^sendtodo/',sendtodo),
#    url(r'^runrecord/', RunRecord),
#    url(r'^track/', track),

#    url(r'^setappointmentrun/', setAppointmentRun),
]


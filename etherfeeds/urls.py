from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.shortcuts import render, redirect


from . import views
app_name = 'etherfeeds'
def auto_login(request):
	if not request.user.is_authenticated:
		return render(request, 'web3auth/autologin.html')
	else:
		return redirect('/etherfeeds/dashboard/')
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^auto_login/', auto_login, name='auto_login'),
	url(r'dashboard/',views.dashboard,name='dashboard'),
	url(r'logout/',views.logout,name='logout'),
	url(r'listMembers/',views.listMembers,name='listMembers'),
	url(r'createpoll/',views.createpoll,name='createpoll'),
	url(r'memberProposal/',views.memberProposal,name='memberProposal'),
	url(r'addmember/',views.addmember,name='addmember'),
	url(r'addQuestion',views.addQuestion,name='addQuestion'),
	url(r'feeds/',views.feeds,name='feeds'),
	url(r'addAnswers/(?P<questionId>[0-9]+)',views.addAnswer,name='addAnswer'),
	url(r'question_view/(?P<pk>[0-9]+)',views.question_view,name='question_view'),
	url(r'(?P<answerId>[0-9]+)/(?P<questionId>[0-9]+)/answerUpDown/',views.answerUpDown,name='answerUpDown'),
]

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from web3 import Web3
from .models import Users,Question,HashList,Answer,AnswerEntries,memberProposal
from .EtherFeeds import authUser,addUser
import datetime

from .EtherFeeds import authUser,addUser,addQu
def index(request,error_message=""):
	init(request)
	args={'error_message':error_message}
	return render(request, 'etherfeeds/index.html', args)
def logout(request):
	args={}
	request.session.clear()
	return HttpResponseRedirect(reverse('etherfeeds:index'))
def listMembers(request):
	members=Users.objects.all()
	args={'members':members}
	return render(request, 'etherfeeds/listMembers.html', args)
def dashboard(request):
	if authUser(str(request.user)):
		args={'user':request.user}
		return render(request,'etherfeeds/dashboard.html',args)
	else:
		args={'error_message':"You are still not a member of the compnay"}
		return HttpResponseRedirect(reverse('etherfeeds:index'))
def createpoll(request):
	args={}
	return render(request,'etherfeeds/createpoll.html',args)
def addmember(request,):
	args={}
	return render(request,'etherfeeds/addmember.html',args)
def addQuestion(request):
	args={}
	question_text 	= request.POST['question']
	pub_date		= datetime.datetime.now()
	time_exp_days	= request.POST['time_exp_days']
	time_exp_hours	= request.POST['time_exp_hours']
	time_exp_minutes= request.POST['time_exp_minutes']
	exp_time		= pub_date+datetime.timedelta(days=int(time_exp_days))+datetime.timedelta(hours=int(time_exp_hours))+datetime.timedelta(minutes=int(time_exp_minutes))
	usrAddr			= request.user
	tx_receipt=addQu(request.user,'0x29246a5B71c9876E71B58f79f49D5F1454D87686',hash(question_text))
	print(tx_receipt)
	try:
		user	=	Users.objects.get(usrAddr=usrAddr)
	except:
		user	=	Users.objects.create(usrAddr=usrAddr,usrSig="DEF132DA167829F8")

	Question.objects.create(question_text=question_text,pub_date=pub_date,\
	time_exp_days=time_exp_days,time_exp_hours=time_exp_hours,time_exp_minutes=time_exp_minutes,\
	user=user,exp_time=exp_time)
	return HttpResponseRedirect(reverse('etherfeeds:dashboard'))
def addAnswer(request,questionId):
	answer=request.POST["newAnswer"]
	questionObj=get_object_or_404(Question,pk=questionId)
	Answer.objects.create(question=questionObj,answer_text=answer)
	return HttpResponseRedirect(reverse('etherfeeds:question_view', args=(questionObj.id,)))
def init(request):
	init_user	= '0x29246a5B71c9876E71B58f79f49D5F1454D87686'
	init_sig    = 'Ia23yoahaf!'
	try:
		Obj	=	Users.objects.get(usrAddr=init_user,usrSig=init_sig)
	except Users.DoesNotExist:
		Users.objects.create(usrAddr=init_user,usrSig=init_sig)
		suser=User.objects.create_superuser(username=init_user,email="",password="Ia23yoahaf!")
		suser.save()
def feeds(request):
	now=datetime.datetime.now()
	questions=Question.objects.all()#.order_by('time_exp_days')
	time_left=[]
	for question in questions:
		print(str(now))
		if now.strftime("%Y-%m-%d %H:%M:%S")>question.exp_time.strftime("%Y-%m-%d %H:%M:%S"):
			question.status=0
			question.save()
		else:
			question.status=1
			question.save()
		time_left.append(question.exp_time)
	quest_time=zip(questions,time_left)
	args={'questions':quest_time}
	return render(request,'etherfeeds/feeds.html',args)
def question_view(request,pk):
	questionObj	 	= get_object_or_404(Question, pk=pk)
	if questionObj.status==1:
		answers 		= Answer.objects.filter(question=questionObj)
		status 			= []
		upvotes		 	= []
		downvotes	 	= []
		for answer in answers:
			user=get_object_or_404(Users,usrAddr=request.user)
			try:
				Obj=get_object_or_404(AnswerEntries,user=user,answer=answer)
				status.append(0)
			except:
				status.append(1)
			upvotes.append(answer.upvotes)
			downvotes.append(answer.downvotes)
		answerList=zip(answers,status,upvotes,downvotes)
		args={'question':questionObj,'answerList':answerList,'finalAns':""}
		return render(request,'etherfeeds/question_view.html',args)
	else:
		args=[]
		answers 		= Answer.objects.filter(question=questionObj)
		status 			= []
		upvotes		 	= []
		downvotes	 	= []
		maxVotes		= []
		for answer in answers:
			user=get_object_or_404(Users,usrAddr=request.user)
			try:
				Obj=get_object_or_404(AnswerEntries,user=user,answer=answer)
				status.append(0)
			except:
				status.append(1)
			upvotes.append(answer.upvotes)
			downvotes.append(answer.downvotes)
			maxVotes.append(answer.upvotes-answer.downvotes)
		finalAns=""
		try:
			maxVote=max(maxVotes)
			indexOfFinalAns=maxVotes.index(maxVote)
			finalAns=answers[indexOfFinalAns]
		except:
			pass
		answerList=zip(answers,status,upvotes,downvotes)
		args={'question':questionObj,'answerList':answerList,'finalAns':finalAns}
		return render(request,'etherfeeds/question_view.html',args)
def answerUpDown(request,answerId,questionId):
	answerObj	= get_object_or_404(Answer, pk=answerId)
	questionObj = get_object_or_404(Question, pk=questionId)
	user		= get_object_or_404(Users, usrAddr=request.user)
	if request.POST['answer'+answerId]=='1':
		answerObj.upvotes+=1
	else:
		answerObj.downvotes+=1
	answerObj.save()
	newVote=AnswerEntries.objects.create(answer=answerObj,user=user)
	return HttpResponseRedirect(reverse('etherfeeds:question_view', args=(questionObj.id,)))
def memberProposal(request):
	proposer	= request.user
	proposalFor	= request.POST['publicAddr']
	# print(type(proposalFor))
	if Web3.isAddress(proposalFor):
		try:
			Obj	=	Users.objects.get(usrAddr=proposalFor,usrSig=proposer)
		except:
			tx_receipt=addUser(request.user,proposalFor)
			print(tx_receipt)
			Users.objects.create(usrAddr=proposalFor,usrSig=proposer)
			suser=User.objects.create_superuser(username=proposalFor,email="",password="Ia23yoahaf!")
			suser.save()
		return HttpResponseRedirect(reverse('etherfeeds:dashboard'))
	else:
		return HttpResponseRedirect(reverse('etherfeeds:addmember'))

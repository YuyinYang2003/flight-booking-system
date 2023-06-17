from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q


@api_view(['GET',"POST"])
# 用户注册
def userRegister(request):
  # 获取参数
  id_card = request.POST.get('id_card')
  name = request.POST.get('name')
  account = request.POST.get('account')
  pwd = request.POST.get('pwd')
  sex = request.POST.get('sex')
  telephone = request.POST.get('telephone')
  # 查询身份证号是否已被注册
  checkUser = user.objects.filter(Q(id_card=id_card) | Q(account=account))
  if checkUser.exists() == True :
    # 如果已经被注册,则直接返回错误消息
    return Action.fail("身份证或账户已被注册")
  # 若没注册，添加入数据库
  newUser = user(id_card=id_card, name=name, account=account, pwd=pwd, sex=sex, telephone=telephone, type=2)
  newUser.save()
  return Action.success()

@api_view(['GET',"POST"])
# 用户编辑
def userEdit(request):
  # 获取参数
  id_card = request.POST.get('id_card')
  name = request.POST.get('name')
  account = request.POST.get('account')
  pwd = request.POST.get('pwd')
  sex = request.POST.get('sex')
  telephone = request.POST.get('telephone')
  # 查询是否存在
  checkUser = user.objects.filter(Q(id_card=id_card) | Q(account=account))
  if checkUser.exists() == True :
    # 如果存在则开始更改
    newuser = checkUser.first()
    newuser.name = name
    newuser.pwd = pwd
    newuser.sex = sex
    newuser.telephone = telephone
    newuser.save()
    return Action.success(UserSerializer(newuser, many = False).data)
  else:
    # 若没注册
    return Action.fail("信息有误")

@api_view(['GET',"POST"])
# 用户登录
def userLogin(request):
  # 获取参数
  login_type = request.POST.get('login_type')
  account = request.POST.get('account')
  id_card = request.POST.get('id_card')
  pwd = request.POST.get('pwd')
  if login_type=='account':
    # 根据account查询
    checkUser = user.objects.filter(account=account).first()
  else:
    checkUser = user.objects.filter(id_card=id_card).first()
  if not checkUser:
    # 用户不存在,则直接返回错误消息
    return Action.fail("用户不存在")
  if checkUser.pwd != pwd:
    # 用户存在,密码不一致,则直接返回错误消息
    return Action.fail("密码错误")
  # 登陆成功
  return Action.success(UserSerializer(checkUser, many = False).data)

@api_view(['GET',"POST"])
# 列表
def userList(request):
  name = request.POST.get('name')
  if name:
    list = user.objects.filter(name__icontains=name).all()
  else:
    list = user.objects.all()
  return Action.success(UserSerializer(list, many = True).data)
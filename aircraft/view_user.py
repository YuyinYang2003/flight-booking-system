from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q


@api_view(['GET',"POST"])
# 用户注册
def userRegister(request):
  user_name = request.POST.get('user_name')
  password = request.POST.get('password')
  phone = request.POST.get('phone')
  email = request.POST.get('email')
  # 查询身份证号是否已被注册
  checkUser = user_info.objects.filter(Q(user_name=user_name))
  if checkUser.exists() == True :
    # 如果已经被注册,则直接返回错误消息
    return Action.fail("账户已被注册")
  # 若没注册，添加入数据库
  newUser = user_info(user_name=user_name, password=password, phone=phone, email=email, user_type='非会员', point=0)
  newUser.save()
  return Action.success()

@api_view(['GET',"POST"])
# 用户编辑
def userEdit(request):
  # 获取参数
  user_name = request.POST.get('user_name')
  password = request.POST.get('password')
  phone = request.POST.get('phone')
  email = request.POST.get('email')
  # 查询是否存在
  checkUser = user_info.objects.filter(Q(user_name=user_name))
  if checkUser.exists() == True :
    # 如果存在则开始更改
    newuser = checkUser.first()
    newuser.user_name=user_name
    newuser.password=password
    newuser.phone=phone
    newuser.email=email
    newuser.save()
    return Action.success(UserSerializer(newuser, many = False).data)
  else:
    # 若没注册
    return Action.fail("用户不存在")

@api_view(['GET',"POST"])
# 管理员编辑
def adminEdit(request):
  # 获取参数
  administrator_id = request.POST.get('administrator_id')
  password = request.POST.get('password')
  phone = request.POST.get('phone')
  email = request.POST.get('email')
  # 查询是否存在
  checkAdminId = administrator_info.objects.filter(Q(administrator_id=administrator_id))
  if checkAdminId.exists() == True :
    # 如果存在则开始更改
    newadmin = checkAdminId.first()
    newadmin.password=password
    newadmin.phone=phone
    newadmin.email=email
    newadmin.save()
    return Action.success(AdminSerializer(newadmin, many = False).data)
  else:
    # 若没注册
    return Action.fail("管理员不存在")

@api_view(['GET',"POST"])
# 用户登录
def userLogin(request):
  # 获取参数
  login_type = request.POST.get('login_type') #user或者administrator
  account = request.POST.get('account') #user account
  administrator_id = request.POST.get('administrator_id')
  password = request.POST.get('password')
  if login_type=='user':
    # 根据account查询
    checkUser = user_info.objects.filter(account=account).first()
    if not checkUser:
    # 用户不存在,则直接返回错误消息
      return Action.fail("用户不存在")
    if checkUser.password != password:
    # 用户存在,密码不一致,则直接返回错误消息
      return Action.fail("密码错误")
    return Action.success(UserSerializer(checkUser, many = False).data)
  else:
    checkAdmin = administrator_info.objects.filter(administrator_id=administrator_id).first()
    if not checkAdmin:
    # 管理员不存在,则直接返回错误消息
      return Action.fail("管理员不存在")
    if checkUser.password != password:
    # 管理员存在,密码不一致,则直接返回错误消息
      return Action.fail("密码错误")
    # 登陆成功
    return Action.success(AdminSerializer(checkAdmin, many = False).data)
  

@api_view(['GET',"POST"])
# 列表
def userList(request):
  name = request.POST.get('name')
  if name:
    list = user_info.objects.filter(name__icontains=name).all()
  else:
    list = user_info.objects.all()
  return Action.success(UserSerializer(list, many = True).data)
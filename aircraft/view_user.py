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
# 乘机人注册
def passengerRegister(request):
  user_name = request.POST.get('user_name')
  passenger_identity_id = request.POST.get('passenger_identity_id')
  passenger_name=request.POST.get('passenger_name')
  sex = request.POST.get('sex')
  passenger_phone = request.POST.get('passenger_phone')
  passport = request.POST.get('passport')
  passenger_type = request.POST.get('passenger_type')
  # 查询身份证号是否已被注册
  checkIdentity = passenger_info.objects.filter(Q(passenger_identity_id=passenger_identity_id))
  if checkIdentity.exists() == True :
    # 如果已经被注册,则直接返回错误消息
    return Action.fail("乘机人已被注册，可直接绑定，不可重复注册")
  else:
    # 若没注册，添加入数据库
    newPassenger = passenger_info(passenger_identity_id=passenger_identity_id, passenger_name=passenger_name, sex=sex, phone=passenger_phone, passport=passport, passenger_type=passenger_type)
    newPassenger.save()
    newPassengerUser = passenger_user(user_name=user_name, passenger_identity_id=passenger_identity_id)
    newPassengerUser.save()
    return Action.success()

@api_view(['GET',"POST"])
# 管理员编辑乘机人
def adminEditpassenger(request):
  # 获取要编辑的乘机人身份证号,获取要改变的信息
  passenger_identity_id = request.POST.get('passenger_identity_id')
  passenger_type = request.POST.get('passenger_type')
  # 查询是否存在
  checkPassenger = passenger_info.objects.filter(Q(passenger_identity_id=passenger_identity_id))
  if checkPassenger.exists() == True :
    # 如果存在则开始更改
    newpassenger = checkPassenger.first()
    newpassenger.passenger_type=passenger_type
    newpassenger.save()
    return Action.success(Passenger_infoSerializer(newpassenger, many = False).data)
  else:
    # 若没注册
    return Action.fail("乘机人不存在")

@api_view(['GET',"POST"])
# 乘机人绑定
def passengerBound(request):
  user_name = request.POST.get('user_name')
  passenger_identity_id = request.POST.get('passenger_identity_id')
  passenger_name=request.POST.get('passenger_name')
  # 查询乘机人是否被该用户绑定
  checkIdentityUser = passenger_user.objects.filter(Q(passenger_identity_id=passenger_identity_id)&Q(user_name=user_name))
  checkNameUser = passenger_info.objects.filter(Q(passenger_identity_id=passenger_identity_id)&Q(passenger_name=passenger_name))
  if checkIdentityUser.exists() == True :
    # 如果已经被绑定,则直接返回错误消息
    return Action.fail("乘机人已被绑定")
  else:
    # 如果姓名不匹配,则返回错误信息
    if checkNameUser.exists() == False:
      return Action.fail("乘机人身份证号和姓名不匹配")
    else:
    # 若没注册，添加入数据库
      newPassengerUser = passenger_user(user_name=user_name, passenger_identity_id=passenger_identity_id)
      newPassengerUser.save()
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
# 管理员创建用户
def adminCreateuser(request):
  user_name = request.POST.get('user_name')
  password = request.POST.get('password')
  phone = request.POST.get('phone')
  email = request.POST.get('email')
  user_type = request.POST.get('user_type')
  point = request.POST.get('point')
  # 查询身份证号是否已被注册
  checkUser = user_info.objects.filter(Q(user_name=user_name))
  if checkUser.exists() == True :
    # 如果已经被注册,则直接返回错误消息
    return Action.fail("账户已被注册")
  # 若没注册，添加入数据库
  newUser = user_info(user_name=user_name, password=password, phone=phone, email=email, user_type=user_type, point=point)
  newUser.save()
  return Action.success()

@api_view(['GET',"POST"])
# 管理员编辑用户
def adminEdituser(request):
  # 获取要编辑的用户名,获取要改变的信息
  user_name = request.POST.get('user_name')
  user_type = request.POST.get('user_type')
  point = request.POST.get('point')
  # 查询是否存在
  checkUser = user_info.objects.filter(Q(user_name=user_name))
  if checkUser.exists() == True :
    # 如果存在则开始更改
    newuser = checkUser.first()
    newuser.user_type=user_type
    newuser.point=point
    newuser.save()
    return Action.success(UserSerializer(newuser, many = False).data)
  else:
    # 若没注册
    return Action.fail("用户不存在")


@api_view(['GET',"POST"])
# 乘机人编辑
def passengerEdit(request):
  # 获取参数
  passenger_identy_id=request.POST.get('passenger_identity_id')
  passenger_phone = request.POST.get('passenger_phone')
  passport = request.POST.get('passport')
  passenger_type = request.POST.get('passenger_type')
  # 查询是否存在
  checkPassenger = passenger_info.objects.filter(Q(passenger_identy_id=passenger_identy_id))
  if checkPassenger.exists() == True :
    # 如果存在则开始更改
    newpassenger = checkPassenger.first()
    newpassenger.phone=passenger_phone
    newpassenger.passport=passport
    newpassenger.passenger_type=passenger_type
    newpassenger.save()
    return Action.success(Passenger_infoSerializer(newpassenger, many = False).data)
  else:
    # 若没注册
    return Action.fail("乘机人不存在，请先注册")

@api_view(['GET',"POST"])
# 用户登录
def userLogin(request):
  # 获取参数
  login_type = request.POST.get('login_type') #user或者administrator
  user_name = request.POST.get('user_name') #user account
  administrator_id = request.POST.get('administrator_id')
  password = request.POST.get('password')
  if login_type=='user':
    # 根据account查询
    checkUser = user_info.objects.filter(user_name=user_name).first()
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
    if checkAdmin.password != password:
    # 管理员存在,密码不一致,则直接返回错误消息
      return Action.fail("密码错误")
    # 登陆成功
    return Action.success(AdminSerializer(checkAdmin, many = False).data)
  

@api_view(['GET',"POST"])
# 管理员查看用户列表
def userList(request):
  name = request.POST.get('name')
  if name:
    list = user_info.objects.filter(user_name=name).all()
  else:
    list = user_info.objects.all()
  return Action.success(UserSerializer(list, many = True).data)

@api_view(['GET',"POST"])
# 用户查看乘机人列表
def passengerList(request):
  user_name = request.POST.get('user_name')
  list = passenger_user.objects.all()
  if user_name:
    list = list.filter(user_name=user_name)
  arr = []
  for item in list:
    temp_data = {}
    temp_data['passenger_identity_id'] = item.passenger_identity_id
    passenger=passenger_info.objects.filter(passenger_identity_id=item.passenger_identity_id).first()
    temp_data['passenger_name'] = passenger.passenger_name 
    temp_data['sex'] = passenger.sex
    temp_data['passenger_phone'] = passenger.phone
    temp_data['passport'] = passenger.passport
    temp_data['passenger_type'] = passenger.passenger_type
    arr.append(temp_data)
  return Action.success(arr)

@api_view(['GET',"POST"])
# 管理员删除乘机人
def Deletepassenger(request):
  # 获取参数
  passenger_identy_id=request.POST.get('passenger_identity_id')
  # 查询是否存在
  checkPassenger = passenger_info.objects.filter(Q(passenger_identy_id=passenger_identy_id))
  if checkPassenger.exists() == True :
    # 如果存在则删除
    checkPassenger.delete()
    return Action.success()
  else:
    # 若没注册
    return Action.fail("乘机人不存在，无法删除")

@api_view(['GET',"POST"])
# 管理员删除用户
def Deleteuser(request):
  # 获取参数
  user_name=request.POST.get('user_name')
  # 查询是否存在
  checkUser = user_info.objects.filter(Q(user_name=user_name))
  if checkUser.exists() == True :
    # 如果存在则删除
    checkUser.delete()
    return Action.success()
  else:
    # 若没注册
    return Action.fail("用户不存在，无法删除")



# 用户编辑
def buyVIP(request):
  # 获取参数
  user_name = request.POST.get('user_name')
  # 查询是否本来就是会员
  checkUser=user_info.objects.filter(Q(user_name=user_name))
  checkVIP = checkUser.first().user_type
  if checkVIP=='非会员':
    # 如果非会员则开始更改
    newuser = checkUser.first()
    newuser.user_type='会员'
    newuser.save()
    return Action.success(UserSerializer(newuser, many = False).data)
  else:
    # 若本来就是
    return Action.fail("已是会员")
  
@api_view(['GET',"POST"])
# 乘机人绑定的修改删除
def passengerBoundDrop(request):
  user_name = request.POST.get('user_name')
  passenger_identity_id = request.POST.get('passenger_identity_id')
  # 查询乘机人是否被该用户绑定
  checkIdentityUser = passenger_user.objects.filter(Q(passenger_identity_id=passenger_identity_id)&Q(user_name=user_name))
  if checkIdentityUser.exists() == False :
    # 如果乘机人没有被绑定,则直接返回错误消息
    return Action.fail("乘机人未被当前用户绑定")
  else:
    # 若已被绑定，则删除
    checkIdentityUser.delete()
    return Action.success()
  

@api_view(['GET',"POST"])
# 收藏的删除
def FavoriteDrop(request):
  favorite_id = request.POST.get('favorite_id')
  user_name=request.POST.get('user_name')
  # 查询该收藏是否被当前用户添加到收藏信息中
  checkfavorite_id = favorites.objects.filter(Q(favorite_id=favorite_id)|Q(user_name=user_name))
  if checkfavorite_id.exists() == False :
    # 如果该收藏没有被用户添加，则返回错误信息
    return Action.fail("当前收藏不存在")
  else:
    # 若收藏已经被添加，则删除
    checkfavorite_id.delete()
    return Action.success()

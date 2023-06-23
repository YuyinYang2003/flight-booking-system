from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q


# 添加订单
def buyTicketAlter(p,s,type):
  #买机票后的积分和价格变更
  #type=0留学生，1会员，2非会员
  if type==0:
    if s<=p*1.1:
      dp=s//1.1
      p=p-dp
      s=s-dp*1.1
    else:
      p=0
      s=s-p*1.1
    if s<=1000:
      p=p+s//100
    elif 1000<s and s<=5000:
      p=p+10+(s-1000)//80
    elif 5000<s and s<=12000:
      p=p+60+(s-5000)//70
    else:
      p=p+160+(s-12000)//60
  elif type==1:
    if s<=p:
      p=p-s
      s=0
    else:
      p=0
      s=s-p
    if s<=1000:
      p=p+s//100
    elif 1000<s and s<=5000:
      p=p+10+(s-1000)//80
    else:
      p=p+60+(s-5000)//70
  else:
    if s<=p*0.5:
      p=p-2*s
      s=0
    else:
      p=0
      s=s-p*0.5
    if s<=1200:
      p=p+s//120
    elif 1200<s and s<=6200:
      p=p+10+(s-1200)//100
    else:
      p=p+60+(s-6200)//80
  return [p,s]
  
@api_view(['GET',"POST"])
# 添加订单
# 点确认购买
def orderAdd(request):
  # 获取参数
  user_name = request.POST.get('user_name')
  passenger_identity_id = request.POST.get('passenger_identity_id') #需要增加乘机人信息
  flight_num1 = request.POST.get('flight_num1')
  flight_num2 = request.POST.get('flight_num2') #两个航班显示在同一条订单记录里
  airplane_num1 = request.POST.get('airplane_num1')
  airplane_num2 = request.POST.get('airplane_num2')
  set_class = request.POST.get('set_class') #0economy,1first,2business
  if set_class=='经济舱':
     set_classn = 0
  elif set_class=='头等舱':
     set_classn = 1
  else:
     set_classn = 2
  flight_mode = request.POST.get('flight_mode') #0直飞，1转机
  flight_mode = int(flight_mode)
  usePointOrNot = request.POST.get('usePointOrNot') #0是否 1是是
  if usePointOrNot == '1':
    usePointOrNot = 1
  else:
    usePointOrNot = 0
  # 查询航班
  checkUserPassenger=passenger_user.objects.filter(user_name=user_name,passenger_identity_id=passenger_identity_id)
  if checkUserPassenger.exists():
    if flight_mode==0:
      checkFlight = flight_city2.objects.filter(flight_num=flight_num1).first()
      user=user_info.objects.filter(user_name=user_name).first()
      passenger=passenger_info.objects.filter(passenger_identity_id=passenger_identity_id).first()
      flight=flight_info.objects.filter(flight_num=flight_num1).first()
      studentornot=passenger.passenger_type
      if studentornot=='留学生':
        user_type=0
      else:
        vipornot=user.user_type
        if vipornot=='会员':
          user_type=1
        else:
          user_type=2
      point=user.point
      if set_class == '经济舱':

        total_seat=airplane_info.objects.filter(airplane_id=airplane_num1).first().economy_set
        remain_seat = checkFlight.current_economy_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.economy_class_price
        #更新余票
        flight.current_economy_set-=1
        flight.save()
      elif set_class == '头等舱':
        total_seat=airplane_info.objects.filter(airplane_id=airplane_num1).first().first_set
        remain_seat = checkFlight.current_first_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.first_class_price
        #更新余票
        flight.current_first_set-=1
        flight.save()
      else:
        total_seat=airplane_info.objects.filter(airplane_id=airplane_num1).first().bussiness_set
        remain_seat = checkFlight.current_bussiness_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.business_class_price
        #更新余票
        flight.current_bussiness_set-=1
        flight.save()
      #生成座位号
      if set_class=='经济舱':
        seat_num = 'JJ' + str(total_seat-remain_seat + 1)
      elif set_class=='头等舱':
        seat_num='TD'+str(total_seat-remain_seat + 1)
      else:
        seat_num='SW'+str(total_seat-remain_seat + 1)
      
      #计算积分和价格变更
      #if usePointOrNot:
      #  cost=buyTicketAlter(float(point),cost,user_type)[1]
      #  point=buyTicketAlter(float(point),cost,user_type)[0]
      
      #生成订单
      classl=['经济舱','头等舱','公务舱']
      usepointl=['否','是']
      newOrder=order_info(passenger_identity_id=passenger_identity_id,flight_num1=flight_num1,set_class1=classl[set_classn],set_class2='无',set_num1=seat_num,order_state='正常',point_use=usepointl[usePointOrNot],price=cost,user_name=user_name)
      newOrder.save()
      
      #更新积分
      user.point=point
      user.save()
      return Action.success()
    else:
      checkFlight = flight_result.objects.filter(Q(flight_num1=flight_num1)&Q(flight_num2=flight_num2)).first()
      user=user_info.objects.filter(user_name=user_name).first()
      passenger=passenger_info.objects.filter(passenger_identity_id=passenger_identity_id).first()
      flight1=flight_info.objects.filter(flight_num=flight_num1).first()
      flight2=flight_info.objects.filter(flight_num=flight_num2).first()
      studentornot=passenger.passenger_type
      if studentornot=='留学生':
        user_type=0
      else:
        vipornot=user.user_type
        if vipornot=='会员':
          user_type=1
        else:
          user_type=2
      point=user.point
      if set_class == '经济舱':
        total_seat1=airplane_info.objects.filter(airplane_id=airplane_num1).first().economy_set
        remain_seat1 = checkFlight.current_economy_set1
        total_seat2=airplane_info.objects.filter(airplane_id=airplane_num2).first().economy_set
        remain_seat2 = checkFlight.current_economy_set2
        if remain_seat1*remain_seat2==0:
          return Action.fail("已售罄")
        cost = checkFlight.economy_class_price
        #更新余票
        flight1.current_economy_set-=1
        flight1.save()
        flight2.current_economy_set-=1
        flight2.save()
      elif set_class == '头等舱':
        total_seat1=airplane_info.objects.filter(airplane_id=airplane_num1).first().first_set
        remain_seat1 = checkFlight.current_first_set1
        total_seat2=airplane_info.objects.filter(airplane_id=airplane_num2).first().first_set
        remain_seat2 = checkFlight.current_first_set2
        if remain_seat1*remain_seat2==0:
          return Action.fail("已售罄")
        cost = checkFlight.first_class_price
        #更新余票
        flight1.current_first_set-=1
        flight1.save()
        flight2.current_first_set-=1
        flight2.save()
      else:
        total_seat1=airplane_info.objects.filter(airplane_id=airplane_num1).first().bussiness_set
        remain_seat1 = checkFlight.current_bussiness_set1
        total_seat2=airplane_info.objects.filter(airplane_id=airplane_num2).first().bussiness_set
        remain_seat2 = checkFlight.current_bussiness_set2
        if remain_seat1*remain_seat2==0:
          return Action.fail("已售罄")
        cost = checkFlight.business_class_price
        #更新余票
        flight1.current_bussiness_set-=1
        flight1.save()
        flight2.current_bussiness_set-=1
        flight2.save()
      #生成座位号
      if set_class=='经济舱':
        seat_num1 = 'JJ' + str(total_seat1-remain_seat1 + 1)
        seat_num2 = 'JJ' + str(total_seat2-remain_seat2 + 1)
      elif set_class=='头等舱':
        seat_num1='TD'+str(total_seat1-remain_seat1 + 1)
        seat_num2='TD'+str(total_seat2-remain_seat2 + 1)
      else:
        seat_num1='SW'+str(total_seat1-remain_seat1 + 1)
        seat_num2='SW'+str(total_seat2-remain_seat2 + 1)
      
      #计算积分和价格变更
      #if usePointOrNot:
      #  cost=buyTicketAlter(point,cost,user_type)[1]
      #  point=buyTicketAlter(point,cost,user_type)[0]
      
      #生成订单
      classl=['经济舱','头等舱','公务舱']
      usepointl=['否','是']
      
      newOrder=order_info(passenger_identity_id=passenger_identity_id,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=classl[set_classn],set_class2=classl[set_classn],set_num1=seat_num1,set_num2=seat_num2,order_state='正常',point_use=usepointl[usePointOrNot],price=cost,user_name=user_name)
      newOrder.save()
      
      #更新积分
      user.point=point
      user.save()
      return Action.success()
  else:
    Action.fail("未绑定乘机人")

# 订单列表
def orderList(request):
  #获取用户名信息
  user_name = request.POST.get('user_name')
  list = order_info.objects.all()
  #如果获取到，筛选出该用户的订单
  if user_name:
    list = list.filter(user_name=user_name)
  arr = []
  #显示信息
  for item in list:
    temp_data = {}
    temp_data['order_id'] = item.order_id
    temp_data['user_name'] = item.user_name
    temp_data['passenger_name'] = passenger_info.objects.filter(passenger_identity_id=item.passenger_identity_id).first().passenger_name 
    temp_data['flight_num1'] = item.flight_num1
    temp_data['airplane_num1'] = flight_info.objects.filter(flight_num= item.flight_num1).first().airplane_num
    temp_data['order_time'] = item.order_time
    temp_data['price'] = item.price
    temp_data['order_state'] = item.order_state
    if item.flight_num2:
      temp_data['flight_num2'] = item.flight_num2
      temp_data['airplane_num2'] = flight_info.objects.filter(flight_num= item.flight_num2).first().airplane_num

    arr.append(temp_data)
  return Action.success(arr)

# 添加收藏
def favouriteAdd(request):
  # 获取参数
  user_name = request.POST.get('user_name')  #获取用户名
  flight_mode = request.POST.get('flight_mode')  #获取要收藏的这个订单是直飞0还是中转1
  flight_mode = int(flight_mode)
  set_class = request.POST.get('set_class')  #获取舱位
  #如果是直飞：
  if flight_mode == 0:
    flight_num = request.POST.get('flight_num1')  #获取想要收藏的航班号
    checkFlight = flight_info.objects.filter(flight_num=flight_num).first()
    checkFavorite = favorites.objects.filter(user_name = user_name,flight_num1=flight_num,set_class1=set_class,flight_num2='无').first()  #检验有没有收藏过
    #如果之前已经收藏过
    if checkFavorite:
      return Action.fail("已存在收藏夹中")  
    else :
      UserlastFavorite = favorites.objects.filter(user_name = user_name).last()  #检验用户之前是否有过收藏记录
      #按照舱位的不同收藏不同的价格
      if set_class == '经济舱':
        if UserlastFavorite:   #存在收藏记录则收藏编号+1
          newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.economy_class_price)
        else:   #不存在则设置为0
          newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.economy_class_price)
      else :
        if set_class == '头等舱':
          if UserlastFavorite:
            newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.first_class_price)
          else:
            newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.first_class_price)
        else:
          if UserlastFavorite:
            newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.business_class_price)
          else:
            newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,set_class2='无',total_price=checkFlight.business_class_price)
      newfavorite.save()
      return Action.success()
  else:
    #如果是转机的情况
    if flight_mode == 1:
      flight_num1 = request.POST.get('flight_num1')  #获取第一趟航班
      flight_num2 = request.POST.get('flight_num2')  #获取第二段航班
      print('收藏：', flight_num1,flight_num2, user_name)
      # 查询收藏，和之前相同，只是增加了第二段航班的信息和转机字段
      checkFlight = flight_result.objects.filter(flight_num1=flight_num1,flight_num2=flight_num2).first()
      checkFavorite = favorites.objects.filter(user_name = user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class).first()
      if checkFavorite:
        return Action.fail("已存在收藏夹中")  
      else :
        UserlastFavorite = favorites.objects.filter(user_name = user_name).last()
        if set_class == '经济舱':
          if UserlastFavorite:
            newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.economy_class_price)
          else:
            newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.economy_class_price)
        else :
          if set_class == '头等舱':
            if UserlastFavorite:
              newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.first_class_price)
            else:
              newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.first_class_price)
          else:
            if UserlastFavorite:
              newfavorite = favorites(favorite_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.business_class_price)
            else:
              newfavorite = favorites(favorite_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.business_class_price)
        newfavorite.save()
        return Action.success()

@api_view(['GET',"POST"])
# 订单列表
def favourList(request):
  #获取用户名信息
  user_name = request.POST.get('user_name')
  list = favorites.objects.all()
  #如果获取到，筛选出该用户的订单
  if user_name:
    list = list.filter(user_name=user_name)
  arr = []
  #显示信息
  for item in list:
    temp_data = {}
    temp_data['favorite_id'] = item.favorite_id
    temp_data['flight_num1'] = item.flight_num1
    temp_data['airplane_num1'] = flight_info.objects.filter(flight_num= item.flight_num1).first().airplane_num
    temp_data['set_class1']=item.set_class1
    temp_data['total_price'] = item.total_price
    #temp_data['transfer_time'] = item.transfer_time
    if item.flight_num2:
      temp_data['airplane_num2'] = flight_info.objects.filter(flight_num= item.flight_num2).first().airplane_num
      temp_data['set_class2']=item.set_class1
    arr.append(temp_data)
  return Action.success(arr)

@api_view(['GET',"POST"])
# 退票
def orderReturn(request):
  # 获取参数
  order_id = request.POST.get('order_id')
  # 查询
  print(order_id)
  checkOrder = order_info.objects.filter(order_id=order_id).first()
  if not checkOrder :
    return Action.fail("订单不存在")
  checkOrder.order_state = '退款申请'  #修改订单状态
  checkOrder.save()
  return Action.success()

@api_view(['GET',"POST"])
# 处理退票
def returnmoney(request):
  # 获取参数
  order_id = request.POST.get('order_id')
  # 查询
  checkOrder = order_info.objects.filter(order_id=order_id).first()
  if not checkOrder :
    return Action.fail("订单不存在")
  checkOrder.order_state = '已退款'  #修改订单状态
  checkOrder.save()
  return Action.success()

@api_view(['GET',"POST"])
# 收藏的删除
def FavoriteDrop(request):
  favorite_id = request.POST.get('favorite_id')
  user_name=request.POST.get('user_name')
  # 查询该收藏是否被当前用户添加到收藏信息中
  checkfavorite_id = favorites.objects.filter(Q(favorite_id=favorite_id)&Q(user_name=user_name))
  if checkfavorite_id:
    # 若收藏已经被添加，则删除
    checkfavorite_id.delete()
    return Action.success()
  else:
    # 如果该收藏没有被用户添加，则返回错误信息
    return Action.fail("当前收藏不存在")
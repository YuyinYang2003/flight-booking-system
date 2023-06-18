from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q


@api_view(['GET',"POST"])
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
  set_class = request.POST.get('set_class') #0economy,1first,2business
  flight_mode = request.POST.get('flight_mode') #0直飞，1转机
  usePointOrNot = request.POST.get('usePointOrNot')
  print('购票：', flight_num1, flight_num2, set_class, user_name, passenger_identity_id)
  # 查询航班
  checkUserPassenger=passenger_user.objects.filter(user_name=user_name,passenger_identity_id=passenger_identity_id)
  if checkUserPassenger.exists():
    if flight_mode==0:
      checkFlight = flight_city2.objects.filter(flight_num=flight_num1).first()
      user=user_info.objects.filter(username=user_name).first()
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
      if set_class == '0':
        total_seat=airplane_info.objects.filter(aiplane_id=flight_num1).first().economy_set
        remain_seat = checkFlight.current_ecnomy_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.economy_class_price
        #更新余票
        flight.current_ecnomy_set-=1
        flight.save()
      elif set_class == '1':
        total_seat=airplane_info.objects.filter(aiplane_id=flight_num1).first().first_set
        remain_seat = checkFlight.current_first_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.first_class_price
        #更新余票
        flight.current_first_set-=1
        flight.save()
      else:
        total_seat=airplane_info.objects.filter(aiplane_id=flight_num1).first().bussiness_set
        remain_seat = checkFlight.current_bussiness_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.business_class_price
        #更新余票
        flight.current_bussiness_set-=1
        flight.save()
      #生成座位号
      if set_class==0:
        seat_num = 'JJ' + str(total_seat-remain_seat + 1)
      elif set_class==1:
        seat_num='TD'+str(total_seat-remain_seat + 1)
      else:
        seat_num='SW'+str(total_seat-remain_seat + 1)
      
      #计算积分和价格变更
      if usePointOrNot:
        cost=buyTicketAlter(point,cost,user_type)[1]
        point=buyTicketAlter(point,cost,user_type)[0]
      
      #生成订单
      classl=['经济舱','头等舱','商务舱']
      usepointl=['否','是']
      newOrder=order_info(passenger_identity_id=passenger_identity_id,flight_num1=flight_num1,set_class1=classl[set_class],set_num1=seat_num,order_state='正常',point_use=usepointl[usePointOrNot],price=cost)
      
      #更新积分
      user.point=point
      user.save()
      return Action.success()
    else:
      checkFlight = flight_result.objects.filter(Q(flight_num1=flight_num1)&Q(flight_num2=flight_num2)).first()
      user=user_info.objects.filter(username=user_name).first()
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
      if set_class == '0':
        total_seat1=airplane_info.objects.filter(aiplane_id=flight_num1).first().economy_set
        remain_seat1 = checkFlight.current_ecnomy_set1
        total_seat2=airplane_info.objects.filter(aiplane_id=flight_num2).first().economy_set
        remain_seat2 = checkFlight.current_ecnomy_set2
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.economy_class_price
        #更新余票
        flight1.current_ecnomy_set-=1
        flight1.save()
        flight2.current_ecnomy_set-=1
        flight2.save()
      elif set_class == '1':
        total_seat1=airplane_info.objects.filter(aiplane_id=flight_num1).first().first_set
        remain_seat1 = checkFlight.current_first_set1
        total_seat2=airplane_info.objects.filter(aiplane_id=flight_num2).first().first_set
        remain_seat2 = checkFlight.current_first_set2
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.first_class_price
        #更新余票
        flight1.current_first_set-=1
        flight1.save()
        flight2.current_first_set-=1
        flight2.save()
      else:
        total_seat1=airplane_info.objects.filter(aiplane_id=flight_num1).first().bussiness_set
        remain_seat1 = checkFlight.current_bussiness_set1
        total_seat2=airplane_info.objects.filter(aiplane_id=flight_num1).first().bussiness_set
        remain_seat2 = checkFlight.current_bussiness_set2
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.business_class_price
        #更新余票
        flight1.current_bussiness_set-=1
        flight1.save()
        flight2.current_bussiness_set-=1
        flight2.save()
      #生成座位号
      if set_class==0:
        seat_num1 = 'JJ' + str(total_seat1-remain_seat1 + 1)
        seat_num2 = 'JJ' + str(total_seat2-remain_seat2 + 1)
      elif set_class==1:
        seat_num1='TD'+str(total_seat1-remain_seat1 + 1)
        seat_num2='TD'+str(total_seat2-remain_seat2 + 1)
      else:
        seat_num1='SW'+str(total_seat1-remain_seat1 + 1)
        seat_num2='SW'+str(total_seat2-remain_seat2 + 1)
      
      #计算积分和价格变更
      if usePointOrNot:
        cost=buyTicketAlter(point,cost,user_type)[1]
        point=buyTicketAlter(point,cost,user_type)[0]
      
      #生成订单
      classl=['经济舱','头等舱','商务舱']
      usepointl=['否','是']
      newOrder=order_info(passenger_identity_id=passenger_identity_id,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=classl[set_class],set_class2=classl[set_class],set_num1=seat_num1,set_num2=seat_num2,order_state='正常',point_use=usepointl[usePointOrNot],price=cost)
      
      #更新积分
      user.point=point
      user.save()
      return Action.success()
  else:
    Action.fail("未绑定乘机人")

# 列表
def orderList(request):
  user_id = request.POST.get('user_id')
  user_name = request.POST.get('user_name')
  list = order.objects.all()
  if user_id:
    list = list.filter(user_id=user_id)
  arr = []
  for item in list:
    temp_data = {}
    temp_data['id'] = item.id
    temp_data['user_id'] = item.user_id
    if user_name:
      temp_user = user.objects.filter(id_card=item.user_id, name__icontains=user_name).first()
      if not temp_user:
        continue
    temp_data['user_name'] = user.objects.filter(id_card=item.user_id).first().name 
    temp_data['flight_id'] = item.flight_id
    temp_data['time'] = item.time
    temp_data['ticket_id'] = item.ticket_id
    temp_data['cost'] = item.cost
    temp_data['status'] = item.status
    temp_data['message'] = ''
    if item.ticket_id:
      temp_data['message'] = ticket.objects.filter(id=item.ticket_id).first().message
    arr.append(temp_data)
  return Action.success(arr)

# 添加收藏
def favouriteAdd(request):
  # 获取参数
  user_name = request.POST.get('user_name')  #获取用户名
  flight_mode = request.POST.get('flight_mode')  #获取要收藏的这个订单是直飞0还是中转1
  set_class = request.POST.get('set_class')  #获取舱位
  #如果是直飞：
  if flight_mode == 0:
    flight_num = request.POST.get('flight_num')  #获取想要收藏的航班号
    print('收藏：', flight_num,  user_name)
    checkFlight = flight_info.objects.filter(flight_num=flight_num).first()
    checkFavorite = favorites.objects.filter(user_name = user_name,flight_num=flight_num,set_class1=set_class).first()  #检验有没有收藏过
    #如果之前已经收藏过
    if checkFavorite.exists():
      return Action.fail("已存在收藏夹中")  
    else :
      UserlastFavorite = favorites.objects.filter(user_name = user_name).last()  #检验用户之前是否有过收藏记录
      #按照舱位的不同收藏不同的价格
      if set_class == '经济舱':
        if UserlastFavorite.exists():   #存在收藏记录则收藏编号+1
          newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.ecnomy_class_price)
        else:   #不存在则设置为0
          newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.ecnomy_class_price)
      else :
        if set_class == '头等舱':
          if UserlastFavorite.exists():
            newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.first_class_price)
          else:
            newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.first_class_price)
        else:
          if UserlastFavorite.exists():
            newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.bussiness_class_price)
          else:
            newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num,set_class1=set_class,total_price=checkFlight.bussiness_class_price)
      newfavorite.save()
      return Action.success()
  else:
    #如果是转机的情况
    if flight_mode == 1:
      flight_num1 = request.POST.get('flight_num1')  #获取第一趟航班
      flight_num2 = request.POST.get('flight_num2')  #获取第二段航班
      print('收藏：', flight_num,flight_num2, user_name)
      # 查询收藏，和之前相同，只是增加了第二段航班的信息和转机字段
      checkFlight = flight_result.objects.filter(flight_num1=flight_num1,flight_num2=flight_num2).first()
      checkFavorite = favorites.objects.filter(user_name = user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class).first()
      if checkFavorite.exists():
        return Action.fail("已存在收藏夹中")  
      else :
        UserlastFavorite = favorites.objects.filter(user_name = user_name).last()
        if set_class == '经济舱':
          if UserlastFavorite.exists():
            newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.economy_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
          else:
            newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num1=flight_num1,set_class1=set_class,set_class2=set_class,total_price=checkFlight.economy_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
        else :
          if set_class == '头等舱':
            if UserlastFavorite.exists():
              newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.first_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
            else:
              newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.first_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
          else:
            if UserlastFavorite.exists():
              newfavorite = favorites(favorites_id = UserlastFavorite.favorite_id+1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.business_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
            else:
              newfavorite = favorites(favorites_id = 1,user_name=user_name,flight_num1=flight_num1,flight_num2=flight_num2,set_class1=set_class,set_class2=set_class,total_price=checkFlight.business_class_price,transfer=(checkFlight.depart_time2-checkFlight.arrive_time1))
        newfavorite.save()
        return Action.success()


@api_view(['GET',"POST"])
# 退票
def orderReturn(request):
  # 获取参数
  id = request.POST.get('id')
  # 查询
  checkOrder = order.objects.filter(id=id).first()
  if not checkOrder :
    return Action.fail("订单不存在")
  checkOrder.status = 3
  checkOrder.save()
  return Action.success()
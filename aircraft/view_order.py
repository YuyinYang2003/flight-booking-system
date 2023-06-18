from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q

   
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
        remain_seat = checkFlight.current_economy_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.economy_class_price
      elif set_class == '1':
        total_seat=airplane_info.objects.filter(aiplane_id=flight_num1).first().first_set
        remain_seat = checkFlight.current_first_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.first_class_price
      else:
        total_seat=airplane_info.objects.filter(aiplane_id=flight_num1).first().bussiness_set
        remain_seat = checkFlight.current_bussiness_set
        if remain_seat==0:
          return Action.fail("已售罄")
        cost = checkFlight.business_class_price
      #生成座位号
      if set_class==0:
        seat_num = 'JJ' + str(total_seat-remain_seat + 1)
      elif set_class==1:
        seat_num='TD'+str(total_seat-remain_seat + 1)
      else:
        seat_num='SW'+str(total_seat-remain_seat + 1)
      #生成订单
      newOrder=order_info(passenger_identity_id=passenger_identity_id)
    # 查询票
    checkTickets = flight_city2.objects.filter(flight_num1=flight_num1, flight_num2=flight_num2)
  if checkTickets.count() == seat_num_sum:
    return Action.fail("已售罄")
  if ticket_type == '0':
    seat_num = 'JJ' + str(checkTickets.count() + 1)
  else:
    seat_num = 'JJ' + str(checkTickets.count() + 1)
  # 生成票
  newTicket = ticket(corp=checkFlight.corp, flight_id=flight_num, user_id=user_id, ticket_type=ticket_type, boarding_time=checkFlight.depart_time, seat_num=seat_num, port=checkFlight.port)
  newTicket.save()
  # 生成订单
  newOrder = order(user_id=user_id, flight_id=flight_num, ticket_id=newTicket.id, cost=cost, status=2)
  newOrder.save()
  # 更新航班余票
  checkFlight.ticket_remain -= 1
  checkFlight.save()
  return Action.success()

# 列表
# 显示购票记录
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
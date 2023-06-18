from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q
from django.core import serializers

# 机票详情（用户光标点击 订单管理 界面 详情的时候）
def ticketInfo(request):
  order_id = request.POST.get('orfer_id')
  #根据订单号获取详细信息
  checkTicket = order_info.objects.filter(order_id=order_id).first()
  checkFlight1 = flight_city2.objects.filter(flight_num = checkTicket.flight_num1).first()
  checkFlight2 = flight_city2.objects.filter(flight_num = checkTicket.flight_num2).first()
  checkPassenger = passenger_info.objects.filter(passenger_identity_id = checkTicket.passenger_identity_id).first()
  #获取乘机人姓名，出发时间地点到达时间地点和座位号的数据，先获取第一段航班
  data = {}
  data['passenger_name'] = checkPassenger.passenger_name,
  data['airplane_num1'] = checkFlight1.airplane_num,
  data['depart_airport_name1'] = checkFlight1.depart_airport_name,
  data['arrive_airport_name1'] = checkFlight1.arrive_airport_name,
  data['depart_time1'] = checkFlight1.depart_time,
  data['seat_num1'] = checkTicket.set_num1,
  data['arrive_time1'] = checkFlight1.arrive_time,
  if checkFlight2:   #如果存在第二段航班，获取第二段航班的信息
    data['airplane_num2'] = checkFlight2.airplane_num,
    data['depart_airport_name2'] = checkFlight2.depart_airport_name,
    data['arrive_airport_name2'] = checkFlight2.arrive_airport_name,
    data['depart_time2'] = checkFlight2.depart_time,
    data['seat_num2'] = checkTicket.set_num2,
    data['arrive_time2'] = checkFlight2.arrive_time,
  # json_data = serializers.serialize('json', { checkTicket, checkFlight, checkUser })
  return Action.success(data)   #上传显示

# （面向管理员）订单管理表
def ticketList(request):
  #获取数据
  user_name = request.POST.get('user_name')
  list = order_info.objects.all()
  if user_name:
    list = list.filter(user_name=user_name)
  arr = []
  #显示该用户的所有机票订单信息
  for item in list:
    temp_data = {}
    temp_data['user_name'] = item.user_name
    temp_data['flight_num1'] = item.flight_num1
    temp_data['passenger_identity_id'] = item.passenger_identity_id
    temp_data['passenger_name'] = passenger_info.objects.filter(passenger_identity_id=item.passenger_identity_id).first().passenger_name 
    temp_data['ticket_type1'] = item.set_class1
    temp_data['set_num1'] = item.set_num1
    temp_data['order_status'] = item.order_status
    if item.flight_num2:  #如果是有第二段航班，收集第二段航班的信息
      temp_data['flight_num2'] = item.flight_num2
      temp_data['ticket_type2'] = item.set_class2
      temp_data['set_num2'] = item.set_num2
    arr.append(temp_data)
  return Action.success(arr)   #发送显示

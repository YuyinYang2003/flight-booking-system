from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q


@api_view(['GET',"POST"])
# 添加订单
def orderAdd(request):
  # 获取参数
  user_id = request.POST.get('user_id')
  flight_num = request.POST.get('flight_num')
  ticket_type = request.POST.get('ticket_type')
  print('购票：', flight_num, ticket_type, user_id)
  # 查询航班
  checkFlight = flight.objects.filter(flight_num=flight_num).first()
  if checkFlight.ticket_remain == 0 :
    return Action.fail("已售罄")
  if ticket_type == '1':
    seat_num_sum = checkFlight.ticket_total_first_class
    cost = checkFlight.price_first_class
  else:
    seat_num_sum = checkFlight.ticket_total_economy_class
    cost = checkFlight.price_economy_class
  # 查询票
  checkTickets = ticket.objects.filter(flight_id=flight_num, ticket_type=ticket_type)
  if checkTickets.count() == seat_num_sum:
    return Action.fail("已售罄")
  if ticket_type == '1':
    seat_num = 'TD' + str(checkTickets.count() + 1)
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
from rest_framework.decorators import api_view
from datetime import datetime,timedelta
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q

@api_view(['GET',"POST"])
# 列表
def flightList(request):
  flight_num = request.POST.get('flight_num')
  depart = request.POST.get('depart')
  arrive = request.POST.get('arrive')
  depart_time = request.POST.get('depart_time')
  list = flight.objects.all()
  if flight_num:
    list = list.filter(flight_num__icontains=flight_num)
  if  depart:
    list = list.filter(depart__icontains=depart)
  if  arrive:
    list = list.filter(arrive__icontains=arrive)
  if  depart_time :
    list = list.filter(depart_time__range=(datetime.strptime(depart_time, '%Y-%m-%d')+timedelta(days=-1),datetime.strptime(depart_time, '%Y-%m-%d')))
  return Action.success(FlightSerializer(list, many = True).data)

@api_view(['GET',"POST"])
# 添加
def flightAdd(request):
  # 获取参数
  flight_num = request.POST.get('flight_num')
  #corp = request.POST.get('corp')
  #depart = request.POST.get('depart')
  #arrive = request.POST.get('arrive')
  depart_time = request.POST.get('depart_time')
  airplane_num = request.POST.get('airplane_num')
  arrive_time = request.POST.get('arrive_time')
  depart_airport = request.POST.get('depart_airport')
  arrive_airport = request.POST.get('arrive_airport')
  ticket_total_first_class = request.POST.get('ticket_total_first_class')
  ticket_total_business_class = request.POST.get('ticket_total_business_class')
  ticket_total_economy_class = request.POST.get('ticket_total_economy_class')
  first_class_price = request.POST.get('first_class_price')
  business_class_price = request.POST.get('business_class_price')
  economy_class_price = request.POST.get('economy_class_price')
  baggage_info = request.POST.get('baggage_info')
  # 查询
  has = flight_info.objects.filter(flight_num=flight_num)
  if has.exists() == True :
    return Action.fail("已存在")
  # 若没,添加入数据库
  new = flight_info(flight_num=flight_num, depart_airport=depart_airport, airplane_num=airplane_num, arrive_airport=arrive_airport, depart_time=depart_time, arrive_time=arrive_time, economy_class_price=economy_class_price, first_class_price=first_class_price, business_class_price=business_class_price, current_economy_set=ticket_total_economy_class, current_first_set=ticket_total_first_class, current_business_set=ticket_total_business_class, baggage_info=baggage_info)
  new.save()
  # 添加成功
  return Action.success()

#这一段没改完，得改完view_ticket再改
@api_view(['GET',"POST"])
# 发送延误
def flightDelay(request):
  # 获取参数
  airplane_num = request.POST.get('airplane_num')
  #改成了通过真实世界的航班号来查询
  # 查询
  checkFlight = flight_info.objects.filter(airplane_num=airplane_num)
  if checkFlight.exists() == False :
    return Action.fail("航班不存在")
  checkFlight = checkFlight.first()
  ticketList = ticket.objects.filter(flight_id=checkFlight.flight_num)
  for item in ticketList:
    item.message = '该航班已延误'
    item.save()
  return Action.success()

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
  corp = request.POST.get('corp')
  depart = request.POST.get('depart')
  arrive = request.POST.get('arrive')
  depart_time = request.POST.get('depart_time')
  arrive_time = request.POST.get('arrive_time')
  depart_airport = request.POST.get('depart_airport')
  arrive_airport = request.POST.get('arrive_airport')
  ticket_total_first_class = request.POST.get('ticket_total_first_class')
  ticket_total_economy_class = request.POST.get('ticket_total_economy_class')
  ticket_remain = request.POST.get('ticket_remain')
  price_first_class = request.POST.get('price_first_class')
  price_economy_class = request.POST.get('price_economy_class')
  port = request.POST.get('port')
  # 查询
  has = flight.objects.filter(flight_num=flight_num)
  if has.exists() == True :
    return Action.fail("已存在")
  # 若没,添加入数据库
  new = flight(flight_num=flight_num, corp=corp, depart=depart, arrive=arrive, depart_time=depart_time, arrive_time=arrive_time, depart_airport=depart_airport, arrive_airport=arrive_airport, ticket_total_first_class=ticket_total_first_class, ticket_total_economy_class=ticket_total_economy_class, ticket_remain=ticket_remain, price_first_class=price_first_class, price_economy_class=price_economy_class, port=port)
  new.save()
  # 添加成功
  return Action.success()

@api_view(['GET',"POST"])
# 发送延误
def flightDelay(request):
  # 获取参数
  flight_num = request.POST.get('flight_num')
  # 查询
  checkFlight = flight.objects.filter(flight_num=flight_num)
  if checkFlight.exists() == False :
    return Action.fail("航班不存在")
  checkFlight = checkFlight.first()
  ticketList = ticket.objects.filter(flight_id=checkFlight.flight_num)
  for item in ticketList:
    item.message = '该航班已延误'
    item.save()
  return Action.success()

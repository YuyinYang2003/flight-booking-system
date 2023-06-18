from rest_framework.decorators import api_view
from datetime import datetime,timedelta
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q

@api_view(['GET',"POST"])
# 列表
# 查询航班
def flightList(request):
  #航班查询四个筛选方式：价格，出发地，到达地，出发日期，行李信息
  price_low = request.POST.get('price_low')
  price_high = request.POST.get('price_high')
  depart = request.POST.get('depart')
  arrive = request.POST.get('arrive')
  depart_time = request.POST.get('depart_time')
  baggage = request.POST.get('luggage') #只能筛选全都含免费行李/无筛选需求，要求全都含免费行李为1，无筛选需求为0
  flight_mode = request.POST.get('flight_mode') #要么中转要么直飞，0是直飞，1是中转
  if flight_mode == 1:
    list = flight_result.objects.all()
    #筛选中价格筛选是只要三种价格一种在区间内，这个飞行方案就会出现
    if price_low:
      list = list.filter(Q(economy_class_price__gt=price_low)|Q(first_class_price__gt=price_low)|Q(business_class_price__gt=price_low))
    if price_high:
      list = list.filter(Q(economy_class_price__lt=price_high)|Q(first_class_price__lt=price_high)|Q(business_class_price__lt=price_high))
    if depart:
      list = list.filter(depart_city=depart)
    if arrive:
      list = list.filter(arrive_city=arrive)
    if depart_time:
      list = list.filter(depart_time1__range=(datetime.strptime(depart_time, '%Y-%m-%d')+timedelta(days=-1),datetime.strptime(depart_time, '%Y-%m-%d')))
    if baggage:
      list = list.filter(Q(baggage_info1=1)&Q(baggage_info2=1))
    return Action.success(MultiFlightSerializer(list, many = True).data) #多加一个转机的serializer
  else:
    list = flight_city2.objects.all()
    if price_low:
      list = list.filter(Q(economy_class_price__gt=price_low)|Q(first_class_price__gt=price_low)|Q(business_class_price__gt=price_low))
    if price_high:
      list = list.filter(Q(economy_class_price__lt=price_high)|Q(first_class_price__lt=price_high)|Q(business_class_price__lt=price_high))
    if depart:
      list = list.filter(depart_city=depart)
    if arrive:
      list = list.filter(arrive_city=arrive)
    if depart_time:
      list = list.filter(depart_time1__range=(datetime.strptime(depart_time, '%Y-%m-%d')+timedelta(days=-1),datetime.strptime(depart_time, '%Y-%m-%d')))
    if baggage:
      list = list.filter(baggage_info=1)
    return Action.success(FlightSerializer(list, many = True).data)

@api_view(['GET',"POST"])
# 管理员添加新航班
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

from rest_framework.decorators import api_view
from datetime import datetime,timedelta
from .Action import Action
from .models import *
from .models_view import *
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
  flight_mode = request.POST.get('flight_mode') #要么中转要么直飞，0直飞1中转，默认0
  arr = []
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
    for item in list:
      flight = {}
      flight['airplane_num1'] = item.airplane_num1
      flight['airplane_num2'] = item.airplane_num2
      flight['depart_time1'] = item.depart_time1
      flight['arrive_time1'] = item.arrive_time1
      flight['depart_time2'] = item.depart_time2
      flight['arrive_time2'] = item.arrive_time2
      flight['depart_airport_name'] = item.depart_airport_name
      flight['transfer_airport_name'] = item.transfer_airport_name
      flight['arrive_airport_name'] = item.arrive_airport_name
      if item.current_economy_set1>=1:
        flight['price'] = item.economy_class_price
      if item.current_first_set2>=1:
        flight['price'] = item.first_class_price
      if item.current_bussiness_set2>=1:
        flight['price'] = item.business_class_price
      arr.append(flight)

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
  for item in list:
    flight = {}
    flight['airplane_num1'] = item.airplane_num
    flight['airplane_num2'] = None
    flight['depart_time1'] = item.depart_time
    flight['arrive_time1'] = item.arrive_time
    flight['depart_time2'] = None
    flight['arrive_time2'] = None
    flight['depart_airport_name'] = item.depart_airport_name
    flight['transfer_city'] = None
    flight['arrive_airport_name'] = item.arrive_airport_name
    if item.current_economy_set>=1:
      flight['price'] = item.ecnomy_class_price
    if item.current_first_set>=1:
      flight['price'] = item.first_class_price
    if item.current_bussiness_set>=1:
      flight['price'] = item.business_class_price
    arr.append(flight)
  return Action.success(arr)   

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




@api_view(['GET',"POST"])
# 发送延误
def flightDelay(request):
  # 获取延误的这一趟飞行的航班号（唯一标识一趟飞行的）
  flight_num = request.POST.get('flight_num')
  #查询检索航班号是否存在
  checkFlight = flight_info.objects.filter(flight_num=flight_num)
  if checkFlight.exists() == False :
    return Action.fail("航班不存在")
  # 存在则查询含有这趟航班的订单
  else:
    checkFlight = checkFlight.first()
    ticketList = order_info.objects.filter(Q(flight_num1=flight_num)|Q(flight_num2=flight_num)) #中转订单任何一个取消都算取消
    #取消航班的同时将这趟航班的的余票设置为0，防止再次查询出来
    checkFlight.current_economy_set=0
    checkFlight.current_bussiness_set=0
    checkFlight.current_first_set=0
    checkFlight.save()
    for item in ticketList:
      item.order_status = '该航班已取消'  #修改订单状态
      item.save()
    return Action.success()
  


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
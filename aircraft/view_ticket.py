from rest_framework.decorators import api_view
from .Action import Action
from .models import *
from .serializers import *
from django.shortcuts import render
from django.db.models import Q
from django.core import serializers

# 机票详情
def ticketInfo(request):
  ticket_id = request.POST.get('ticket_id')
  checkTicket = ticket.objects.filter(id=ticket_id).first()
  checkFlight = flight.objects.filter(flight_num = checkTicket.flight_id).first()
  checkUser = user.objects.filter(id_card = checkTicket.user_id).first()
  data = {}
  data['corp'] = checkFlight.corp,
  data['user_name'] = checkUser.name,
  data['flight_id'] = checkFlight.flight_num,
  data['depart'] = checkFlight.depart,
  data['arrive'] = checkFlight.arrive,
  data['depart_time'] = checkFlight.depart_time,
  data['seat_num'] = checkTicket.seat_num,
  data['port'] = checkFlight.port,
  data['boarding_time'] = checkTicket.boarding_time,
  # json_data = serializers.serialize('json', { checkTicket, checkFlight, checkUser })
  return Action.success(data)

# 列表
def ticketList(request):
  user_id = request.POST.get('user_id')
  list = ticket.objects.all()
  if user_id:
    list = list.filter(user_id=user_id)
  arr = []
  for item in list:
    temp_data = {}
    temp_data['id'] = item.id
    temp_data['corp'] = item.corp
    temp_data['flight_id'] = item.flight_id
    temp_data['user_id'] = item.user_id
    temp_data['user_name'] = user.objects.filter(id_card=item.user_id).first().name 
    temp_data['ticket_type'] = item.ticket_type
    temp_data['boarding_time'] = item.boarding_time
    temp_data['seat_num'] = item.seat_num
    temp_data['port'] = item.port
    temp_data['message'] = item.message
    arr.append(temp_data)
  return Action.success(arr)

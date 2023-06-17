from rest_framework import serializers
from .models import *

# 用户
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ['id_card', 'name', 'account', 'pwd', 'sex', 'telephone', 'type']

# 航班
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight
        fields = ['flight_num', 'corp', 'depart', 'arrive', 'depart_time', 'arrive_time', 'depart_airport', 'arrive_airport', 'ticket_total_first_class', 'ticket_total_economy_class', 'ticket_remain', 'price_first_class', 'price_economy_class', 'port']

# 订单
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order
        fields = ['id', 'user_id', 'flight_id', 'time', 'ticket_id', 'cost', 'status']

# 票
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ticket
        fields = ['id', 'corp', 'flight_id', 'user_id', 'ticket_type', 'boarding_time', 'seat_num', 'port', 'message']

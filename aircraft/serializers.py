from rest_framework import serializers
from .models import *

# 用户
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_info
        fields = ['user_name', 'password', 'phone', 'email', 'user_type', 'point']

# 管理员
class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = administrator_info
        fields = ['administrator_id', 'email', 'password', 'phone']

# 航班
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight_info
        fields = ['flight_num', 'corp', 'depart', 'arrive', 'depart_time', 'arrive_time', 'depart_airport', 'arrive_airport', 'ticket_total_first_class', 'ticket_total_economy_class', 'ticket_remain', 'price_first_class', 'price_economy_class', 'port']

# 订单
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order_info
        fields = ['id', 'user_id', 'flight_id', 'time', 'ticket_id', 'cost', 'status']

# 票
#class TicketSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = ticket
#        fields = ['id', 'corp', 'flight_id', 'user_id', 'ticket_type', 'boarding_time', 'seat_num', 'port', 'message']

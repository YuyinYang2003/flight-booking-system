from rest_framework import serializers
from .models import *
from .models_view import *

# 用户
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_info
        fields = ['user_name',  'password', 'phone', 'email', 'user_type', 'point']

#管理员
class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = administrator_info
        fields = ['administrator_id',  'password', 'phone', 'email']


#乘机人
class Passenger_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = passenger_info
        fields = ['passenger_identity_id',  'passenger_name', 'passenger_phone', 'sex','birthdate','passport','passenger_type']

# 飞机
class Airplane_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = airplane_info
        fields = ['airplane_id', 'plane_type', 'company_id', 'economy_set', 'first_set', 'bussiness_set']

#机场
class Airport_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = airport_info
        fields = ['airport_id', 'airport_name', 'location', 'time_zones']

# 航班
class Flight_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight_info
        fields = ['flight_num', 'depart_time', 'arrive_time', 'airplane_num', 'depart_airport', 'arrive_airport', 'current_first_set', 'current_economy_set', 'current_bussiness_set', 'ecnomy_class_price', 'first_class_price', 'bussiness_class_price', 'baggage_info']

# 收藏
class FavoritesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = favorites
        fields = ['favorite_id', 'user_name', 'flight_num1', 'flight_num2', 'set_choice', 'set_class1', 'set_class2','total_price','transfer']

# 票
class Order_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order_info
        fields = ['order_id', 'user_name', 'passenger_identity_id', 'flight_num1', 'flight_num2', 'order_time',  'set_class1', 'set_class2','set_num1','set_num2','order_status','price','point_use']

#用户乘机人绑定
class Passenger_userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = passenger_user
        fields = ['passenger_user_key','user_name', 'passenger_identity_id']

#有转机的路线信息
class MultiFlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight_result
        fields = ['airplane_num1', 'airplane_num2', 'depart_time1','arrive_time2','depart_airport_name','transfer_airport_name','arrive_airport_name','economy_class_price']

#直达的路线信息
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight_city2
        fields = ['airplane_num', 'depart_time','arrive_time','depart_airport_name','arrive_airport_name','economy_class_price']
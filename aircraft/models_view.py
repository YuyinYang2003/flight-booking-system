from django.db import models
from datetime import datetime
import django_mysql.models
#中转查询
class flight_result(models.Model):
    flight_num1 = models.CharField(max_length=10) # 航班号1
    airplane_num1 = models.CharField(max_length=10) # 飞机号1
    arrive_time1 = models.DateTimeField() # 到达时间1
    depart_time1 = models.DateTimeField() # 出发时间1
    depart_airport_name = models.CharField(max_length=10) # 出发机场名
    depart_city = models.CharField(max_length=30) # 出发城市
    baggage_choice={
        ('0'),
        ('1')
    }
    baggage_info1 =django_mysql.models.EnumField(choices=baggage_choice) # 航班1含几件免费行李
    current_bussiness_set1 = models.SmallIntegerField() #航班一剩余公务舱座位
    current_economy_set1 =  models.SmallIntegerField() #航班一剩余经济舱座位
    current_first_set1 = models.SmallIntegerField() #航班一剩余头登舱座位
    transfer_airport_name = models.CharField(max_length=10) # 中转机场名
    transfer_city = models.CharField(max_length=30) # 中转城市
    economy_class_price = models.DecimalField(max_digits=7, decimal_places=0) #经济舱总价格
    business_class_price = models.DecimalField(max_digits=7, decimal_places=0) #公务舱总价格
    first_class_price = models.DecimalField(max_digits=7, decimal_places=0) #公务舱总价格
    flight_num2 = models.CharField(max_length=10) # 航班号2
    airplane_num2 = models.CharField(max_length=10) # 飞机号2
    arrive_airport_name = models.CharField(max_length=10) # 到达机场名
    depart_time2 = models.DateTimeField() # 出发时间2
    arrive_time2 = models.DateTimeField() # 到达时间2
    arrive_city = models.CharField(max_length=30) # 到达城市
    baggage_info2 =django_mysql.models.EnumField(choices=baggage_choice) # 航班2含几件免费行李
    current_bussiness_set2 = models.SmallIntegerField() #航班二剩余公务舱座位
    current_economy_set2 =  models.SmallIntegerField() #航班二剩余经济舱座位
    current_first_set2 = models.SmallIntegerField() #航班二剩余头登舱座位

    class Meta:
        db_table = 'flight_result'

#单次查询
class flight_city2(models.Model):
    flight_num = models.CharField(primary_key=True, max_length=10) # 唯一标识飞机编号
    depart_time = models.DateTimeField() # 出发时间
    arrive_time = models.DateTimeField() # 达到时间
    airplane_num = models.CharField(max_length=10) # 飞机编号
    depart_airport_name = models.CharField(max_length=10) # 出发机场名
    depart_city = models.CharField(max_length=30) # 出发城市
    arrive_airport_name = models.CharField(max_length=10) # 到达机场名
    arrive_city = models.CharField(max_length=30) # 到达城市
    current_first_set = models.SmallIntegerField() # 头等舱剩余票数
    current_economy_set = models.SmallIntegerField() # 经济舱剩余票数
    current_bussiness_set = models.SmallIntegerField() # 公务舱剩余票数
    ecnomy_class_price = models.DecimalField(max_digits=6, decimal_places=0) # 经济舱票价
    first_class_price  = models.DecimalField(max_digits=6, decimal_places=0) # 头等舱票价
    business_class_price  = models.DecimalField(max_digits=6, decimal_places=0) # 公务舱票价
    baggage_choice={
        ('0'),
        ('1')
    }
    baggage_info =django_mysql.models.EnumField(choices=baggage_choice) # 含几件免费行李
    depart_time_zones = models.SmallIntegerField()#出发地时区
    arrive_time_zones = models.SmallIntegerField()#到达地时区
    class Meta:
        db_table = 'flight_city2'

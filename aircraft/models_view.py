from django.db import models
from datetime import datetime
import django_mysql.models

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

from django.db import models
from datetime import datetime
import django_mysql.models

# 用户信息类
class user_info(models.Model):
    user_name = models.CharField(primary_key=True, max_length=30) # 唯一用户名
    password = models.CharField(max_length=30) # 密码
    phone = models.CharField(max_length=15) # 电话号码
    email = models.EmailField(max_length=30) # email
    user_type_choice={
        ('非会员'),
        ('会员')
    }
    user_type = django_mysql.models.EnumField(choices=user_type_choice) # 用户种类：非会员/会员
    point = models.SmallIntegerField() # 积分值

    class Meta:
        managed = False
        db_table = 'user_info'

#管理员
class administrator_info(models.Model):
    administrator_id = models.CharField(primary_key=True, max_length=30) # 唯一管理员id
    password = models.CharField(max_length=30) # 密码
    phone = models.CharField(max_length=15) # 电话号码
    email = models.EmailField(max_length=30) # email

    class Meta:
        managed = False
        db_table = 'administrator_info'

#乘机人信息类
class passenger_info(models.Model):
    passenger_identity_id = models.CharField(primary_key=True, max_length=18) # 乘机人身份证号
    passenger_name = models.CharField(max_length=10) # 姓名
    phone = models.CharField(max_length=15) # 电话号码
    sex = models.SmallIntegerField() # 性别0男1女
    birthdate = models.DateField() # 出生日期
    passport = models.CharField(max_length=10) # 护照号码
    passenger_type_choice={
        ('留学生','普通乘客'),
        ('会员')
    }
    passenger_type =django_mysql.models.EnumField(choices=passenger_type_choice) # 普通乘客/留学生
    
    class Meta:
        managed = False
        db_table = 'passenger_info'

#飞机
class airplane_info(models.Model):
    airplane_id = models.CharField(primary_key=True, max_length=10) # 唯一飞机id
    plane_type = models.CharField(max_length=10) # 飞机种类
    company_set = models.CharField(max_length=10) # 所属航空公司id
    economy_set = models.SmallIntegerField() # 经济舱座位数量
    first_set = models.SmallIntegerField() # 头等舱座位数量
    bussiness_set = models.SmallIntegerField() # 公务舱座位数量

    class Meta:
        managed = False
        db_table = 'airplane_info'

#机场
class airport_info(models.Model):
    airport_id = models.CharField(primary_key=True, max_length=10) # 唯一机场id
    airport_name = models.CharField(max_length=10) # 机场名字
    location = models.CharField(max_length=30) # 机场所在城市
    time_zones = models.SmallIntegerField() # 经济舱座位数量

    class Meta:
        managed = False
        db_table = 'airplane_info'

# 航班(一趟飞行)
class flight_info(models.Model):
    flight_num = models.CharField(primary_key=True, max_length=10) # 唯一标识飞机编号
    depart_time = models.DateTimeField() # 出发时间
    arrive_time = models.DateTimeField() # 达到时间
    airplane_num = models.CharField(max_length=10) # 出发机场编号
    depart_airport = models.CharField(max_length=10) # 出发机场编号
    arrive_airport = models.CharField(max_length=45) # 目的机场编号
    current_first_set = models.SmallIntegerField() # 头等舱剩余票数
    current_economy_set = models.SmallIntegerField() # 经济舱剩余票数
    current_business_set = models.SmallIntegerField() # 公务舱剩余票数
    ecnomy_class_price = models.DecimalField(max_digits=6, decimal_places=0) # 经济舱票价
    first_class_price  = models.DecimalField(max_digits=6, decimal_places=0) # 头等舱票价
    bussiness_class_price  = models.DecimalField(max_digits=6, decimal_places=0) # 公务舱票价
    baggage_info = models.CharField(max_length=50)#行李信息
 
    class Meta:
        managed = False
        db_table = 'flight_info'

# 收藏
class favorites(models.Model):
    favorite_id = models.SmallIntegerField() # 收藏号
    user_name = models.CharField(max_length=30) # 收藏的用户名
    flight_num1 = models.CharField(max_length=30) # 航班号1
    flight_num2 = models.CharField(max_length=30) # 航班号2
    set_choice={
        ('经济舱'),
        ('头等舱'),
        ('公务舱')
    }
    set_class1=django_mysql.models.EnumField(choices=set_choice)#舱位1
    set_class2=django_mysql.models.EnumField(choices=set_choice)#舱位2
    total_price = models.DecimalField(max_digits=6, decimal_places=0) # 原始金额
    transfer = models.TimeField() # 转机时间

    class Meta:
        unique_together=("user_name","favorite_id")
        managed = False
        db_table = 'favorites'

# 订单
class order_info(models.Model):
    order_id = models.AutoField(primary_key=True) # 唯一的订单号
    user_name = models.CharField(max_length=30) # 下单用户名
    passenger_identity_id = models.CharField(max_length=18) # 乘机人身份证号
    flight_num1 = models.CharField(max_length=10) # 航班号1
    flight_num2 = models.CharField(max_length=10) # 航班号2
    order_time = models.DateTimeField(auto_now_add=True) # 下单时间
    set_choice={
        ('经济舱'),
        ('头等舱'),
        ('公务舱')
    }
    set_class1=django_mysql.models.EnumField(choices=set_choice)#舱位1
    set_class2=django_mysql.models.EnumField(choices=set_choice)#舱位2
    set_num1=models.CharField(max_length=4)#座位号1
    set_num2=models.CharField(max_length=4)#座位号2
    status_choice={
        ('正常'),
        ('航班取消'),
        ('退款申请'),
        ('已退款')
    }
    order_status=django_mysql.models.EnumField(choices=status_choice)#订单状态
    price= models.DecimalField(max_digits=8, decimal_places=2) # 实际支付金额
    point_choice={
        ('是'),
        ('否'),
    }
    point_use=django_mysql.models.EnumField(choices=point_choice)#是否使用积分
    class Meta:
        managed = False
        db_table = 'order_info'

# 用户乘机人绑定
class passenger_user(models.Model):
    user_name = models.CharField(max_length=30) # 用户名
    passenger_identity_id = models.CharField(max_length=18) # 乘机人身份证号

    class Meta:
        unique_together=("user_name","passenger_identity_id")
        managed = False
        db_table = 'passenger_user'


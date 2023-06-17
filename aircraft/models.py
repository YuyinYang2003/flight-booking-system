from django.db import models
from datetime import datetime

# 用户类
class user(models.Model):
    id_card = models.CharField(primary_key=True, max_length=45) # id
    name = models.CharField(max_length=45) # 姓名
    account = models.CharField(max_length=45) # 账户
    pwd = models.CharField(max_length=45) # 密码
    sex = models.SmallIntegerField() # 性别
    telephone = models.CharField(max_length=45) # 电话
    type = models.SmallIntegerField(default=2) # 类型： 1-管理员，2-用户

    class Meta:
        managed = False
        db_table = 'user'

# 航班
class flight(models.Model):
    flight_num = models.CharField(primary_key=True, max_length=45) # id
    corp = models.CharField(max_length=45) # 航空公司
    depart = models.CharField(max_length=45) # 出发地
    arrive = models.CharField(max_length=45) # 目的地
    depart_time = models.DateTimeField() # 出发时间
    arrive_time = models.DateTimeField() # 达到时间
    depart_airport = models.CharField(max_length=45) # 出发机场
    arrive_airport = models.CharField(max_length=45) # 目的机场
    ticket_total_first_class = models.SmallIntegerField() # 头等舱总票数
    ticket_total_economy_class = models.SmallIntegerField() # 经济舱总票数
    ticket_remain = models.SmallIntegerField() # 剩余票数
    price_first_class = models.DecimalField(max_digits=10, decimal_places=2) # 头等舱票价
    price_economy_class = models.DecimalField(max_digits=10, decimal_places=2) # 经济舱票价
    port = models.CharField(max_length=45) # 登机口

    class Meta:
        managed = False
        db_table = 'flight'

# 订单
class order(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    user_id = models.CharField(max_length=45) # 用户id
    flight_id = models.CharField(max_length=45) # 航班id
    time = models.DateTimeField(auto_now_add=True) # 下单时间
    ticket_id = models.SmallIntegerField() # 票id
    cost = models.DecimalField(max_digits=10, decimal_places=2) # 金额
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'order'

# 票
class ticket(models.Model):
    id = models.AutoField(primary_key=True) # id 
    corp = models.CharField(max_length=45) # 航空公司
    flight_id = models.CharField(max_length=45) # 航班id
    user_id = models.CharField(max_length=45) # 用户id
    ticket_type = models.SmallIntegerField() # 类型
    boarding_time = models.DateTimeField() # 登机时间
    seat_num = models.CharField(max_length=45) # 座位号
    port = models.CharField(max_length=45) # 登机口
    message = models.CharField(max_length=200) # 消息

    class Meta:
        managed = False
        db_table = 'ticket'

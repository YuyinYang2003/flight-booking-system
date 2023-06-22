from django.shortcuts import render

# 页面渲染
#登陆页面
def login(request):
  return render(request, 'login.html')

#管理员页面: 航班
def admin_flight(request):
  return render(request, 'admin_flight.html')

#管理员页面: 订单
def admin_order(request):
  return render(request, 'admin_order.html')

#管理员页面: 机票
def admin_ticket(request):
  return render(request, 'admin_ticket.html')
  
#管理员页面: 乘机人
def admin_passenger(request):
  return render(request, 'admin_passenger.html')

#管理员页面: 用户
def admin_user(request):
  return render(request, 'admin_user.html')

#用户页面: 航班
def user_flight(request):
  return render(request, 'user_flight.html')

#用户页面: 订单
def user_order(request):
  return render(request, 'user_order.html')

#用户页面: 用户
def user_user(request):
  return render(request, 'user_user.html')

#用户页面: 乘机人
def user_passenger(request):
  return render(request, 'user_passenger.html')

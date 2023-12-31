"""aircraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from aircraft import view_user
from aircraft import view_flight
from aircraft import view_order
from aircraft import view_ticket
from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    #页面请求
    path('login/', views.login),
    path('admin/', views.admin_flight),
    path('admin_flight/', views.admin_flight),
    path('admin_order/', views.admin_order),
    path('admin_ticket/', views.admin_ticket),
    path('admin_user/', views.admin_user),
    path('admin_passenger/', views.admin_passenger),
    

    path('user/', views.user_flight),
    path('user_flight/', views.user_flight),
    path('user_order/', views.user_order),
    path('user_user/', views.user_user),
    path('user_passenger/', views.user_passenger),
    path('user_favourite/', views.user_favourite),

    path('adim_flightList', view_flight.adim_flightList, name='adim_flightList'),
    path('orderList', view_order.orderList, name='orderList'),
    path('returnmoney', view_order.returnmoney, name='returnmoney'),
    #数据请求

    #用户
    path('userLogin', view_user.userLogin, name='userLogin'),
    path('userRegister', view_user.userRegister, name='userRegister'),
    path('userEdit', view_user.userEdit, name='userEdit'),
    path('userList', view_user.userList, name='userList'),
    path('buyVIP', view_user.buyVIP, name='buyVIP'),
    #乘机人
    path('passengerRegister', view_user.passengerRegister, name='passengerRegister'),
    path('passengerBound', view_user.passengerBound, name='passengerBound'),
    path('passengerEdit', view_user.passengerEdit, name='passengerEdit'),
    path('passengerList', view_user.passengerList, name='passengerList'),
    path('passengerBoundDrop', view_user.passengerBoundDrop, name='passengerBoundDrop'),
    #航班
    path('flightList', view_flight.flightList, name='flightList'),
    path('flightAdd', view_flight.flightAdd, name='flightAdd'),
    path('flightDelay', view_flight.flightDelay, name='flightDelay'),
    #订单
    path('orderAdd', view_order.orderAdd, name='orderAdd'),
    path('orderList', view_order.orderList, name='orderList'),
    path('orderReturn', view_order.orderReturn, name='orderReturn'),
    # 机票
    path('ticketInfo', view_ticket.ticketInfo, name='ticketInfo'),
    path('ticketList', view_ticket.ticketList, name='ticketList'),
    # 收藏
    path('favouriteAdd', view_order.favouriteAdd, name='favouriteAdd'),
    path('favourList', view_order.favourList, name='favourList'),
    path('FavoriteDrop', view_order.FavoriteDrop, name='FavoriteDrop'),
    # 管理员
    path('adminEdit', view_user.adminEdit, name='adminEdit'),
    path('adminEdituser', view_user.adminEdituser, name='adminEdituser'),
    path('Deletepassenger', view_user.Deletepassenger, name='Deletepassenger'),
    path('Deleteuser', view_user.Deleteuser, name='Deleteuser'),
    path('adminCreateuser', view_user.adminCreateuser, name='adminCreateuser'),
]

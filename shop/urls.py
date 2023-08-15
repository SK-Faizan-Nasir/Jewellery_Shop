from django.conf.urls import include
from django.urls import re_path
from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^login/$', views.login_user, name='login'),
    re_path(r'^logout/$', views.logout_user, name='logout'),
    re_path(r'$', views.index, name='home'),
    re_path(r'^jewellery/$', views.index),
    # re_path(r'^/rings/$', views.showRings, name='rings'),
    # re_path(r'^/neckless/$', views.showNeckless, name = 'neckless'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^thank/$', views.thankYouPage , name='thank'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^cart/$', views.cart, name='cart'),
    re_path(r'^addToCart/(?P<qty>([^/]+))/(?P<buy_id>[0-9]+)/$', views.setQty, name = 'qty'),
    re_path(r'^detail/(?P<product_id>[0-9]+)/$', views.detailproduct, name='detail'),
    re_path(r'^detail/(?P<product_id>[0-9]+)/saved$', views.saveReview, name='saveReview'),
    re_path(r'^addToCart/(?P<product_id>[0-9]+)/$',views.addToCart, name = 'addToCart'),
    re_path(r'^addToCart/(?P<buy_id>[0-9]+)/unbuy$', views.removeFromCart, name = 'remove'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
]

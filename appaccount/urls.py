
from django.urls import path,include,reverse
from django.contrib.auth.views import LoginView, LogoutView
from appaccount.views import AccountCreateView, hello_world,AccountUserDetailView,AccountUserUpdateView,AccountUserDeleteView

#호출 쉽게 하려고 accountapp:urls
app_name="appaccount"

urlpatterns = [
   path('hello_world/',hello_world,name='hello_world'),
   path('login/', LoginView.as_view(template_name="appaccount/login.html"), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('create/',AccountCreateView.as_view(),name='create'),
   path('detail/<int:pk>', AccountUserDetailView.as_view(), name='detail'),
   path('update/<int:pk>', AccountUserUpdateView.as_view(), name='update'),
   path('delete/<int:pk>', AccountUserDeleteView.as_view(), name='delete'),
 
]
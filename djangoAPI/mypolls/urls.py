from django.contrib import admin
from django.urls import path
from mypolls.views import ItemsView , ItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', ItemsView),
    path('item/<int:nm>/', ItemView),
]
from django.urls import path
from koppee import views

urlpatterns=[
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('display/', views.display, name="display"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatepage/<int:dataid>/', views.updatepage, name="updatepage"),
    path('deletepage/<int:dataid>/', views.deletepage, name="deletepage"),
    path('catpage/',views.catpage,name="catpage"),
    path('datasave/', views.datasave, name="datasave"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('cateditpage/<int:dataid>/', views.cateditpage ,name="cateditpage"),
    path('catupdate/<int:dataid>/', views.catupdate, name="catupdate"),
    path('catdelete/<int:dataid>/', views.catdelete, name="catdelete"),
    path('coffeepage/', views.coffeepage, name="coffeepage"),
    path('coffeesave/', views.coffeesave, name="coffeesave"),
    path('coffeedisplay/',views.coffeedisplay,name="coffeedisplay"),
    path('coffeeedit/<int:dataid>/', views.coffeeedit, name="coffeeedit"),
    path('coffeeupdate/<int:dataid>/', views.coffeeupdate, name="coffeeupdate"),
    path('coffeedelete/<int:dataid>/', views.coffeedelete, name="coffeedelete"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('contpage/',views.contpage,name="contpage"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact"),
    path('logout/',views.logout,name="logout"),


]


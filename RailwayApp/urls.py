from django.urls import path
from . import views


urlpatterns = [
    path('adminIndex/', views.index, name="adminIndex"), 
    path('login/', views.login, name="login"), 
    path('loginAdmin/', views.loginAdmin, name="loginAdmin"), 
    path('adminlogout/', views.adminlogout, name="adminlogout"), 

    path('index/', views.index, name="index"), 
    path('addRail/', views.addRail, name="addRail"), 
    path('addRailPost/', views.addRailPost, name="addRailPost"),
    path('showRails/', views.showRails, name="showRails"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('updateRail/', views.updateRail, name="updateRail"),
    path('deleteRail/<int:qid>', views.deleteRail, name="deleteRail"),
    path('', views.userIndex, name="userIndex"),
    path('getDetails/<int:id>', views.getDetails, name="getDetails"),
    path('userRegister/', views.userRegister, name="userRegister"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('loginUserPost/', views.loginUserPost, name="loginUserPost"),
    path('bookTicket/', views.bookTicket, name="bookTicket"),
    path('getAllBooking/', views.getAllBooking, name="getAllBooking"),
    path('getAllBookingRequest/', views.getAllBookingRequest, name="getAllBookingRequest"),
    path('approveBooking/<int:id>', views.approveBooking, name="approveBooking"),
    path('booked/', views.booked, name="booked"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('availableBooking/', views.availableBooking, name="availableBooking"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('checkTicket/', views.checkTicket, name="checkTicket"),
    path('isTicketAvailable/', views.isTicketAvailable, name="isTicketAvailable"),
    path('booktrains/', views.booktrains, name="booktrains"),
    path('userDashboard/', views.userDashboard, name="userDashboard"),
    path('getDashDetails/<int:id>', views.getDashDetails, name="getDashDetails"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('userBooking/', views.userBooking, name="userBooking"),
    path('cancelBooking/<int:id>', views.cancelBooking, name="cancelBooking"),
    path('sendVerifyEmail', views.sendVerifyEmail, name="sendVerifyEmail"),
    path('checkUsername', views.checkUsername, name="checkUsername"),
    path('updateVerifyStatus', views.updateVerifyStatus, name="updateVerifyStatus"),
    path('getSeatNumberByUser', views.getSeatNumberByUser, name="getSeatNumberByUser"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),   # 👈 important line
]

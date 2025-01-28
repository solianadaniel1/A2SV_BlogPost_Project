
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def index(request):
    return HttpResponse(
        "Welcome to the API! Go to /blog/ to view the product list."
    )


urlpatterns = [
    path("", index, name="index"), 
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
        path('api-auth/', include('rest_framework.urls'))

]

from django.urls import path
from Multi_API_app import views
from rest_framework import urls
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('post_shooling/', views.Postdetails.as_view()),
    path('post_graduation/', views.Postdetails1.as_view()),
    path('get/',views.Get_all_details_in_one_API.as_view()),
    path('get_schooling/',views.GetSchooling.as_view()),
    path('get_gradution/',views.GetGraduation.as_view()),

]

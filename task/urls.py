from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'fill_types', views.FillTypeViewSet)
# router.register(r'areass', views.AreaViewSet)
router.register(r'type attributes',views.FillTypeAttributeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('areas', views.areass, name='areas'),
    path('area', views.area, name='fill type CRU'),

]
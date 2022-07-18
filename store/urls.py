from rest_framework import routers
from store.views import StoresGenericView, MyStores, AdminStores


router = routers.SimpleRouter()
router.register(r'stores', StoresGenericView, basename='stores')
router.register(r'my_stores', MyStores, basename='my_stores')
router.register(r'admin_stores', AdminStores, basename='admin_stores')


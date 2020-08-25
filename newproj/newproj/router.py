from login.viewsets import UsersViewset, AccountViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('detail', UsersViewset)
# print('************')
# print(AccountViewset.queryset)
router.register('create', AccountViewset)

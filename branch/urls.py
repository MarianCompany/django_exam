from django.urls import path
from branch.views import branches_list, branch_detail, api_root

urlpatterns = [
    path('branch/', branches_list, name="branches_list"),
    path('branch/<int:pk>/', branch_detail, name="branch_detail"),
    path('', api_root, name="api_root"),
]
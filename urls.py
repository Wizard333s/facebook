from django.urls import path, include

from .routers import router
from .views import (
    FacebookDataDeletion,
    CheckUserDeletionStatus,
)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
    path('facebook-data-delete/', FacebookDataDeletion.as_view()),
    path('check-status/', CheckUserDeletionStatus.as_view()),
]

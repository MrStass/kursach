from django.urls import path
from .import views
from .views import AddCommentView

app_name = "attractions"

urlpatterns = [
    path('country/<int:attractions_id>/', views.AttractionsView, name='attractions'),
    path('attractions/country/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]

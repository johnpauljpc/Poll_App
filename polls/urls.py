from django.urls import path
from .views import index, results, detail, vote
app_name = 'polls'
urlpatterns = [
	path('', index.as_view(), name='index'),
	path('detail/<int:pk>/', detail.as_view(), name = 'detail'),
	path('result/<int:pk>/', results.as_view(), name = 'results'),
	path('<int:question_id>/', vote, name = 'vote'),

]
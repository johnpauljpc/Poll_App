from django.urls import path
from .views import index, results,detail, vote

urlpatterns = [
	path('', index, name='index'),
	path('detail/<int:question_id>/', detail, name = 'detail'),
	path('result/<int:question_id>/', results, name = 'results'),
	path('<int:question_id>/', vote, name = 'vote'),

]
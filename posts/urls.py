from django.urls import path
from .views import post_list,post_detail,post_create,post_update,post_delete

app_name="posts"
urlpatterns = [
	path('',post_list,name="list"),
	path('<int:id>/',post_detail,name="detail"),
	path('create/',post_create),
	path('<int:id>/edit/',post_update,name="post_update"),
	path('<int:id>/delete/',post_delete),
]

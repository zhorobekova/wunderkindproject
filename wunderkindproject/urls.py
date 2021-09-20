"""wunderkindproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('news/', NewsViews.as_view(), name='news'),
    path('detail/<int:pk>/', DetailNews.as_view(), name='detail_news'),
    # path('comment/', comment, name='comment'),
    # path('com_detail/<int:comment_id>/comment', comment, name='comment'),
    path('author/create/',AuthorCreate.as_view(), name='create-author'),
    path('author/update/<int:pk>/',AuthorUpdate.as_view(), name='update-author'),
    path('author/delete/<int:pk>/',AuthorDelete.as_view(), name='delete-author'),
    path('readers/',readers,name='readers'),
    path('readers/create/',create_readers,name='create-readers'),
    path('readers/update/<int:read_id>/',update_readers,name='update-readers'),
    path('paginator/', index, name='paginator'),
    path('base/',NewsViews.as_view(),name='base'),

    

]

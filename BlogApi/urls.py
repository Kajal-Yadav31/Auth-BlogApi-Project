from django.urls import path
from . import views

urlpatterns = [
    path("blog_list/", views.BlogListView.as_view(), name="blog_list"),
    path("blog_create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_list"),

    path("category_list/", views.CategoryListeCreateView.as_view(),
         name="category_list"),
    path("category_detail/<int:pk>/",
         views.CategorydetailView.as_view(), name="category_detail"),

    path("blog_comment_list/blog/<int:blog_id>/",
         views.BlogCommentListCreateView.as_view(), name="blog_comment_list"),
    path("blog_comment_detail/blog/<int:blog_id>/comment/<int:comment_id>/",
         views.BlogCommentDetailView.as_view(), name="blog_comment_detail"),
]
# path('blog_detail/<int:pk>/',
#      views.BlogDetailView.as_view(), name="blog_details"),
# path('category_list/', views.CategoryListView.as_view(), name="category_view"),
# path('category_detail/<int:pk>/',
#      views.CategoryDetailView.as_view(), name="category_details"),
# path('blog_genericview/', views.BlogListGenericView.as_view(),
#      name="blog_genericview"),
# path('blog_detail_genericview/<str:slug>/', views.BlogDetailGenericView.as_view(),
#      name="blog_detail_genericview"),

# <---------Concrete View Class------------->

# path('blog_create_api/', views.BlogCreateConcreate.as_view(),
#      name="blog_create_api"),
# path('blog_list_api/', views.BlogListConcreate.as_view(),
#      name="blog_list_api"),
# path('blog_retrive_api/<str:slug>/', views.BlogRetriveConcreate.as_view(),
#      name="blog_retrive_api"),
# path('blog_delete_api/<int:pk>/', views.BlogDestroyConcreate.as_view(),
#      name="blog_delete_api"),

# path('blog_delete_and_retrive_api/<int:pk>/', views.BlogRetrive_DestroyCon.as_view(),
#      name="blog_delete_and_retrive_api"),

# path('blog_create_and_list_api/<int:pk>/', views.BlogList_create_Con.as_view(),
#      name="blog_create_and_list_api"),

# path('blog_RUD_api/<int:pk>/', views.BlogRUDApiView.as_view(),
#      name="blog_RUD_api"),

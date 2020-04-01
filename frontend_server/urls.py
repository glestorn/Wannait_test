from django.urls import path
from .views import RecommendationsView
from .views import LikeView
from .views import CommentView
from .views import DislikeView
from .views import OwnedProductsView
from .views import DeleteProductView
from .views import ProductInfoView
from .views import ChangeProductView
from .views import CreateProductView

from .views import login_view
from .views import logout_view
from .views import register_view


app_name = 'frontend_server'


urlpatterns = [
    path('', RecommendationsView.as_view(), name='index'),
    path('owned', OwnedProductsView.as_view(), name='owned'),
    path('delete/', DeleteProductView.as_view(), name='delete'),
    path('info/<int:id>', ProductInfoView.as_view(), name='info'),
    path('changeproduct/<int:product_id>', ChangeProductView.as_view(),
         name='changeproduct'),
    path('addnewproduct/', CreateProductView.as_view()),
    path('like/', LikeView.as_view(), name='like'),
    path('dislike/', DislikeView.as_view(), name='dislike'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('accounts/signin/', login_view, name='signin'),
    path('accounts/signup/', register_view, name='signup'),
    path('accounts/signout/', logout_view, name='signout')
]

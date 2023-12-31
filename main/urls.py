from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id , increment_amount, decrement_amount, delete_item, get_product_json, add_product_ajax
from main.views import register , create_product_flutter
from main.views import login_user
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('increment_amount/<int:item_id>/', increment_amount, name='increment_amount'),
    path('decrement_amount/<int:item_id>/', decrement_amount, name='decrement_amount'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax')

]
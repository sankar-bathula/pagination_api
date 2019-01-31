from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
	page_size = 5 #max_number of records for page
	page_query_param = 'mypage' # http://127.0.0.1:8000/api/?mypage=10
	page_size_query_param = 'num'
	max_page_size = 11
	last_page_strings = ('end_page',)


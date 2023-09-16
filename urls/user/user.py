from flask import Blueprint, request,g
from views.user.city_list import CityListController, UserListController
from views.user.test_files import TestInsertController

from views.user.user_view import ListController, SearchController, TestListController, UserDetailsController

user_bp = Blueprint('user', __name__)



##
@user_bp.route("/city", methods=["GET"])
def city_list():
  ct = request.args.get("ct", default=0)
  ac = request.args.get("ac", default=0)
  pt = request.args.get("pt", default=0)

  # if ct == 0:
  #   return {"data":False, "respMessage":"Data not found", "pageNum":0}

  return CityListController('all_dist', ct, int(ac), int(pt))



##
@user_bp.route("/details", methods=["POST"])
def user_details():
  data = request.get_json()

  if data is None or len(data.keys()) == 0:
    return {"data":False, "respMessage":"Data not found", "pageNum":0}

  return UserDetailsController('user_details', data)



# ##
# @user_bp.route("/user-details", methods=["POST"])
# def user_details():
#   data = request.get_json()

#   if data is None or len(data.keys()) == 0:
#     return {"data":False, "respMessage":"Data not found", "pageNum":0}

#   return UserDetailsController('user_details', data)







# @user_bp.route('/')
# def index():
#     return "This is an example app"
'''

@user_bp.route('/')
def list_user():
  limit = request.args.get("l", default=10)
  page  = int(request.args.get("p", default=1))

  select_columns = ["id","user_id","first_name","last_name","initials","user_name","user_email","phone_number",
  "country","(select `country_name` from toc_country_list where toc_country_list.cid=toc_user.country) as country_name",
  "(select  `full_name` from `toc_address_book_details` where `toc_address_book_details`.id=`toc_user`.organization) as organization", "organization as web_organization",
  "subscription_id","(select `company_name` from `toc_subscriber_info` where `toc_subscriber_info`.id=`toc_user`.subscription_id) as subscription_company",
  "designation","(select  `designation` from `toc_user_designation` where `toc_user_designation`.id=`toc_user`.designation) as designation_name",
  "user_status","(select sl_name from toc_status_list where toc_status_list.id=toc_user.user_status) as user_status_name"
 ]

  
  return ListController('all_dist', ",".join(select_columns), None, limit, page)




@user_bp.route('/search')
def list_user_search():
  limit = request.args.get("l", default=10)
  page  = int(request.args.get("p", default=1))

#   select_columns = ["id","user_id","first_name","last_name","initials","user_name","user_email","phone_number",
#   "country","(select `country_name` from toc_country_list where toc_country_list.cid=toc_user.country) as country_name",
#   "(select  `full_name` from `toc_address_book_details` where `toc_address_book_details`.id=`toc_user`.organization) as organization", "organization as web_organization",
#   "subscription_id","(select `company_name` from `toc_subscriber_info` where `toc_subscriber_info`.id=`toc_user`.subscription_id) as subscription_company",
#   "designation","(select  `designation` from `toc_user_designation` where `toc_user_designation`.id=`toc_user`.designation) as designation_name",
#   "user_status","(select sl_name from toc_status_list where toc_status_list.id=toc_user.user_status) as user_status_name"
#  ]

  
  return UserListController('test_user_details', None, limit, page)









@user_bp.route("/search", methods=["POST"])
def tco_save():
  data = request.get_json()
  rl = request.args.get("rl", default=0)
  rr = request.args.get("rr", default=0)

  if data is None or len(data.keys()) == 0:
    return {"data":False, "respMessage":"Data not found", "pageNum":0}

  return SearchController('toc_tco_general_details', data, int(rl), int(rr))






@user_bp.route('/test')
def test():
  limit = request.args.get("l", default=10)
  page  = int(request.args.get("p", default=1))

  select_columns = ["id","first_name","last_name"
 ]

  
  return TestListController('table_test', ",".join(select_columns), None, limit, page)



@user_bp.route('/insert')
def test_insert():

  
  return TestInsertController('all_dist')
  '''
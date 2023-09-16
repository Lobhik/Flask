
import json

from flask import jsonify
from comman_use.comman import mandatoryCheck
from models.models import BaseModel
import pandas as pd

##
def UserDetailsController(table_name, post_data):

  # list1=["first_name",""]
  # flag=mandatoryCheck(list1,post_data)
  # if(flag==0):
  #   return {"data":False, "respMessage":"Please enter all mandatory fields !", "pageNum":0}
  

  bm = BaseModel(table_name)
  where_clause = "name LIKE '{}%'".format(post_data['name'])
  

  select_columns = ["sr_no","name","ac_no","part_no",
    "(select part_name from all_dist where ass_no = user_details.ac_no AND part_no = user_details.part_no) as village_name",
    "(select dist from all_dist where ass_no = user_details.ac_no AND part_no = user_details.part_no) as district" 
    ]

  #order_by = "id DESC"

  
  rows = bm.selectAll(select_column=",".join(select_columns), where_clause=where_clause, limit=0)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return jsonify(rows)
  else:
    return {"data":False, "msg":"Unble to process the data"}













def ListController(table_name, column_select, filter, limit, page):
  bm = BaseModel(table_name)
  where_clause = "`{}`.`status` = 1".format(table_name)
  
  # if filter is not None and 'where' in filter:
  #   if isinstance(filter['where'], str) == True:
  #     filter = json.loads(filter)
    
  #   filter['where']['AND'] = {'status': 1}
  #   if 'country_name' in filter['where']:
  #       filter['where']['country'] = {'in': '(SELECT cid FROM `toc_country_list` WHERE country_name LIKE "%{}%")'.format(filter['where']['country_name']['l'])}
  #       filter['where'].pop('country_name')
      
  #   if 'designation_name' in filter['where']:
  #     filter['where']['designation'] = {'in': '(SELECT id FROM `toc_user_designation` WHERE designation LIKE "%{}%")'.format(filter['where']['designation_name']['l'])}
  #     filter['where'].pop('designation_name')
    
  #   if 'organization_name' in filter['where']:
  #     filter['where']['organization'] = {'in': '(SELECT id FROM `toc_address_book_details` WHERE short_name LIKE "%{}%")'.format(filter['where']['organization_name']['l'])}
  #     filter['where'].pop('organization_name')
  #   where_clause = filter['where']


  order_by = "id DESC"
  if filter is not None and 'order_by' in filter:
    order_by = filter['order_by']

  
  rows = bm.selectAll(select_column='*', limit=limit, page=page, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return jsonify(rows)
  else:
    return jsonify(False)






def SearchController(table_name, post_data, filter, limit, page):


  list1=["vessel","my_company","v_status","owner","ownership_type"]
  flag=mandatoryCheck(list1,post_data)
  if(flag==0):
    return {"data":False, "respMessage":"Please enter all mandatory fields !", "pageNum":0}
  


  bm = BaseModel(table_name)
  where_clause = "`{}`.`status` = 1".format(table_name)
  
  if filter is not None and 'where' in filter:
    if isinstance(filter['where'], str) == True:
      filter = json.loads(filter)
    
    filter['where']['AND'] = {'status': 1}
    if 'country_name' in filter['where']:
        filter['where']['country'] = {'in': '(SELECT cid FROM `toc_country_list` WHERE country_name LIKE "%{}%")'.format(filter['where']['country_name']['l'])}
        filter['where'].pop('country_name')
      
    if 'designation_name' in filter['where']:
      filter['where']['designation'] = {'in': '(SELECT id FROM `toc_user_designation` WHERE designation LIKE "%{}%")'.format(filter['where']['designation_name']['l'])}
      filter['where'].pop('designation_name')
    
    if 'organization_name' in filter['where']:
      filter['where']['organization'] = {'in': '(SELECT id FROM `toc_address_book_details` WHERE short_name LIKE "%{}%")'.format(filter['where']['organization_name']['l'])}
      filter['where'].pop('organization_name')
    where_clause = filter['where']


  order_by = "id DESC"
  if filter is not None and 'order_by' in filter:
    order_by = filter['order_by']

  
  rows = bm.selectAll(select_column="*", where_clause=where_clause, limit=limit, page=page, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return {"data":rows}
  else:
    return {"data":False}






def TestListController(table_name, column_select, filter, limit, page):
  bm = BaseModel(table_name)
  where_clause = "`{}`.`status` = 1".format(table_name)
  
  # if filter is not None and 'where' in filter:
  #   if isinstance(filter['where'], str) == True:
  #     filter = json.loads(filter)
    
  #   filter['where']['AND'] = {'status': 1}
  #   if 'country_name' in filter['where']:
  #       filter['where']['country'] = {'in': '(SELECT cid FROM `toc_country_list` WHERE country_name LIKE "%{}%")'.format(filter['where']['country_name']['l'])}
  #       filter['where'].pop('country_name')
      
  #   if 'designation_name' in filter['where']:
  #     filter['where']['designation'] = {'in': '(SELECT id FROM `toc_user_designation` WHERE designation LIKE "%{}%")'.format(filter['where']['designation_name']['l'])}
  #     filter['where'].pop('designation_name')
    
  #   if 'organization_name' in filter['where']:
  #     filter['where']['organization'] = {'in': '(SELECT id FROM `toc_address_book_details` WHERE short_name LIKE "%{}%")'.format(filter['where']['organization_name']['l'])}
  #     filter['where'].pop('organization_name')
  #   where_clause = filter['where']


  order_by = "id DESC"
  if filter is not None and 'order_by' in filter:
    order_by = filter['order_by']

  
  rows = bm.selectAll(select_column='*', limit=limit, page=page, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return jsonify(rows)
  else:
    return jsonify(False)
  







from flask import jsonify

from models.models import BaseModel


def UserListController(table_name, filter, limit, page):
  bm = BaseModel(table_name)
  #test_user_details
  where_clause = "`{}`.`status` = 1".format(table_name)
  
  select_columns = ["id","sr_no","full_name","ac_no","part_no",
    "(select part_name from all_dist where ass_no = test_user_details.ac_no AND part_no = test_user_details.part_no) as village_name" 
    ]
  order_by = "id DESC"
  if filter is not None and 'order_by' in filter:
    order_by = filter['order_by']

  
  rows = bm.selectAll(select_column= ",".join(select_columns), limit=limit, page=page, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return jsonify(rows)
  else:
    return jsonify(False)
  






def UserListController(table_name, filter, limit, page):
  bm = BaseModel(table_name)
  #test_user_details
  where_clause = "`{}`.`status` = 1".format(table_name)
  
  select_columns = ["id","sr_no","full_name","ac_no","part_no",
    "(select part_name from all_dist where ass_no = test_user_details.ac_no AND part_no = test_user_details.part_no) as village_name" 
    ]
  order_by = "id DESC"
  if filter is not None and 'order_by' in filter:
    order_by = filter['order_by']

  
  rows = bm.selectAll(select_column= ",".join(select_columns), limit=limit, page=page, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return jsonify({"data":rows})
  else:
    return jsonify(False)
  





def CityListController(table_name, ct, ac, pt):
  bm = BaseModel(table_name)
  #test_user_details
  if ct is not None:
    where_clause = "`dist` Like '{}'".format(ct)
    if ac > 0:
      where_clause = " `dist` Like '{}' AND `ass_no` = {}".format(ct,ac)
      if pt > 0:
        where_clause = "`dist` Like '{}' AND `ass_no` = {} AND `part_no` = {}".format(ct,ac,pt)

  
  select_columns = ["id","ass_no","as_name","part_no","part_name","dist"

    ]
  order_by = "id DESC"

  
  rows = bm.selectAll(select_column= ",".join(select_columns),where_clause= where_clause, limit=10, page=1, order_by=order_by)
  if type(rows) is not str:
    rowCount = bm.countAll(where_clause=where_clause)
    return {"data":rows}
  else:
    return {False}
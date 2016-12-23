# encoding=utf8
from jinja2 import *


sql='''
with result as
(select sum(cnt) as total_cnt from rpt_qta_order_booking_plat_fail)
select
    err_sys,
    sum(cnt) as cnt,
    total_cnt,
    round(sum(cnt)/total_cnt::decimal * 100,2)::text||'%%' as total_rate
from rpt_qta_order_booking_plat_fail,result
where true
{% if start_date and end_date %} and date>={{start_date}} and date<={{end_date}} {% endif %}
{% if booking_source %}and booking_source in ({{booking_source}}){% endif %}
{% if wrapper_list is undefined %} xxx {% endif %}
group by err_sys, result.total_cnt
'''
wrapper_id=''
template=Template(sql)
print template.render(start_date='2016-11-25',end_date='2016-11-28',booking_source='stc',wrapper_list=wrapper_id)


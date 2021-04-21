select * from
(select '大于160' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('㎡')))) as jzmj
from ershoufang_chengjiao) where jzmj >160)

create view v_zxt_fj as--折线图最近三年房价
(select year,month,round(avg(sqmeter),1) as sqmeter from
(select substr(to_char(to_date(gpsj,'yyyy/mm/dd'),'yyyymmdd'),1,4) as year,
substr(to_char(to_date(gpsj,'yyyy/mm/dd'),'yyyymmdd'),5,2) as month,sqmeter
from ershoufang_chengjiao)
where year='2018'
group by year,month)

select * from v_zxt_fj order by year,month

select f.month,f.y2018,f.y2019,g.y2020 from 
(select d.month,d.y2018,e.y2019 from
(select a.month,a.sqmeter as y2018 from v_zxt_fj a where a.year='2018') d left join
(select b.month,b.sqmeter as y2019 from v_zxt_fj b where b.year='2019') e on d.month=e.month) f left join
(select c.month,c.sqmeter as y2020 from v_zxt_fj c where c.year='2020') g on f.month=g.month
order by f.month


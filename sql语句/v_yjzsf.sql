create view v_yjzsf as--预计在售房
(select * from
(select (t.areanamebig || t.communityname) as xq,t.price,t.price-v.jj as yj_price,t.sqmeter,v.SQMETER as avg_sqmeter,v.CJZQ,t.fwhx,t.szlc,t.jzmj,t.fwcx,t.zxqk,t.thbl
from ershoufang_zaishou t right join v_rd_jj v on t.communityname=v.COMMUNITYNAME
order by rd desc))

select * from v_rd_jj

select * from ershoufang_zaishou

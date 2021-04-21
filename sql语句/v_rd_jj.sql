select * from ershoufang_chengjiao

create view v_rd_jj as--热度，平均降价
(select * from
(select round(avg(jj),1) as jj,sum(rd) as rd,round(avg(cjzq),1) as cjzq,round(avg(sqmeter),1) as sqmeter,communityname from
(select * from
(select gpjg,gpjg-price as jj,round(ll/cjzq,1) as rd,cjzq,communityname,areanamebig,areanamesmall,sqmeter from ershoufang_chengjiao
where ll is not null and communityname !='"wrapper"'
order by rd desc)
where rd>200)
group by communityname
order by rd desc)
where rd >800)


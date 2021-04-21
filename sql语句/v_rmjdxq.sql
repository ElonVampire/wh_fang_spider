select * from ershoufang_chengjiao

create view v_rmjdxq as--热门街道小区
select * from
(select sum(rd) as rd,round(avg(cjzq),1) as cjzq,round(avg(sqmeter),1) as sqmeter,areanamesmall,areanamebig from
(select * from
(select round(ll/cjzq,1) as rd,cjzq,communityname,areanamebig,areanamesmall,sqmeter from ershoufang_chengjiao
where ll is not null
order by rd desc)
where rd>100)
group by areanamebig,areanamesmall
order by rd desc)

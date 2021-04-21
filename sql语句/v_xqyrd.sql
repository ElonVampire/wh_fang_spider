select (areanamebig || communityname) as communityname,count(*) as he from ershoufang_chengjiao
where communityname != '"wrapper"' and communityname is not null and areanamebig is not null and communityname != 'Ñô'
group by areanamebig,communityname order by he desc

select avg(sqmeter) from
(select substr(to_char(to_date(gpsj, 'yyyy/mm/dd'),'yyyymmdd'),1,6) as sj,sqmeter from ershoufang_chengjiao)
where sj = '202103'

select * from ershoufang_chengjiao


select sum(rd) as rd,round(avg(cjzq),1) as cjzq,round(avg(sqmeter),1) as sqmeter,areanamesmall,areanamebig from
(select * from
(select round(ll/cjzq,1) as rd,cjzq,communityname,areanamebig,areanamesmall,sqmeter from ershoufang_chengjiao
where ll is not null
order by rd desc)
where rd>100)
group by areanamebig,areanamesmall
order by rd desc

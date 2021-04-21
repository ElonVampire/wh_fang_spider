create view v_esfl as --二手房量
select * from
(select gpsj,sum(he) as he from
(select substr(to_char(to_date(gpsj,'yyyy/mm/dd'),'yyyymmdd'),1,6) as gpsj,he from
(select gpsj,count(*) as he from ershoufang_zaishou
group by gpsj
union
select gpsj,count(*) as he from ershoufang_chengjiao
group by gpsj))
group by gpsj
order by gpsj)

select * from ershoufang_chengjiao

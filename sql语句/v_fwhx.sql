
select * from
(select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where rownum <8

select rownum,t.* from
(select sum(he) as he from (select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where fwhx not in 
(select fwhx from
(select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where rownum <8)) t

select rownum, a.* from (select '其他' as fwhx from dual) a


create view v_fwhx as--房屋户型对比
select * from
(select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where rownum <8
union
select b.fwhx,c.he from (select a.* from (select '其他' as fwhx from dual) a) b
cross join 
(select sum(he) as he from (select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where fwhx not in 
(select fwhx from
(select fwhx,count(*) as he from ershoufang_chengjiao group by fwhx order by he desc)
where rownum <8)) c

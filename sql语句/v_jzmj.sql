create view v_jzmj as --��������Ա�
(select * from
(select '����160' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj >160)
union
select * from
(select '140-160' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj between 140 and 160)
union
select * from
(select '120-140' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj between 120 and 140)
union
select * from
(select '100-120' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj between 100 and 120)
union
select * from
(select '80-100' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj between 80 and 100)
union
select * from
(select '60-80' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj between 60 and 80)
union
select * from
(select 'С��60' as mj from dual) cross join
(select count(*) as he from
(select to_number(substr(jzmj,1,(length(jzmj)-length('�O')))) as jzmj
from ershoufang_chengjiao) where jzmj < 60))

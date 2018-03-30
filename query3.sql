create view totalerrors as (
  select time::date as day, count(*) as errors
  from log where status like '4%'
  group by day
)

create view totalperday as (
  select time::date as day, count (*) as total
  from log group by day
)

select day, round(pcter, 2) as pcter from
(select te.day as day, (te.errors::decimal/td.total::decimal)*100 as pcter
from totalerrors te join totalperday td
on te.day = td.day) as calc
where pcter > 1
order by pcter;

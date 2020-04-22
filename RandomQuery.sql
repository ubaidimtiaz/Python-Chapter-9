with Temp as
(
select
names,
split_part(petting_start,' ',2) as p_start,
split_part(petting_end,' ',2) as p_end

from cat_petting.pet_detection
)
--select p_date, min(p_start), max(p_end) from Temp
--group by p_date;

select Temp.names, cat_petting.entry_times.entry_start, min(p_start), max(p_end)
from cat_petting.entry_times inner join Temp
on cat_petting.entry_times.names = Temp.names
group by Temp.names, cat_petting.entry_times.entry_start;


select split_part(cat_petting.pet_detection.names,' ',1) as firstname,
       split_part(cat_petting.pet_detection.names,' ',2) as lastname





from cat_petting.pet_detection
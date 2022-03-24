# Update inconsistent apostrophe types that were breaking joins on name
update items_data
set name = replace(name, '’', '''');

update melee_data
set name = replace(name, '’', '''');

update ranged_data_temp
set name = replace(name, '’', '''');

update sacredseal_data
set name = replace(name, '’', '''');


UPDATE t2
JOIN t1 ON t2.name = t1.name
SET t2.id = t1.id;

select name, count(name)
from items_data
group by name
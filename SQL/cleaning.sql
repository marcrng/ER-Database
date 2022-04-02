# Update inconsistent apostrophe types that were breaking joins on name
update items_data
set name = replace(name, '’', '''');

update melee_data
set name = replace(name, '’', '''');

update ranged_data_temp
set name = replace(name, '’', '''');

update sacredseal_data
set name = replace(name, '’', '''');


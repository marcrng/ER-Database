# Create items_data masterlist
create table items_data
(
    id        int  not null auto_increment primary key,
    name      text not null,
    item_type text not null
);

# Create melee datatable
CREATE TABLE melee_data
(
    id          int,
    name        varchar(255) not null,
    atkPhysical int,
    defPhysical int,
    atkMagic    int,
    defMagic    int,
    atkFire     int,
    defFire     int,
    atkLight    int,
    defLight    int,
    atkHoly     int,
    defHoly     int,
    crit        int,
    guardBoost  int,
    strReq      int,
    strScaling  char,
    dexReq      int,
    dexScaling  char,
    intReq      int,
    intScaling  char,
    faiReq      int,
    faiScaling  char,
    arcReq      int,
    arcScaling  char,
    weight      double,
    skill       varchar(255),
    foreign key (id) references items_data (id)
);

# Insert id's
update melee_data ss
    join items_data i on ss.name = i.name
set ss.id = i.id;

create table ranged_data
(
    id          int,
    name        TEXT   null,
    atkPhysical INT    null,
    defPhysical TEXT   null,
    `range`     INT    null,
    atkMagic    int    null,
    defMagic    int    null,
    atkFire     int    null,
    defFire     int    null,
    atkLight    int    null,
    defLight    int    null,
    atkHoly     int    null,
    defHoly     int    null,
    crit        INT    null,
    guardBoost  int    null,
    strReq      int    null,
    strScaling  text   null,
    dexReq      INT    null,
    dexScaling  TEXT   null,
    intReq      int    null,
    intScaling  TEXT   null,
    faiReq      int    null,
    faiScaling  TEXT   null,
    arcReq      int    null,
    arcScaling  TEXT   null,
    weight      DOUBLE null,
    skill       TEXT   null,
    foreign key (id) references items_data (id)
);

insert into ranged_data(name, atkPhysical, defPhysical, `range`, atkMagic, defMagic, atkFire, defFire, atkLight,
                        defLight, atkHoly, defHoly, crit, guardBoost, strReq, strScaling, dexReq, dexScaling, intReq,
                        intScaling, faiReq, faiScaling, arcReq, arcScaling, weight, skill)
select name,
       atkPhysical,
       defPhysical,
       `range`,
       atkMagic,
       defMagic,
       atkFire,
       defFire,
       atkLight,
       defLight,
       atkHoly,
       defHoly,
       crit,
       guardBoost,
       strReq,
       strScaling,
       dexReq,
       dexScaling,
       intReq,
       intScaling,
       faiReq,
       faiScaling,
       arcReq,
       arcScaling,
       weight,
       skill
from ranged_data_temp;


create table sacredSeal_data
(
    id          int,
    name        TEXT   null,
    atkPhysical INT    null,
    defPhysical INT    null,
    atkMagic    int    null,
    defMagic    int    null,
    atkFire     int    null,
    defFire     int    null,
    atkLight    int    null,
    defLight    int    null,
    atkHoly     INT    null,
    defHoly     int    null,
    crit        INT    null,
    guardBoost  DOUBLE null,
    atkIncant   INT    null,
    strReq      INT    null,
    strScaling  TEXT   null,
    dexReq      INT    null,
    dexScaling  TEXT   null,
    intReq      INT    null,
    intScaling  TEXT   null,
    faiReq      INT    null,
    faiScaling  TEXT   null,
    arcReq      INT    null,
    arcScaling  TEXT   null,
    weight      DOUBLE null,
    skill       TEXT   null,
    foreign key (id) references items_data (id)
);

insert into sacredSeal_data(name, atkPhysical, defPhysical, atkMagic, defMagic, atkFire, defFire, atkLight, defLight,
                            atkHoly, defHoly, crit, guardBoost, atkIncant, strReq, strScaling, dexReq, dexScaling,
                            intReq, intScaling, faiReq, faiScaling, arcReq, arcScaling, weight, skill)
select name,
       atkPhysical,
       defPhysical,
       atkMagic,
       defMagic,
       atkFire,
       defFire,
       atkLight,
       defLight,
       atkHoly,
       defHoly,
       crit,
       guardBoost,
       atkIncant,
       strReq,
       strScaling,
       dexReq,
       dexScaling,
       intReq,
       intScaling,
       faiReq,
       faiScaling,
       arcReq,
       arcScaling,
       weight,
       skill
from sacredseal_data_temp;

create table staff_data
(
    name        TEXT   null,
    atkPhysical INT    null,
    defPhysical INT    null,
    atkMagic    int    null,
    defMagic    int    null,
    atkFire     int    null,
    defFire     int    null,
    atkLight    int    null,
    defLight    int    null,
    atkHoly     INT    null,
    defHoly     int    null,
    crit        INT    null,
    guardBoost  DOUBLE null,
    strReq      INT    null,
    strScaling  TEXT   null,
    dexReq      INT    null,
    dexScaling  TEXT   null,
    intReq      INT    null,
    intScaling  TEXT   null,
    faiReq      INT    null,
    faiScaling  TEXT   null,
    arcReq      INT    null,
    arcScaling  TEXT   null,
    weight      DOUBLE null,
    skill       TEXT   null,
    type varchar(255) null
);

alter table staff_data
add column id int;

alter table staff_data
add foreign key (id) references items_data(id);

# Insert id's
update staff_data ss
    join items_data i on ss.name = i.name
set ss.id = i.id;

# Add weapon type to tables
alter table melee_data
add column type varchar(255);

alter table melee_data
add column type varchar(255);

alter table melee_data
add column type varchar(255)

#TODO: add skills table with fp cost values
#TODO: add spells table with damage and fp cost
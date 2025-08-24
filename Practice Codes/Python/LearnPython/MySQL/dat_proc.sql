create procedure dat (f_name varchar, l_name varchar, company varchar, age number) is

begin
    insert into test_table values(f_name, l_name, company, age);
    commit;
end;
/
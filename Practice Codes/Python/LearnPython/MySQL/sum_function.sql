create or replace function testsum() return number is 
res number;
BEGIN
    num1 number:=50;
    num2 number:=50
    res := num1+num2;
    return res;
end;
/
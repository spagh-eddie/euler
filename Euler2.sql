create table fibonacci as
  with f(i, curr, last) as (
    select 1, 1, 0 union
    select 2, 1, 1 union
    select i+1, curr + last, curr from f where curr + last < 4000000
  )
  with helper(fib) as (
    select curr from f where curr%2==0
  )
  select sum(fib) from helper;

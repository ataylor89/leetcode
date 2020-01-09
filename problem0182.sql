select Email from (
    select Email, count(*) N from Person 
    group by Email
) X where N > 1

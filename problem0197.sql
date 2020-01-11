select Id from
(select today.Id from Weather today 
 left outer join Weather yesterday 
 on yesterday.RecordDate = DATE_SUB(today.RecordDate, INTERVAL 1 DAY)
 where today.Temperature > yesterday.Temperature) X

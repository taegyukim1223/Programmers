CREATE EXTERNAL TABLE IF NOT EXISTS ratings(
posted timestamp,
cust_id int,
prod_id int,
rating tinyint,
message string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/cloudera/ratings';

select prod_id, avg(rating) as avg_rating, count(*)
from ratings
group by prod_id
having count(*) >= 50
order by avg_rating
limit 1;

select ngrams(sentences(lower(message)),3,5)
from ratings
where prod_id = 1274673;

ngram 명령어?

select distinct message
from ratings
where prod_id = 1274673 and message like '%red%'
limit 10;


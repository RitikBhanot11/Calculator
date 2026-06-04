create database market_analysis;
use market_analysis;
show tables;
select * from dataset limit 5;
describe dataset;

#1. Which age group generates the most revenue?
select age_group, round(sum(total_price),2) as total_earn
from dataset
group by age_group
order by total_earn desc
limit 1;

#2. Which age group places the most orders?
select age_group, sum(quantity) as total_order
from dataset
group by age_group
order by total_order desc
limit 1;

#3. Which city generates the highest revenue?
select city, round(sum(total_price),2) as total_earn
from dataset
group by city
order by total_earn desc
limit 1;

#4. Which country has the most customers?
select city, count(*) as total_customers
from dataset
group by city
order by total_customers desc
limit 1;

#5. Which product category is the most popular?
select category, count(*) as total_purchases
from dataset
group by category
order by total_purchases desc
limit 1;

#6. Which product category generates the most revenue?
select category, round(sum(total_price),2) as total_earn_by_cat
from dataset
group by category
order by total_earn_by_cat desc
limit 1;

#7. What products are most frequently purchased by each age group?
select age_group, category, count(*) as total_purchases
from dataset
group by age_group, category
order by age_group, total_purchases desc;

#8. What is the average order value for each age group?
select age_group, round(avg(total_price),2) as avg_earn
from dataset
group by age_group;

#9. Who are the top-spending customers by country?
select country, round(sum(total_price),2) as total_earn
from dataset
group by country
order by country desc
limit 1;

#10. What are the number of customers more than 3 products?
SELECT COUNT(*) AS num_customers
FROM (
    SELECT customer_id
    FROM dataset
    GROUP BY customer_id
    HAVING SUM(quantity) > 3
) t;

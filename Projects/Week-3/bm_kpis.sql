#Brand


select brand, (sum(stockraw)/ (select sum(stockraw) from computer)*100)as stock_rate
from computer
group by 1
order by 2 desc; # In Stock: HP (33%), Dell(29%) Lenovo(19%), Apple(15%)


select brand, count(distinct title)
from computer
group by 1
order by 2 desc; # 107 Different Articles provided by Apple vs 46 Dell and HP


# Discounts

## Product with the highest discount:


select *, (price_new-price)/price_new as discount 
from computer
order by  discount desc; Lenovo 

create temporary table discount
select *, (price_new-price)/price_new as discount 
from computer
order by  discount desc;# 80% # is the highest discount for a Lenovo 

#Avg DIscount
select brand, avg(discount)
from discount
group by 1
order by 1 desc ;  # Fujitsu  products are the most discounted ones (--> having a deeper look there is only 1 title for F.)

select *
from computer
where title like 'F%';


select brand,max(price)
from computer
group by 1
order by 2 desc; # no surprises the most expensive product is sold by Apple for 2783 euros

select brand,price
from computer
order by 2
asc; #The cheapest product is sold by HP 79 euros

# Quality: Stallone, Eta Correct, Bon Etat, Tres Bone Etat, Comme Neuf

select brand, state_label as quality, avg(price)
from computer
group by 1,2
order by 2; 


# Considering avg price and quality: ( not taking into consideration all the other features)
# Stallone: around 400 euros (except for Aplle 800)
# Eta Correct: Between 300 and 500 (except for Apple >1000)
# Tres Bon Eta: Between 300 and 600 (except for Apple >1000)
# Comme Neuf: Betweenn 400 and 550 (except Apple>1200)

 
# Processor Speed

select distinct processor_speed, title
from computer
order by 1 desc ;
# The product with the highes processor speed is a Mac Mini

select brand, processor_speed, count(title)
from computer
group by 1,2
order by 2 desc; # computer with the higher processor speed (3.6) is by Apple vs 3,4 by Dell and HP


select * from computer where brand is null;


select price=price_new
from computer; # Back Market has descreases its price for real :))

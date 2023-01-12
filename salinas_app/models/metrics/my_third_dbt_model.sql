select 
    crime, 
    count (crime) as crime_count
    --    sum(num_crimes) / count(distinct date) as avg_crimes_per_day,
    --    sum(num_crimes) / count(distinct date) / count(distinct crime_type) as avg_crimes_per_day_per_type,
    --    sum(num_crimes) / count(distinct date) / count(distinct crime_type) / count(distinct neighborhood) as avg_crimes_per_day_per_type_per_neighborhood
from {{source ('source', 'crime_data')}}
group by 1
ORDER BY 2 DESC
LIMIT 10
# Write your MySQL query statement below
# first get volume per product 


select w.name as WAREHOUSE_NAME, sum(p.Width * p.Length * p.Height * w.units) as VOLUME from Warehouse w join Products p on w.product_id = p.product_id group by w.name;
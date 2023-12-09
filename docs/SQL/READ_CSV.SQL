COPY customers(customer_id,first_name,last_name,phone,email,street,city,state,zip_code)
FROM 'C:\Users\PC\Documents\GitHub\Projeto_03_ADA\docs\csv\customers.csv'
DELIMITER ','
CSV HEADER;
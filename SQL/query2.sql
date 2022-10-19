SELECT client_id,
       sum(case when product_type="MEUBLE" then transaction_amount else 0 end) AS ventes_meuble,
       sum(case when product_type="DECO" then transaction_amount else 0 end) AS ventes_deco


FROM ( 
Select client_id,product_type,sum(prod_price * prod_qty) as 'transaction_amount'
FROM Transaction
INNER JOIN PRODUCT_NOMENCLATURE ON Transaction.prod_id = PRODUCT_NOMENCLATURE.prod_id
WHERE date BETWEEN "2020-01-01" AND "2020-12-31"
GROUP BY client_id,product_type ) AS X


GROUP BY X.client_id

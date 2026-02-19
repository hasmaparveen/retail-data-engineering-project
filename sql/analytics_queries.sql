-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM fact_sales;

-- Revenue by Category
SELECT category, SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY category
ORDER BY revenue DESC;

-- Top 5 Customers by Revenue
SELECT customer_id, SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 5;

-- Monthly Sales Trend
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;

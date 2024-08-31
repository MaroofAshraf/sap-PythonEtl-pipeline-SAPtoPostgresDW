CREATE VIEW material_summary AS
SELECT MATERIAL, COUNT(*) AS total, AVG(PRICE) AS avg_price
FROM materials
GROUP BY MATERIAL;

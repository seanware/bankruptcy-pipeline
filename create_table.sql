--table for bankruptcy data
DROP TABLE IF EXISTS companies;

CREATE TABLE IF NOT EXISTS companies (
  id serial PRIMARY KEY,
  district VARCHAR(3),
  state VARCHAR(3),
  company_name VARCHAR(50),
  assets NUMERIC(8,2),
  liabilities NUMERIC(8, 2)
  );

--load csv file cases
COPY companies(district, state, company_name, assets, liabilities)
FROM '/cases.csv'
DELIMITER ','
CSV HEADER;
--sql test
SELECT * FROM companies
LIMIT 10;

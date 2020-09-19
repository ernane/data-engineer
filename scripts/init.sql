\c data_engineer

CREATE SEQUENCE IF NOT EXISTS seq_customer;
CREATE TABLE IF NOT EXISTS customers (
  id_customer int default nextval('seq_customer'::regclass) PRIMARY KEY,
  first_name varchar(100),
  last_name varchar(100),
  email varchar(100)
);

\l
\c data_engineer
\d customers
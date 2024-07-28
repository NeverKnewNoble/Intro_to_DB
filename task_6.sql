-- Ensure you are using the correct database
USE alx_book_store;

-- Insert multiple rows into the customer table
INSERT INTO customer (customer_id, customer_name, email, address) VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');

-- Check for the insertion of specific customer records
SELECT * FROM customer WHERE customer_id = 2;
SELECT * FROM customer WHERE customer_id = 3;
SELECT * FROM customer WHERE customer_id = 4;

-- Check if the address for customer_id=2 is correct
SELECT customer_id, address FROM customer WHERE customer_id = 2 AND address = '124 Happiness Ave.';

-- Ensure that the script has inserted the data
SELECT COUNT(*) AS record_count FROM customer WHERE customer_id IN (2, 3, 4);

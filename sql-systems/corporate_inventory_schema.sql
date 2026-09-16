-- ========================================================================
-- PROJECT: CORPORATE INVENTORY & DATA ENTRY COMPLIANCE TRACKING SYSTEM
-- AUTHOR: SUDHRSHAN G S
-- TARGET USE CASE: Data Management, Quality Auditing, and System Metrics
-- ========================================================================

-- 1. Create a table tracking bulk operational product inventory
CREATE TABLE product_inventory (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    stock_quantity INT DEFAULT 0,
    unit_price DECIMAL(10, 2),
    warehouse_location VARCHAR(50)
);

-- 2. Create an audit table tracking data entry precision and logging speeds
CREATE TABLE data_entry_logs (
    log_id INT PRIMARY KEY,
    operator_name VARCHAR(50),
    timestamp_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    records_processed INT,
    error_count INT,
    compliance_status VARCHAR(20)
);

-- ========================================================================
-- DATA POPULATION PHASE (Mock Dataset Injection)
-- ========================================================================

INSERT INTO product_inventory VALUES
(501, 'Enterprise Server Rack Rackmount', 'Hardware', 14, 1200.00, 'Warehouse-A'),
(502, 'Cat6e Network Cable 1000ft', 'Networking', 45, 150.00, 'Warehouse-B'),
(503, 'Managed Network Switch 24-Port', 'Networking', 8, 450.00, 'Warehouse-A'),
(504, 'Uninterruptible Power Supply 1500VA', 'Power', 0, 299.99, 'Warehouse-C'),
(505, 'Solid State Drive 2TB NVMe', 'Storage', 120, 180.00, 'Warehouse-B');

INSERT INTO data_entry_logs VALUES
(1001, 'Sudhrshan G S', '2026-09-14 09:30:00', 450, 0, 'Zero-Error Pass'),
(1002, 'System_Auto_Log', '2026-09-14 12:00:00', 1200, 4, 'Warning-Review'),
(1003, 'Sudhrshan G S', '2026-09-15 10:15:00', 680, 0, 'Zero-Error Pass'),
(1004, 'Temp_Operator', '2026-09-15 16:45:00', 210, 15, 'Failed-Audit');

-- ========================================================================
-- DATA ANALYSIS & COMPLIANCE REPORTING QUERIES
-- ========================================================================

-- REPORT 1: Identify critical inventory storage depletion (Out of stock or critically low)
SELECT product_name, stock_quantity, warehouse_location 
FROM product_inventory 
WHERE stock_quantity <= 10 
ORDER BY stock_quantity ASC;

-- REPORT 2: Calculate operational data entry efficiency metrics for the current cycle
SELECT operator_name, 
       SUM(records_processed) as total_records, 
       SUM(error_count) as total_errors
FROM data_entry_logs
GROUP BY operator_name
ORDER BY total_records DESC;

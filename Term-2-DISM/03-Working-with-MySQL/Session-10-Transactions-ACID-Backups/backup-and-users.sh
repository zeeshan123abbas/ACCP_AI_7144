#!/usr/bin/env bash
# backup-and-users.sh  - run from a terminal where `mysql` and `mysqldump` are on PATH

# 1) Consistent backup of one database (InnoDB) including routines and triggers
mysqldump -u root -p --single-transaction --routines --triggers \
  --databases institute_db > institute_db_$(date +%F).sql

# 2) Restore into the server (creates the database because of --databases)
mysql -u root -p < institute_db_$(date +%F).sql

# 3) Backup only the structure (no data)
mysqldump -u root -p --no-data institute_db > institute_schema_only.sql

# 4) Least-privilege application user
mysql -u root -p <<'SQL'
CREATE USER IF NOT EXISTS 'institute_app'@'localhost' IDENTIFIED BY 'Change_Me_123!';
GRANT SELECT, INSERT, UPDATE, DELETE ON institute_db.* TO 'institute_app'@'localhost';
CREATE USER IF NOT EXISTS 'report_viewer'@'%' IDENTIFIED BY 'Viewer_456!';
GRANT SELECT ON institute_db.v_result_card TO 'report_viewer'@'%';
SHOW GRANTS FOR 'institute_app'@'localhost';
REVOKE DELETE ON institute_db.* FROM 'institute_app'@'localhost';
SQL

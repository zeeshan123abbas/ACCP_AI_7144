-- replication-setup.sql
-- Lab setup: two MySQL 8 servers (two VMs, two Docker containers, or two ports on one PC).

-- ===== On the SOURCE: my.cnf / my.ini =====
-- [mysqld]
-- server-id                = 1
-- log-bin                  = mysql-bin
-- gtid_mode                = ON
-- enforce_gtid_consistency = ON

-- Create a replication account on the source
CREATE USER 'repl'@'%' IDENTIFIED BY 'Repl_Pass_789!';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
SHOW BINARY LOG STATUS;   -- MySQL 8.2+ (older: SHOW MASTER STATUS)

-- ===== On the REPLICA: my.cnf / my.ini =====
-- [mysqld]
-- server-id                = 2
-- gtid_mode                = ON
-- enforce_gtid_consistency = ON
-- read_only                = ON

-- Point the replica at the source (MySQL 8.0.23+ syntax)
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST = '192.168.1.10',
  SOURCE_PORT = 3306,
  SOURCE_USER = 'repl',
  SOURCE_PASSWORD = 'Repl_Pass_789!',
  SOURCE_AUTO_POSITION = 1,
  GET_SOURCE_PUBLIC_KEY = 1;

START REPLICA;
SHOW REPLICA STATUS\G
-- Check: Replica_IO_Running = Yes, Replica_SQL_Running = Yes, Seconds_Behind_Source = 0

-- file name : test.sql
-- pwd : /project_name/app/schema/test.sql

CREATE DATABASE testDBdefault
CHARACTER
SET UTF8;

use testDB;

CREATE TABLE testTable
(
    idx INT
    UNSIGNEDNOT NULL AUTO_INCREMENTPRIMARY KEY,
    test    VARCHAR
    (256)NOT NULL
) CHARSET=utf8;

USE `iot_db`;
CREATE PROCEDURE insert_server_data(
    server_id_param INT,
    name_param VARCHAR(45),
    creation_date_param DATETIME
)
BEGIN
    INSERT INTO `server` (server_id, name, creation_date)
    VALUES (server_id_param, name_param, creation_date_param);
END//
DELIMITER ;
CALL insert_server_data(2, 'ServerName', '2023-01-01 15:06:00');

DELIMITER //
CREATE PROCEDURE insert_rows()
BEGIN
    DECLARE counter INT DEFAULT 1;
    DECLARE new_name VARCHAR(45);
    WHILE counter <= 10 DO
        SET new_name = CONCAT('Noname', counter);
        INSERT INTO user (username) VALUES (new_name);
        SET counter = counter + 1;
    END WHILE;
END//
DELIMITER ;
CALL insert_rows();

DELIMITER //
DROP procedure if exists StoredMiwa;
CREATE PROCEDURE StoredMiwa(
IN value1 int, out miwa int)
BEGIN
CALL AA4(@max,@min,@sum,@avg);
CASE value1
        WHEN 1 THEN
            set miwa = @max;
        WHEN 2 THEN
            SET miwa = @min;
        WHEN 3 THEN
            set miwa = @sum;
        ELSE
            set miwa = @avg;
    END CASE;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AA4(
    out value1 int,
    OUT value2 int,
    out value3 int,
    out value4 int )
    BEGIN
        SET NOCOUNT ON;
        SELECT MAX(price), MIN(price), SUM(price),AVG(price) INTO value1,value2, value3,value4
        FROM game;
END //
DELIMITER ;


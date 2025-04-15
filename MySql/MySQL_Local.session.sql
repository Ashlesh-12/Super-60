SELECT COUNT(*) FROM memberinfo;

-- simple store procedure

CREATE PROCEDURE get_member_count()
BEGIN
SELECT COUNT(*) FROM memberinfo;
END

CALL get_member_count()

CREATE PROCEDURE get_member_count_by_ages(member_age INT)
BEGIN
SELECT COUNT(*) FROM memberinfo WHERE age>member_age;
END

CALL get_member_count_by_ages(30);

CREATE PROCEDURE get_member_info_by_ids(IN memberid VARCHAR(50))
BEGIN
SELECT * FROM memberinfo WHERE member_id = memberid;
END

CALL get_member_info_by_ids('M100');

CREATE PROCEDURE get_member_countByAge(
    IN member_age INT, 
    OUT member_count INT
)
BEGIN
    SELECT COUNT(*) INTO member_count FROM memberinfo WHERE age > member_age;
END 


DROP PROCEDURE get_member_countByAge;

SET @member_count=0;
CALL get_member_countByAge(30,@member_count);
SELECT @member_count AS Total_Members;

CREATE PROCEDURE get_member_by_gender(IN member_gender INT)
BEGIN
SELECT * FROM memberinfo WHERE gender=member_gender;
END

CALL get_member_by_gender(1)

CREATE PROCEDURE get_member_by_gender_age(IN member_gender INT,IN member_age INT)
BEGIN
SELECT * FROM memberinfo WHERE gender=member_gender AND age=member_age;
END

CALL get_member_by_gender_age(1,30)

CREATE PROCEDURE get_member_count_using_with(IN member_gender INT,IN member_age INT)
BEGIN
WITH filtered_members AS (
    SELECT * FROM memberinfo WHERE gender=member_gender AND age>member_age
)
SELECT * FROM filtered_members;
END

DROP PROCEDURE get_member_count_using_with;

CALL get_member_count_using_with(1,46)

SELECT gender,COUNT(*)
FROM memberinfo
GROUP BY gender;

SELECT COUNT(member_id), CASE 
WHEN gender=1 THEN "FEMALE"
ELSE "MALE"
END AS gender 
FROM memberinfo 
GROUP BY gender;

CREATE FUNCTION get_member_function(gender INT)
RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(45);
    IF gender=0 THEN 
        SET result="Female";
    ELSE
        SET result="Male";
    END IF;
    RETURN result;
END

SELECT get_member_function(1);

DROP PROCEDURE sp_InsertMember;
CREATE PROCEDURE sp_InsertMember(
    IN p_username VARCHAR(50),
    IN p_firstname VARCHAR(50),
    IN p_lastname VARCHAR(50),
    IN p_age INT,
    IN p_gender VARCHAR(10),
    IN p_email VARCHAR(100),
    IN p_phonenumber BIGINT
)
BEGIN
    DECLARE v_new_member_id VARCHAR(50);
    DECLARE v_existing_count INT;

    SELECT COUNT(*) INTO v_existing_count 
    FROM memberinfo 
    WHERE username = p_username;

    IF v_existing_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Username already exists!';
    END IF;

    SELECT (COALESCE(MAX(member_id as Unsigned), 1000), '1') INTO v_new_member_id 
    FROM memberinfo;

    INSERT INTO memberinfo (member_id, username, firstname, lastname, age, gender, email, phonenumber)
    VALUES (v_new_member_id, p_username, p_firstname, p_lastname, p_age, fn_ConvertGender(p_gender), p_email, p_phonenumber);
END $$

DELIMITER ;
SELECT * FROM memberinfo
CALL sp_InsertMember('alex_smith1', 'Alex', 'Smith', 30, 'Male', 'alex@example.com', '7654321098');
SELECT * FROM memberinfo;
SELECT * from memberinfo where username='alex_smith';
CALL sp_InsertMember('alex_smith', 'John', 'Doe', 26, 'Male', 'john_new@example.com', '9123456789');
DELIMITER $$

CREATE FUNCTION fn_ConvertGender(p_gender VARCHAR(10)) 
RETURNS TINYINT DETERMINISTIC
BEGIN
    RETURN CASE 
        WHEN p_gender = 'Male' THEN 1
        WHEN p_gender = 'Female' THEN 0
        ELSE NULL
    END;
END $$

DELIMITER ;

SELECT * FROM memberinfo 
WHERE member_id = (SELECT MAX(member_id) FROM memberinfo);

CALL sp_InsertMember('alex_Ben', 'John', 'Doe', 26, 'Male', 'john_new@example.com', '9123456789');

DROP PROCEDURE sp_InsertMember;

-- Stored Procedures

-- Creating store procedure to get the details(firstname,lastnname,age of members just by passing the member id--
CREATE PROCEDURE get_the_details(IN memberid varchar(45))
BEGIN 
   SELECT firstname,lastname,age
   FROM memberinfo
   WHERE member_id=memberid;
END 
DROP PROCEDURE get_the_details;

CALL get_the_details('M100');

SELECT * FROM memberinfo;

-- 1.Create a Stored Procedure to insert the details of any new member by just passing the details as parameters.
CREATE PROCEDURE insert_member(
IN memberid varchar(45),
IN username varchar(45),
IN firstname varchar(45),
IN lastname varchar(45), 
IN age varchar(45),
IN gender varchar(45),
IN email varchar(45),
IN phonenumber bigint
)
BEGIN 
 INSERT INTO memberinfo(member_id,username,firstname,lastname,age,gender,email,phonenumber)
 VALUES(memberid,username,firstname,lastname,age,gender,email,phonenumber);
END

CALL insert_member(
    'M2905', 
    'john_doe', 
    'John', 
    'Doe', 
    30, 
    'Male', 
    'john.doe@example.com', 
    9876543210
);

-- 2.Create a stored procedure to retrieve all members from the memberinfo table. --
CREATE PROCEDURE get_all_members()
BEGIN 
   SELECT * FROM memberinfo;
END

CALL get_all_members;

-- 3.Write a stored procedure to insert an address for a member in the addressinfo table.--
select * from addressinfo;
CREATE PROCEDURE insert_address(
    IN addressid VARCHAR(45),
    IN city VARCHAR(45),
    IN state VARCHAR(45),
    IN country VARCHAR(45),
    IN pincode VARCHAR(45),
    IN memberid VARCHAR(45)
)
BEGIN
    INSERT INTO addressinfo (address_id, city, state, country, pincode, memberinfo_member_id)
    VALUES (addressid, city, state, country, pincode, memberid);
END 

CALL insert_address(
    'A001', 
    'New York', 
    'NY', 
    'USA', 
    '10001', 
    'M001'
);

-- 4.Develop a stored procedure to insert a new cardio diagnosis record.--
 CREATE PROCEDURE insert_cardiodiagnosis(
    IN cardioid VARCHAR(45),
    IN cardioarrestdetect INT,
    IN datementioned DATETIME,
    IN member_id VARCHAR(45)
)
BEGIN 
    INSERT INTO cardiodiagnosis (cardio_id, cardioarrestdetected, date, memberinfo_member_id)
    VALUES (cardioid, cardioarrestdetect, datementioned, member_id);
END 

CALL insert_cardiodiagnosis(
    'C001', 
    1, 
    '2025-03-06 12:30:00', 
    'M001'
);
SELECT * from bloodtest

-- 5.Write a stored procedure to insert a blood test record into the bloodtest table.--
CREATE PROCEDURE insert_blood_test(
  IN blood_id varchar(45),
  IN datementioned datetime,
  IN bloodpressure int,
  IN fbs int,
  IN thal int,
  IN serumcholesterol int, 
  in cardiodiagnosis_cardio_id varchar(45)
)
BEGIN 
      INSERT INTO bloodtest (blood_id, date, bloodpressure, fbs, thal, serumcholesterol, cardiodiagnosis_cardio_id)
    VALUES (blood_id, datementioned, bloodpressure, fbs, thal, serumcholesterol,cardiodiagnosis_cardio_id);
END 

CALL insert_blood_test(
    'b999', 
    '2025-03-06 12:30:00', 
    120, 
    1, 
    2,
  14,
  'C001'
);

-- 6.Create a stored procedure to insert an ECG report into the ecgreport table.--
CREATE PROCEDURE insert_into_ecgreport(
  IN ecg_id varchar(45),
  IN datementioned datetime,
  IN restecg int,
  IN cardiodiagnosis_cardio_id varchar(45) 
 )
 BEGIN 
    INSERT INTO ecgreport (ecg_id, datementioned, restecg, cardiodiagnosis_cardio_id)
    VALUES (ecg_id, datementioned, restecg, cardiodiagnosis_cardio_id);
END

CALL insert_into_ecgreport(
    'ECG001', 
    '2025-03-06 14:00:00', 
    1, 
    'C001'
);


-- 9) symptom data into symptom table --

SELECT * FROM symptom;

DROP PROCEDURE InsertSymptom;

CREATE PROCEDURE InsertSymptom(
    IN p_symptom_id VARCHAR(45),
    IN p_date datetime,
    IN p_exang INT,
    IN p_oldpeak FLOAT,
    IN p_cp INT
)
BEGIN
    INSERT INTO symptom(symptom_id,date,exang,oldpeak,cp)
    VALUES (p_symptom_id,p_date,p_exang,p_oldpeak,p_cp);
END 

CALL InsertSymptom('symid1000','2024-05-23','1','10','10');

-- 10)  retrieve all diagnoses from the cardiodiagnosis table. --

SELECT * FROM cardiodiagnosis;

CREATE PROCEDURE GetAllDiagnoses()
BEGIN
    SELECT * FROM cardiodiagnosis;
END 

CALL GetAllDiagnoses();

-- 11) Write a stored procedure with a parameter to get a member by their member_id.
 --
SELECT * FROM memberinfo;
DROP PROCEDURE GetMemberById;
CREATE PROCEDURE GetMemberById(
    IN p_member_id VARCHAR(45)
)
BEGIN
    SELECT * FROM memberinfo WHERE member_id = p_member_id;
END 

CALL GetMemberById("M100");

-- 12) Create a stored procedure to retrieve an address by member_id. --

SELECT * FROM addressinfo;

DROP PROCEDURE GetAddressByMemberId;

CREATE PROCEDURE GetAddressByMemberId(
    IN p_memberinfo_member_id VARCHAR(45)
)
BEGIN
    SELECT * FROM addressinfo WHERE memberinfo_member_id = p_memberinfo_member_id;
END 

CALL GetAddressByMemberId("M100");

-- 13) Develop a stored procedure to get all diagnoses for a specific member using member_id.

SELECT * FROM cardiodiagnosis

DROP PROCEDURE GetDiagnosesByMemberId;

CREATE PROCEDURE GetDiagnosesByMemberId(
    IN p_memberinfo_member_id VARCHAR(45)
)
BEGIN
    SELECT * FROM cardiodiagnosis WHERE memberinfo_member_id = p_memberinfo_member_id;
END 

CALL GetDiagnosesByMemberId("M1");

-- 14) Write a stored procedure to retrieve blood test records by cardio_id. --

SELECT * FROM bloodtest;

DROP PROCEDURE GetBloodtestBycardio_Id;

CREATE PROCEDURE GetBloodtestBycardio_Id(
    IN p_cardiodiagnosis_cardio_id VARCHAR(45)
)
BEGIN
    SELECT * FROM bloodtest WHERE cardiodiagnosis_cardio_id = p_cardiodiagnosis_cardio_id;
END 

CALL GetBloodtestBycardio_Id("cid221");

-- 15.Create a stored procedure to get ECG reports by cardio_id.

CREATE PROCEDURE retrieve_ecg(in cardio_id_search varchar(45))
BEGIN
	SELECT * from ecgreport
    	WHERE cardio_id_search = ecgreport.cardiodiagnosis_cardio_id;
END

CALL retrieve_ecg('cid222');


-- 16.Develop a stored procedure to retrieve wearable device data by cardio_id.

CREATE PROCEDURE retrieve_wearable(in cardio_id_search varchar(45))
BEGIN
	SELECT * from wearabledevicedata
    	WHERE cardio_id_search = wearabledevicedata.cardiodiagnosis_cardio_id;
END

call retrieve_wearable('cid222');

-- 17.Write a stored procedure to retrieve symptoms by cardio_id.

CREATE PROCEDURE retrieve_symptoms(in cardio_id_search varchar(45))
BEGIN
	SELECT * from symptom
    	WHERE cardio_id_search = symptom.cardiodiagnosis_cardio_id;
END

CALL retrieve_symptoms('cid222');

-- 18.Create a stored procedure to get X-ray data by cardio_id.

CREATE PROCEDURE retrieve_xray(in cardio_id_search varchar(45))
BEGIN
	SELECT * from xray
    	WHERE cardio_id_search = xray.cardiodiagnosis_cardio_id;
END

CALL retrieve_xray('cid222');

-- 19.Write a function to return the total number of members in the memberinfo table.

CREATE FUNCTION count_members() 
RETURNS INT 
DETERMINISTIC
BEGIN
    DECLARE count_no INT;
    SELECT COUNT(*) INTO count_no FROM memberinfo;
    RETURN count_no;
END
    
SELECT count_members()

-- 20.Develop a function to return the total number of diagnoses for a given member_id.

CREATE FUNCTION count_dia(member_id VARCHAR(45)) 
RETURNS INT 
DETERMINISTIC
BEGIN
    DECLARE count_dia INT;
    SELECT COUNT(cardioarrestdetected) INTO count_dia 
    FROM cardiodiagnosis
    WHERE memberinfo_member_id = member_id;

    RETURN count_dia;
END 

SELECT * FROM cardiodiagnosis

SELECT count_dia('M100')

-- 21.Write a function to calculate the average blood pressure from the bloodtest table.

CREATE FUNCTION avg_bp()
RETURNS int 
	BEGIN
    	DECLARE avg_bp int;
        SELECT AVG(bloodtest.bloodpressure)
        	INTO avg_bp
            	FROM bloodtest;
        RETURN avg_bp;
    END
    
SELECT avg_bp()
            
-- 22.Create a function to return the total number of ECG reports.

CREATE FUNCTION count_ecg()
RETURNS int 
	BEGIN
    	DECLARE count_ecg int;
        SELECT count(*)
        	INTO count_ecg
            	FROM ecgreport;
        RETURN count_ecg;
    END
    
SELECT count_ecg()

-- 23.Develop a function to return the total number of X-ray scans.

CREATE FUNCTION count_xray()
RETURNS int 
	BEGIN
    	DECLARE count_xray int;
        SELECT count(*)
        	INTO count_xray
            	FROM xray;
        RETURN count_xray;
    END
    
SELECT count_xray()

-- CREATE TRIGGER trigger_name
-- AFTER INSERT ON table_name
-- FOR EACH ROW
-- BEGIN
    -- SQL statements to execute
-- END 

CREATE TABLE member_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id VARCHAR(50) NOT NULL,
    action VARCHAR(50) NOT NULL,
    action_date DATETIME NOT NULL
);

-- triggers
-- 1)
CREATE TABLE member_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id VARCHAR(45),
    action VARCHAR(100),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER after_member_insert
AFTER INSERT ON memberinfo
FOR EACH ROW
BEGIN
    INSERT INTO member_log (member_id, action)
    VALUES (NEW.member_id, 'New Member Added');
END

INSERT INTO memberinfo (member_id, username, firstname, lastname, age, gender, email, phonenumber)
VALUES ('M11111111', 'user101', 'John', 'Doe', 30, 'Male', 'john.doe@example.com', 9876543210);

SELECT * FROM member_log;

-- 2)
-- Write a trigger to update the recovereddate when a disease record is updated.--
DROP TRIGGER update_recover_date;
CREATE TRIGGER update_recover_date
BEFORE UPDATE ON diseasedetail
FOR EACH ROW
BEGIN
    SET NEW.recovereddate = NOW();
END;

UPDATE diseasedetail WHERE disease_id='D403';

-- 3.Create a trigger to prevent deletion of records in the cardiodiagnosis table.

CREATE TRIGGER trigger3
BEFORE DELETE ON cardiodiagnosis
FOR EACH ROW 
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT='Deletion is not allowed in the cardiodiagnosis table';
END

DELETE FROM cardiodiagnosis WHERE cardio_id="cid123";

-- 4.Write a trigger to capitalize the first letter of the city name in the addressinfo table.
CREATE TRIGGER trigger4
AFTER 

-- VIEWS --

-- 1. Create a view to get member details with their address.
SELECT * FROM addressinfo;
CREATE VIEW view1 AS
SELECT * FROM memberinfo AS m
JOIN addressinfo AS a 
ON m.member_id=a.memberinfo_member_id;

SELECT * FROM view1;

-- 2) Write a view to get cardio diagnosis details along with member names.
SELECT * FROM cardiodiagnosis;
DROP VIEW view2;
CREATE VIEW view2 AS 
SELECT m.firstname,c.*
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id;

SELECT * FROM view2;

-- 3.Create a view to display disease details along with recovery status.

CREATE VIEW view3 AS
SELECT * FROM diseasedetail;

SELECT * FROM view3
WHERE isrecovered=1;

-- 4.Write a view to display blood test results with member details.

DROP VIEW view4;
CREATE VIEW view4 AS 
SELECT m.*,b.*,b.date AS bloodtestdate FROM memberinfo AS m 
JOIN cardiodiagnosis AS c
ON m.member_id=c.memberinfo_member_id
JOIN bloodtest AS b
ON c.cardio_id=b.cardiodiagnosis_cardio_id;\

SELECT * FROM view4;

-- 5.Create a view to get ECG reports with member names.

CREATE VIEW view5 AS 
SELECT m.firstname,e.*
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN ecgreport AS e 
ON c.cardio_id=e.cardiodiagnosis_cardio_id;

SELECT * FROM view5;

-- 6.Write a view to get recent blood test results for each member.
DROP VIEW view12;

CREATE VIEW view12 AS 
SELECT m.member_id,b.blood_id,MAX(b.date) AS Recent,b.bloodpressure,b.fbs,b.thal,b.serumcholesterol
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN bloodtest AS b 
ON c.cardio_id=b.cardiodiagnosis_cardio_id
GROUP BY m.member_id,b.blood_id,b.bloodpressure,b.fbs,b.thal,b.serumcholesterol;

SELECT * FROM view12;

-- 7.Create a view to display members with abnormal ECG results.
CREATE VIEW view6 AS
SELECT m.*,e.*,e.date AS ecgdate FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN ecgreport AS e 
ON c.cardio_id=e.cardiodiagnosis_cardio_id;

SELECT * FROM view6 
WHERE restecg=0;

-- 8.Write a view to get all symptoms recorded for each member.

CREATE VIEW view7 AS 
SELECT m.*,s.*,s.date AS symptomdate FROM memberinfo AS m
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN symptom AS s 
ON c.cardio_id=s.cardiodiagnosis_cardio_id;

SELECT * FROM view7;

-- 9.Create a view to show members diagnosed with diseases in the last 6 months.

CREATE VIEW view8 AS 
SELECT m.*,d.disease_id,d.diagnoseddate
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN diseasedetail AS d 
ON c.cardio_id=d.cardiodiagnosis_cardio_id
WHERE MONTH(d.diagnoseddate)<6;

SELECT * FROM view8;

-- 10.Write a view to list X-ray results associated with members.

CREATE VIEW view10 AS 
SELECT m.*,x.*,x.date AS xraydate FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN xray AS x 
ON c.cardio_id=x.cardiodiagnosis_cardio_id;

SELECT * FROM view10;

-- 11.Write a view to display a summary of the latest disease diagnoses per member.

DROP VIEW view11;

CREATE VIEW view11 AS 
SELECT m.member_id, d.disease_id,MAX(date) AS Latest ,d.isrecovered,d.recovereddate 
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN diseasedetail AS d 
ON c.cardio_id=d.cardiodiagnosis_cardio_id
GROUP BY m.member_id,d.disease_id,d.recovereddate,d.isrecovered;

SELECT * FROM view11;

-- 12.view to track the average blood pressure readings per member over time

DROP VIEW AvgBloodPressurePerMember;

CREATE VIEW AvgBloodPressurePerMember AS
SELECT m.member_id,m.username ,b.date,AVG(b.bloodpressure) AS avg_bloodpressure
FROM bloodtest b
    JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id=c.cardio_id
    JOIN memberinfo m ON c.memberinfo_member_id= m.member_id
GROUP BY m.member_id,m.username,b.date;

SELECT * FROM AvgBloodPressurePerMember;

-- 13.Write a view to show the number of members diagnosed with cardio diseases each month.

DROP VIEW view14;

CREATE VIEW view14 AS 
SELECT COUNT(*) AS total_count, 
       MONTH(c.date) AS Month 
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id = c.memberinfo_member_id
GROUP BY MONTH(c.date);


SELECT * FROM view14;

-- 14.Create a view to analyze the correlation between blood test results and ECG abnormalities.
DROP VIEW view15;

CREATE VIEW view15 AS
SELECT b.*,e.ecg_id,e.date AS ecg_date,e.restecg
FROM cardiodiagnosis AS c 
JOIN bloodtest AS b 
ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN ecgreport AS e
ON c.cardio_id = e.cardiodiagnosis_cardio_id;

SELECT * FROM view15;

-- 15.Write a view to summarize the health status of members based on available test results.
CREATE VIEW view16 AS 
SELECT m.member_id,
       b.bloodpressure,
       b.fbs,
       b.thal,
       b.serumcholesterol,
       c.cardioarrestdetected,
       d.isrecovered,
       e.restecg,
       s.exang,
       s.oldpeak,
       s.cp,
       w.thalach,
       w.slope,
       x.ca
FROM memberinfo AS m 
JOIN cardiodiagnosis AS c 
ON m.member_id=c.memberinfo_member_id
JOIN bloodtest AS b 
ON c.cardio_id=b.cardiodiagnosis_cardio_id
JOIN diseasedetail AS d 
ON c.cardio_id=d.cardiodiagnosis_cardio_id
JOIN ecgreport AS e 
ON c.cardio_id=e.cardiodiagnosis_cardio_id
JOIN symptom AS s 
ON c.cardio_id=s.cardiodiagnosis_cardio_id
JOIN wearabledevicedata AS w 
ON c.cardio_id=w.cardiodiagnosis_cardio_id
JOIN xray AS x 
ON c.cardio_id=x.cardiodiagnosis_cardio_id;

SELECT * FROM view16;
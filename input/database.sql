-- CREATE A TABLE MAYBAY
DROP TABLE IF EXISTS "MAYBAY";
CREATE TABLE "MAYBAY" (
	"flight"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("flight")
);
INSERT INTO "MAYBAY" ("flight") VALUES ('M1');
INSERT INTO "MAYBAY" ("flight") VALUES ('M2');
INSERT INTO "MAYBAY" ("flight") VALUES ('M3');
INSERT INTO "MAYBAY" ("flight") VALUES ('M4');
INSERT INTO "MAYBAY" ("flight") VALUES ('M5');
INSERT INTO "MAYBAY" ("flight") VALUES ('M6');
-- CREATE A TABLE ATIME
DROP TABLE IF EXISTS "ATIME";
CREATE TABLE "ATIME" (
	"id"	INTEGER NOT NULL UNIQUE,
	"flight"	TEXT NOT NULL,
	"place"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	FOREIGN KEY("flight") REFERENCES "MAYBAY"("flight"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (1, 'M1', 'HUE', '11:00HR');
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (2, 'M2', 'HUE', '13:30HR');
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (3, 'M3', 'HCM', '16:30HR');
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (4, 'M4', 'HAIPHONG', '10:30HR');
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (5, 'M5', 'HN', '05:45HR');
INSERT INTO "ATIME" ("id", "flight", "place", "time")
VALUES (6, 'M6', 'HAIPHONG', '11:30HR');
-- CREATE A TABLE DTIME
DROP TABLE IF EXISTS "DTIME";
CREATE TABLE "DTIME" (
	"id"	INTEGER NOT NULL UNIQUE,
	"flight"	TEXT NOT NULL,
	"place"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	FOREIGN KEY("flight") REFERENCES "MAYBAY"("flight"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (1, 'M1', 'HCMC', '10:00HR');
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (2, 'M2', 'HN', '12:30HR');
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (3, 'M3', 'DANANG', '15:00HR');
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (4, 'M4', 'DANANG', '08:30HR');
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (5, 'M5', 'HCM', '03:30HR');
INSERT INTO "DTIME" ("id", "flight", "place", "time")
VALUES (6, 'M6', 'HCMC', '09:30HR');
-- CREATE A TABLE RUN-TIME
DROP TABLE IF EXISTS "RUNTIME";
CREATE TABLE "RUNTIME" (
	"id"	INTEGER NOT NULL UNIQUE,
	"flight"	TEXT NOT NULL,
	"src"	TEXT NOT NULL,
	"dest"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	FOREIGN KEY("flight") REFERENCES "MAYBAY"("flight"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (1, 'M1', 'HCMC', 'HUE', '1:00HR');
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (2, 'M2', 'HN', 'HUE', '1:00HR');
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (3, 'M3', 'DANANG', 'HCM', '1:30HR');
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (4, 'M4', 'DANANG', 'HAIPHONG', '02:00HR');
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (5, 'M5', 'HCM', 'HN', '02:15HR');
INSERT INTO "RUNTIME" ("id", "flight", "src", "dest", "time")
VALUES (6, 'M6', 'HCMC', 'HAIPHONG', '02:00HR');
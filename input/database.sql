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
-- Relation
DROP TABLE IF EXISTS "RELATIONS";
CREATE TABLE "RELATIONS" (
	"id"	INTEGER NOT NULL UNIQUE,
	"relation"	TEXT NOT NULL UNIQUE,
	"first"	TEXT,
	"second"	TEXT,
	PRIMARY KEY("id")
);
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('0', 'root', 'ROOT', 'VERB');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('1', 'nsubj', 'VERB', 'NOUN');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('2', 'dobj', 'VERB', 'NOUN');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('3', 'iobj', 'VERB', 'NOUN NAME');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('4', 'pobj', 'PREP', 'NOUN TIME NAME');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('5', 'poss', 'NOUN', 'POSS');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('6', 'prep', 'VERB', 'PREP');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('7', 'aux', 'AUX', 'VERB');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('8', 'amod', 'NOUN', 'ADJ');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('9', 'nmod', 'NOUN', 'NOUN NAME');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('10', 'nummod', 'NOUN', 'NUMBER');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('11', 'conj', '', '');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('12', 'cc', 'AND, OR', '');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('13', 'ccomp', 'VERB', 'VERB');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('14', 'xcomp', 'VERB', 'TO');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('15', 'punc', 'VERB', 'EOL');
INSERT INTO "RELATIONS" ("id", "relation", "first", "second") VALUES ('16', 'det', 'NOUN', 'DET WDET');
-- LEXICON
DROP TABLE IF EXISTS "LEXICON";
CREATE TABLE "LEXICON" (
	"id"	INTEGER NOT NULL UNIQUE,
	"word"	TEXT NOT NULL,
    "num"   INTEGER NOT NULL,
	"type"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
-- Noun type
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('m??y bay', '2', 'NOUN');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('th??nh ph???', '2', 'NOUN');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('tp', '1', 'NOUN');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('h?? n???i', '2', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('m?? hi???u', '2', 'NOUN');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('gi???', '1', 'NOUN');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('th???i gian', '2', 'NOUN');
-- NAME type
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('hu???', '1', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('h??? ch?? minh', '3', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('???? n???ng', '2', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('hcm', '1', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('h???i ph??ng', '2', 'NAME');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('hn', '1', 'NAME');
-- PREP type
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('???', '1', 'PREP');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('t???', '1', 'PREP');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('l??c', '1', 'PREP');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('?????n', '1', 'PREP');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('v??o', '1', 'PREP');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('t???i', '1', 'PREP');
-- DET type
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c??c', '1', 'DET');
--INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c??', '1', 'WDET');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('n??o', '1', 'WDET');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('m???y', '1', 'WDET');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('h??y cho bi???t', '3', 'WDET');
-- Verb datatype
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('?????n', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('m???t', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('bay', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('xu???t ph??t', '2', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('ra', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('??i', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('t???i', '1', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('bay ??i', '2', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('bay ra', '2', 'VERB');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('bay v???', '2', 'VERB');
-- POSS datatype
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a t??i', '2', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a h???', '2', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a anh ta', '3', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a n??', '2', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a c?? ???y', '3', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a em', '2', 'POSS');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('c???a anh', '2', 'POSS');
-- End of line
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('?.', '1', 'EOL');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('.', '1', 'EOL');
INSERT INTO "LEXICON" ("word", "num", "type") VALUES ('?', '1', 'EOL');

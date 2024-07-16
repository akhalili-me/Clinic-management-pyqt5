BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Doctor" (
	"id"	INTEGER NOT NULL,
	"firstName"	TEXT NOT NULL,
	"lastName"	TEXT NOT NULL,
	"specialization"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Service" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Appointment" (
	"id"	INTEGER NOT NULL,
	"status"	TEXT NOT NULL,
	"jalali_date"	TEXT NOT NULL,
	"doctor"	INTEGER NOT NULL,
	"patient"	INTEGER NOT NULL,
	"service"	INTEGER,
	"description"	TEXT,
	"greg_datetime"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("patient") REFERENCES "Patient"("id") ON DELETE CASCADE,
	FOREIGN KEY("service") REFERENCES "Service"("id") ON DELETE CASCADE,
	FOREIGN KEY("doctor") REFERENCES "Doctor"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "MedicalRecordImages" (
	"id"	INTEGER NOT NULL,
	"path"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"medical_record"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("medical_record") REFERENCES "MedicalRecords"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "MedicalRecords" (
	"id"	INTEGER NOT NULL,
	"jalali_date"	TEXT NOT NULL,
	"doctor"	INTEGER NOT NULL,
	"patient"	INTEGER NOT NULL,
	"service"	INTEGER NOT NULL,
	"description"	TEXT,
	"greg_date"	TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("patient") REFERENCES "Patient"("id") ON DELETE CASCADE,
	FOREIGN KEY("service") REFERENCES "Service"("id") ON DELETE CASCADE,
	FOREIGN KEY("doctor") REFERENCES "Doctor"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Expense" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"price"	INTEGER NOT NULL,
	"description"	INTEGER,
	"jalali_date"	TEXT NOT NULL,
	"greg_date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Patient" (
	"id"	INTEGER NOT NULL,
	"firstName"	TEXT NOT NULL,
	"lastName"	TEXT NOT NULL,
	"gender"	TEXT NOT NULL,
	"age"	INTEGER,
	"phoneNumber"	TEXT NOT NULL,
	"address"	TEXT,
	"identityCode"	TEXT UNIQUE,
	"extraInfo"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;

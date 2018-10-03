CREATE DATABASE HospitalBookingDB
USE HospitalBookingDB
# code to create table
CREATE TABLE patientsbookings(
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    booking_time VARCHAR(25) NOT NULL,
    date_of_birth VARCHAR(25) NOT NULL,
    symptoms VARCHAR(300) NOT NULL
)

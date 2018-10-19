CREATE DATABASE HospitalBookingDB
USE HospitalBookingDB
# code to create table
CREATE TABLE `patientsbookings` (`id` INT(11) NOT NULL AUTO_INCREMENT, `name` VARCHAR(100) NOT NULL DEFAULT '0', `booking_time` VARCHAR(25) NOT NULL DEFAULT '0', `date_of_birth` VARCHAR(25) NOT NULL DEFAULT '0', `symptoms` VARCHAR(300) NOT NULL DEFAULT '0', `date` TIMESTAMP NOT NULL DEFAULT '',
                                 PRIMARY KEY(`id`)
                                 )
ENGINE = InnoDB

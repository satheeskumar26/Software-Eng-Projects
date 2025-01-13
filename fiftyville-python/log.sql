-- Keep a log of any SQL queries you execute as you solve the mystery.

-- My Research Prosses:

-- Look at the crime report.
SELECT * FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Clues: Crime report id = 295, time = 10:15am, location =  Humphrey Street bakery)

-- Use crime report id to find the interviews
SELECT transcript FROM interviews WHERE year = 2023 AND month = 7 AND day = 28;
-- Interviewer Clues 01: within ten minutes of the theft thief get into a car, check security footage
-- Interviewer Clues 02: Emma's bakery, before crime ATM on Leggett Street, at time of crime thief called someone
-- Interviewer Clues 03: who talked to them for less than a minute to purchase the flight ticket, earliest flight out of Fiftyville tomorrow,
-- Checked: Just incase i checked the interviews id with the flight list <<< i didnt do it

-- Check Interviewer Clues 01 / check security footage get license_plate
SELECT activity, license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 05 AND minute <= 25 ;
-- Check Interviewer Clues 01 / match license_plate to name
SELECT people.name, people.passport_numder FROM people WHERE people.license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 05 AND minute <= 25);

-- Check Interviewer Clues 02 / Check ATM only for foncormation cos not time wa given
SELECT bank_accounts.account_number, people.name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number WHERE atm_transactions.year = 2023 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Leggett Street';

-- Check Interviewer Clues 03 / match car log to name and name to passanger
SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration <= 60 ;
SELECT phone_calls.caller, phone_calls.receiver FROM people WHERE people.phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration <= 60);

-- Check with passangers, but passangers maybe data worth a year <<< id not work
SELECT * FROM passengers WHERE passport_number = ('2963008352');

-- Connect all passengers to flight to airports
SELECT people.name, flights.hour, flights.minute, airport.city FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id JOIN airports ON flights.origin_airport_id = airports.id WHERE flights.year = 2023 AND flights.month = 7 AND flights.day = 29 AND airports.city = 'Fiftyville' ORDER BY flights.hour;
-- Find the city
SELECT city FROM airports WHERE id = 4;

DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS availabilities;
DROP SEQUENCE IF EXISTS availabilities_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    username text,
    password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price_per_night float,
    booked_flag boolean,
    user_id int,
    constraint fk_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS availabilities_id_seq;
CREATE TABLE availabilities (
  id SERIAL PRIMARY KEY,
  date date,
  status TEXT default 'Available',
  space_id int,
  constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
);

INSERT INTO users (name, username, password) VALUES ('Saffron Smith', 'saffron1', 'scrypt:32768:8:1$8FejpA6rMrY4a6MH$8a6ad3dc300d47d2b7aa7a1841b2440e9e097959f3dc5d6e5de133943f65162ae2e2ebb19a792898e19bd3a53b1ad0d8bb290def99842378c1c6b5c21b444596');
INSERT INTO users (name, username, password) VALUES ('Indigo Johnson', 'indigo1', 'scrypt:32768:8:1$OLPYv2Q9DI82PUfv$8bbea1020f401eff1342005dacff23a4806ca5e6b796bbc655940b3ff33515192e7c5cd823aafbb672ec174239b7fc562e33f5a85feed78b5c34d3926fe115c9');

INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Highgarden House', 'Situated within walking distance of most of the main attractions of Highgarden, this luxurious appartment would suit a family of up to 5, with three bedrooms, two en-suite bathrooms and a shared bathroom', 150.00, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Ramsey Beach', 'If you love the sea and sun, visit us here at Ramsey Beach. Our property is perfectly set up for sandy fun with a veranda straight onto the beach', 100.00, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Emerald City', 'Your magical adventure starts here! Bring your loved ones along for a visit that you will never forget!', 70.00, False, 2);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Summerfields', 'Hazy days spent with those you love. Summerfields is a location that you will remember forever.', 120.00, False, 2);

INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-25', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-26', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-27', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-28', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-29', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-30', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-01', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-02', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-03', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-04', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-05', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-06', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-07', 'Available', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-25', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-26', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-27', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-28', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-29', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-30', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-01', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-02', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-03', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-04', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-05', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-06', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-07', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-25', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-26', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-27', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-28', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-29', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-30', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-01', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-02', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-03', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-04', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-05', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-06', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-07', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-25', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-26', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-27', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-28', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-29', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-11-30', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-01', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-02', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-03', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-04', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-05', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-06', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-12-07', 'Available', 4);
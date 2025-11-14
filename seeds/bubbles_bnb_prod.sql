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

INSERT INTO users (name, username, password) VALUES ('Saffron Smith', 'saffron1', 'Password1');
INSERT INTO users (name, username, password) VALUES ('Indigo Johnson', 'indigo1', 'Password1');

INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Highgarden House', 'Situated within walking distance of most of the main attractions of Highgarden, this luxurious appartment would suit a family of up to 5, with three bedrooms, two en-suite bathrooms and a shared bathroom', 150.00, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Ramsey Beach', 'If you love the sea and sun, visit us here at Ramsey Beach. Our property is perfectly set up for sandy fun with a veranda straight onto the beach', 100.00, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Emerald City', 'Your magical adventure starts here! Bring your loved ones along for a visit that you will never forget!', 70.00, False, 2);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Summerfields', 'Hazy days spent with those you love. Summerfields is a location that you will remember forever.', 120.00, False, 2);



INSERT INTO availabilities (date, space_id) VALUES ('2025-08-11', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-01-01', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-09-21', 'Available', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-02-01', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2027-02-01', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-05-30', 'Booked', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-07-01', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-04-14', 'Available', 1);

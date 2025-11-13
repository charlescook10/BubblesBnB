DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS availabilities;
DROP SEQUENCE IF EXISTS availabilities_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

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

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    user_id   INTEGER NOT NULL,
    availability_id  INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (availability_id) REFERENCES availabilities(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, availability_id)
);



INSERT INTO users (name, username, password) VALUES ('Test_User_1', 'testuser1', 'abc123');
INSERT INTO users (name, username, password) VALUES ('Test_User_2', 'testuser2', '123abc');

INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_2', 'This is a description of Test_Space_2', 10.0, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_3', 'This is a description of Test_Space_3', 10.0, False, 2);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 2);



INSERT INTO availabilities (date, space_id) VALUES ('2025-08-11', 1);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-01-01', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2025-09-21', 'Booked', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-02-01', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2027-02-01', 'Available', 4);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-05-30', 'Booked', 3);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-07-01', 'Available', 2);
INSERT INTO availabilities (date, status, space_id) VALUES ('2026-04-14', 'Booked', 1);


INSERT INTO bookings (user_id, availability_id) VALUES (2, 3);
INSERT INTO bookings (user_id, availability_id) VALUES (1, 6);
INSERT INTO bookings (user_id, availability_id) VALUES (2, 8);
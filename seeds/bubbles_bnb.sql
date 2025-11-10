DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

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

INSERT INTO users (name, username, password) VALUES ('Test_User_1', 'testuser1', 'abc123');
INSERT INTO users (name, username, password) VALUES ('Test_User_2', 'testuser2', '123abc');

INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_2', 'This is a description of Test_Space_2', 10.0, False, 1);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_3', 'This is a description of Test_Space_3', 10.0, False, 2);
INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id) VALUES ('Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 2);
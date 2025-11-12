_Copy this recipe template to design and create a database table from a specification._


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| availability               | date, status, space_id|

Name of the table (always plural): `availabilities`

Column names: `date, status, space_id

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
date: date
status: TEXT
space_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: availabilities_table.sql
a
-- Replace the table name, column names and types.

CREATE TABLE availabilities (
  id SERIAL PRIMARY KEY,
  date, date,
  status, TEXT
  space_id, int
 constraint fk_space foreign key(space_id)
    references spaces(id)
    on delete cascade
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < availabilities_table.sql
```
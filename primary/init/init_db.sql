CREATE USER appuser WITH PASSWORD 'apppass';
CREATE DATABASE labdb OWNER appuser;
\c labdb
CREATE SCHEMA IF NOT EXISTS app AUTHORIZATION appuser;
CREATE TABLE IF NOT EXISTS app.messages (
  id serial primary key,
  text text,
  created_at timestamptz default now()
);
INSERT INTO app.messages (text)
SELECT md5(random()::text) FROM generate_series(1,50);

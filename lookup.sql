CREATE TABLE IF NOT EXISTS car_seq (id int, next_id bigint, cache bigint, primary key(id)) comment 'vitess_sequence';
INSERT INTO car_seq(id, next_id, cache) values(0, 1, 128);

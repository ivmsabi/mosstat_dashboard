CREATE TABLE cpi (
    year INT,
    month VARCHAR(10),
    value FLOAT
);

CREATE TABLE income (
    year INT,
    value FLOAT
);

CREATE TABLE poverty (
    year INT,
    value FLOAT
);

CREATE TABLE disease (
    year INT,
    disease_class VARCHAR(100),
    cases INT
);

CREATE TABLE medical_staff (
    year INT,
    staff_type VARCHAR(100),
    count INT,
    per_10k FLOAT
);
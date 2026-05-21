CREATE DATABASE IF NOT EXISTS webtech_lab;
USE webtech_lab;

-- Table for Question 4, 5, 8 (Registration and Authentication)
CREATE TABLE IF NOT EXISTS registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    gender ENUM('male', 'female', 'others') NOT NULL,
    faculty VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Question 9-12 (Books Management)
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publisher VARCHAR(150) NOT NULL,
    author VARCHAR(150) NOT NULL,
    edition VARCHAR(50) NOT NULL,
    no_of_page INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    publish_date DATE NOT NULL,
    isbn VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

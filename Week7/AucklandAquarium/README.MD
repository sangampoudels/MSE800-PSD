# Auckland Aquarium Management System

## Project Description

The Auckland Aquarium Management System is a Python-based application developed to manage fish inventory in an aquarium.

The system allows users to:
- Add fish categories
- Store fish records in a database
- Display fish inventory with quantities
- Manage aquarium data efficiently

This project demonstrates the implementation of Object-Oriented Programming (OOP) concepts and Design Patterns in Python.

---

# Fish Categories

The aquarium manages the following fish types:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

---

# Features

- Add fish to aquarium inventory
- Display fish category and quantity
- Store data using SQLite database
- Menu-driven system
- User-friendly console interface
- Persistent data storage

---

# Design Patterns Used

## 1. Factory Design Pattern

The Factory Pattern is used to create fish objects dynamically without exposing object creation logic.


### Benefits
- Reduces code duplication
- Improves scalability
- Simplifies object creation

---

## 2. Singleton Design Pattern

The Singleton Pattern ensures that only one instance of the database or aquarium system exists during program execution.

### Benefits
- Centralized data management
- Memory efficient
- Prevents multiple database instances

---

# Technologies Used

- Python 3
- SQLite3 Database
- Object-Oriented Programming (OOP)

---

# Project Structure
aquarium_management_system
│
├── fish.py
├── factory.py
├── singleton.py
├── database.py
├── main.py
├── aquarium.db
└── README.md
```

---

# Database Information

The project uses SQLite database.

Database file:

```text
aquarium.db
```

Table used:

```sql
fish_inventory
```

Columns:
- id
- fish_category
- quantity





# Learning Outcomes

Through this project, the following concepts were practiced:
- Python programming
- OOP principles
- Factory Design Pattern
- Singleton Design Pattern
- Database management using SQLite
- File and project organization

---

# Conclusion

This project successfully demonstrates how design patterns can be implemented in a real-world aquarium management system using Python and SQLite database integration.
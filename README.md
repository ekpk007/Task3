# Task 3: FastAPI Web API

This project implements a simple web API using **FastAPI** to perform basic arithmetic and string operations.

## Features

- `POST /add_numbers`: Add two numbers
- `POST /subtract_numbers`: Subtract two numbers
- `POST /concat_strings`: Concatenate two strings
- `POST /remove_substring`: Remove a substring from a string
- Input validation using **Pydantic**
- Interactive API documentation with **Swagger UI**

---

## Setup

### 1. Install dependencies

```sh
pip install fastapi uvicorn
```

## Or create 📦 requirements.txt

This file lists all the Python packages required to run the project.

### ✅ How to install:

```sh
pip install -r requirements.txt
```

---

### 2. Run the server

```sh
uvicorn app:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

### 3. Explore Swagger UI

After starting the server, open this in your browser:

```
http://127.0.0.1:8000/docs
```

You can interact with the API directly using the Swagger UI interface.

---

## API Endpoints & Testing

You can test all endpoints using `curl` or Swagger UI.

---

### 🔹 Add Numbers

**Endpoint:** `POST /add_numbers`

```sh
curl -X POST http://127.0.0.1:8000/add_numbers -H "Content-Type: application/json" -d '{"a":5, "b":3}'
```

**Response:**

```json
{
  "result": 8
}
```

---

### 🔹 Subtract Numbers

**Endpoint:** `POST /subtract_numbers`

```sh
curl -X POST http://127.0.0.1:8000/subtract_numbers -H "Content-Type: application/json" -d '{"a":10, "b":4}'
```

**Response:**

```json
{
  "result": 6
}
```

---

### 🔹 Concatenate Strings

**Endpoint:** `POST /concat_strings`

```sh
curl -X POST http://127.0.0.1:8000/concat_strings -H "Content-Type: application/json" -d '{"s1":"hello", "s2":"world"}'
```

**Response:**

```json
{
  "result": "helloworld"
}
```

---

### 🔹 Remove Substring

**Endpoint:** `POST /remove_substring`

```sh
curl -X POST http://127.0.0.1:8000/remove_substring -H "Content-Type: application/json" -d '{"s":"helloworld", "substr":"lo"}'
```

**Response:**

```json
{
  "result": "helworld"
}
```

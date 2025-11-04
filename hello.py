from fastapi import FastAPI

app = FastAPI(title="Sample FastAPI App", version="1.0.0")

# 1️⃣ Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI on Azure!"}

# 2️⃣ Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User_{user_id}", "status": "active"}

# 3️⃣ Create a new user
@app.post("/users")
def create_user(user: dict):
    name = user.get("name", "Unknown")
    age = user.get("age", None)
    return {"message": f"User {name} (age {age}) created successfully!"}

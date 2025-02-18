from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    salary: int 
    experience: int


class EmployeeUpdate(BaseModel):
    name: str
    salary: int 
    experience: int

class EmployeePartialUpdate(BaseModel):
    name: Optional[str] = None
    salary: Optional[int] = None
    experience: Optional[int] = None



employees = [
    {'id': 1, 'name': 'John Doe', 'is_active': True, 'salary': 55000, 'experience': 5},
    {'id': 2, 'name': 'Jane Smith', 'is_active': False, 'salary': 62000, 'experience': 7},
    {'id': 3, 'name': 'Sam Brown', 'is_active': True, 'salary': 48000, 'experience': 3},
    {'id': 4, 'name': 'Alice Johnson', 'is_active': True, 'salary': 75000, 'experience': 10},
    {'id': 5, 'name': 'Bob White', 'is_active': True, 'salary': 54000, 'experience': 4},
]



# Initialize the fastAPI app
app = FastAPI()

@app.get("/employees")
def get_all_employees():
    return employees


# Path parameter
@app.get("/employees/{employee_id}")
def get_single_employee(employee_id: int):

    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    
    return JSONResponse(content={"message": "Employee not found!"}, status_code=status.HTTP_404_NOT_FOUND)



@app.post("/employees")
def create_employee(employee: EmployeeCreate):
    new_employee = {
        'id': 10,
        'name': employee.name,
        'is_active': True,
        'salary': employee.salary,
        'experience': employee.experience
    }

    employees.append(new_employee)

    return JSONResponse(content={"success": "Employee created successfully"},status_code=status.HTTP_201_CREATED)


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate):
    return JSONResponse(
        content = {"success": "Employee updated successfully"},
        status_code=status.HTTP_200_OK
    )


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    return JSONResponse(
        content = {"success": "Employee deleted successfully"},
        status_code=status.HTTP_204_NO_CONTENT
    )


@app.patch("/employees/{employee_id}")
def partial_update(employee_id: int, employee: EmployeePartialUpdate):
    
    if employee.name:
        print("Update employee name")

    if employee.salary:
        print("Update employee salary")

    if employee.experience:
        print("Update employee experience")
    
    return JSONResponse(
        content = {"success": "Employee updated successfully"},
        status_code=status.HTTP_200_OK
    )
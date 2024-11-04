// Global variable to store the JWT token

let token = null;



// Login function

async function login() {

    const username = document.getElementById('username').value;

    const password = document.getElementById('password').value;



    try {

        const response = await fetch(`${BASE_URL}/api/auth/`, {

            method: 'POST',

            headers: { 'Content-Type': 'application/json' },

            body: JSON.stringify({ username, password })

        });

        

        const data = await response.json();

        if (response.ok) {

            token = data.token;

            document.getElementById('login-form').style.display = 'none';

            document.getElementById('content').style.display = 'block';

        } else {

            alert('Login failed');

        }

    } catch (error) {

        console.error('Error:', error);

        alert('An error occurred during login');

    }

}




// Fetch Departments

async function getDepartments() {

    if (!token) return alert('Please log in');



    try {

        const response = await fetch(`${BASE_URL}/api/departments/`, {

            headers: { 'Authorization': `JWT ${token}` }

        });

        

        const departments = await response.json();

        const departmentList = document.getElementById('department-list');

        departmentList.innerHTML = '';

        departments.forEach(department => {

            const li = document.createElement('li');

            li.textContent = `${department.name}`;

            departmentList.appendChild(li);

        });

    } catch (error) {

        console.error('Error:', error);

    }

}



// Fetch Positions

async function getPositions() {

    if (!token) return alert('Please log in');



    try {

        const response = await fetch('/api/positions/', {

            headers: { 'Authorization': `JWT ${token}` }

        });

        

        const positions = await response.json();

        const positionList = document.getElementById('position-list');

        positionList.innerHTML = '';

        positions.forEach(position => {

            const li = document.createElement('li');

            li.textContent = `${position.name} - Salary: $${position.salary}`;

            positionList.appendChild(li);

        });

    } catch (error) {

        console.error('Error:', error);

    }

}



// Fetch Employees

async function getEmployees() {

    if (!token) return alert('Please log in');



    try {

        const response = await fetch('/api/employees/', {

            headers: { 'Authorization': `JWT ${token}` }

        });

        

        const employees = await response.json();

        const employeeList = document.getElementById('employee-list');

        employeeList.innerHTML = '';

        employees.forEach(employee => {

            const li = document.createElement('li');

            li.textContent = `${employee.name} ${employee.surname} - ${employee.position.name}`;

            employeeList.appendChild(li);

        });

    } catch (error) {

        console.error('Error:', error);

    }

}
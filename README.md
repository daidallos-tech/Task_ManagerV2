# Task_ManagerV2

### ❓About Task ManagerV2.

That's my first project with SQL database (I'm still learning). There is CRUD system in this project, I chose it because I want to practice DB + Python and understand what I do and why I do that.
This application can:
1 - ADD a TASK
2 - SHOW your TASKS
3 - UPDATE your TASK
4 - DELETE your TASK
As I said earlier it's a clean CRUD system.

P.S Why I called this project "V2" because two or three weeks ago I've created the same project, but that was awful actually. There is a JSON saves in first project and almost spaghetti code.

### 🏛️ Project Architecture

📁 TASK_MANAGERV2/  
│
├── 📁 db/
│ ├── database.py  
│ └── repository.py  
│
├── 📁 models/
│ └── task.py  
│
├── 📁 service/
│ └── task_service.py  
│
├── 📜 .env  
├── 📜 .gitignore  
├── 📜 LICENSE  
├── 📜 main.py  
├── 📜 README.md  
└── 📜 requirements.txt

### 💻How to run Locally?

1. Clone and Navigate

```bash
git clone <your-repository-url>
cd Task_ManagerV2
```

2. Set Up the Environment.
   Create a `.env` file in the root directory and add your PostgreSQL credentials:

```text
DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
```

3. Install Dependencies.
   For mac or linux

```bash
source .venv/bin/activate
```

For windows

```bash
.venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

4. Boot Up the App

```bash
python main.py
```

🔧 Technologies Used

- **Python 3.12+**
- **PostgreSQL**
- **Psycopg2** (Sinfonous DB Driver)
- **Python-Dotenv** (Environment Management)

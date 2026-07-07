# Task_ManagerV2

❓ About Task ManagerV2

That's my first project with an SQL database (I'm still learning). There is a CRUD system in this project. I chose it because I want to practice DB + Python and understand what I do and why I do it.

This application can:
1 - ADD a TASK
2 - SHOW your TASKS
3 - UPDATE your TASK
4 - DELETE your TASK

As I said earlier, it's a clean CRUD system.

P.S. Why did I call this project "V2"? Because two or three weeks ago I created the same project, but that was awful, actually. There were JSON saves in the first project and it was almost spaghetti code.

---

🏛️ Project Architecture

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

---

💻 How to run Locally?

1. Clone and Navigate

```bash
git clone <your-repository-url>
cd Task_ManagerV2
```

2. Set Up the Environment
   Create a `.env` file in the root directory and add your PostgreSQL credentials:

```text
DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
```

3. Install Dependencies
   For Mac or Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

Then install all required modules at once:

```bash
pip install -r requirements.txt
```

4. Boot Up the App

```bash
python main.py
```

---

🔧 Technologies Used

- **Python 3.12+**
- **PostgreSQL**
- **Psycopg2** (Synchronous DB Driver)
- **Python-Dotenv** (Environment Management)

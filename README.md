# 🧠 Lifemaxxing Tracker

A personal full-stack web app for tracking and optimizing key life goals — from fitness and finances to social reach and habits.

Built with **React** (Vite + TailwindCSS + DaisyUI) on the frontend and **FastAPI** (SQLModel + SQLite) on the backend.

---

## 🚀 Overview

This app is designed to help you "lifemaxx" — track growth across key dimensions of self-improvement:
- 📈 Followers (LinkedIn, IG, etc.)
- 💸 Financial milestones (income, savings, net worth)
- 💪 Fitness (lifting stats, weight, bodyfat)
- 🧠 Learning (books read, hours studied, etc.)
- 🤝 Social and relationship goals

It's a private dashboard meant for daily/weekly input and reflection — the kind of data you'd normally forget.

---

## 🛠 Tech Stack

### Frontend:
- React + Vite
- TailwindCSS + DaisyUI
- shadcn/ui (optional UI components)
- Axios for API calls

### Backend:
- FastAPI
- SQLModel + SQLite (simple local DB, easy to migrate to PostgreSQL)
- CORS enabled for dev
- Future: add auth layer (JWT or Supabase)

---

## 🧩 Features (WIP)

- [x] Add/update metrics across categories
- [x] Clean dashboard with filter/sort
- [ ] Visualization with charts (Recharts / Chart.js)
- [ ] Habit streak tracking
- [ ] Streak alerts / push notifications
- [ ] Editable categories + dynamic goals
- [ ] Login system

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/lifemaxxing.git
cd lifemaxxing
```

### 2. Start backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Start frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🌱 Why This Project?

"What gets measured gets managed."

This project helps you become your own performance coach — setting goals, tracking progress, and staying accountable.

---

## 📸 Screenshots

*(Add screenshots of the dashboard and forms here)*

---

## 🧠 Long-Term Vision

This is a personal prototype for a broader idea: a customizable self-optimization platform. The eventual vision includes:

- Community features
- AI reflection prompts
- Visual goal timelines
- Privacy-first data handling

---

## 🧊 Author

**Evan Phillips**  
Currently building cool tools, learning fast, and maxxing life.  
📫 DM me on GitHub or email [you@example.com]

---

## 📝 License

MIT License.

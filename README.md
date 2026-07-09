# AI-First CRM Assistant

An AI-powered Customer Relationship Management (CRM) application designed for pharmaceutical sales representatives. The application leverages Large Language Models (LLMs) to automate interaction logging, generate follow-up action items, prioritize healthcare professional visits, and prepare meeting briefs through a natural language interface.

---

## Features

### 🤖 AI Interaction Logging
- Log Healthcare Professional (HCP) interactions using natural language.
- AI extracts structured information including:
  - HCP Name
  - Hospital
  - Interaction Type
  - Date & Time
  - Attendees
  - Discussion Topics
  - Materials Shared
  - Sentiment
  - Outcome
  - Follow-up Actions
- Automatically populates the interaction form for review before saving.

---

### ✏️ AI Interaction Editing
Modify any extracted field using natural language.

Examples:

- "Change the sentiment to Neutral"
- "Update the follow-up to next Monday"
- "Change the interaction type to Phone Call"

Only the requested field is updated without affecting the remaining information.

---

### ✅ AI Action Item Generation
After an interaction is saved, the AI automatically generates follow-up action items.

Each action item includes:
- Task
- Priority
- Due Date
- Status

Action items can be viewed and managed from the Action Items page.

---

### 📋 AI Action Item Dashboard
View all pending and completed action items grouped by Healthcare Professional.

Features:
- Search
- Priority indicators
- Completion tracking
- Progress overview

---

### 🗺️ AI Visit Planner
Generate a prioritized visit plan using natural language.

Example:

```
Plan my visits for today
```

The system ranks Healthcare Professionals using:
- Pending follow-ups
- Pending action items
- Previous interaction sentiment

The planner displays:
- Visit priority
- Priority score
- Recommendation reason

---

### 💬 AI Meeting Preparation
Prepare for upcoming meetings with Healthcare Professionals.

Example:

```
Prepare me for my meeting with Dr. Emily Johnson
```

The AI generates a meeting brief including:
- Previous discussion summary
- Pending action items
- Suggested talking points
- Materials to carry

---

## Tech Stack

### Frontend

- React
- TypeScript
- Redux Toolkit
- React Router
- Axios
- CSS
- React Hot Toast

### Backend

- FastAPI
- LangGraph
- LangChain
- SQLAlchemy
- PostgreSQL
- Pydantic

### AI

- Google Gemini
- Structured Output Extraction

---

## Project Structure

```
frontend/
│
├── components/
├── pages/
├── redux/
├── services/
└── App.tsx

backend/
│
├── ai/
├── api/
├── database/
├── langgraph/
├── models/
├── prompts/
├── schemas/
├── services/
└── main.py
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

---

### 2. Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file inside the backend folder.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost/database_name

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 4. Start Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

### 5. Frontend Setup

Navigate to frontend.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Database

The application uses PostgreSQL.

Tables include:

- hcps
- interactions
- action_items

Tables are automatically created when the backend starts.

---

## Example Workflow

### Log Interaction

```
I met Dr. Sarah Williams at Aster Medcity today. We discussed our latest oncology therapy and reimbursement support. She requested additional safety data and a follow-up meeting next Tuesday.
```

↓

AI extracts the interaction

↓

User reviews

↓

Save Interaction

↓

Action items generated automatically

---

### Plan Visits

```
Plan my visits for today
```

↓

AI calculates visit priorities

↓

Visit Planner opens

---

### Prepare Meeting

```
Prepare me for my meeting with Dr. Sarah Williams
```

↓

AI generates a meeting brief using previous interactions and pending action items.

---

## AI Workflow

```
User
      │
      ▼
 AI Chat Assistant
      │
      ▼
 LangGraph Router
      │
 ┌────┼──────────────┬──────────────┬─────────────┐
 │    │              │              │             │
 ▼    ▼              ▼              ▼             ▼

Log  Edit      Visit Planner   Meeting Prep   Action Items
 │
 ▼
FastAPI Services
 │
 ▼
PostgreSQL
 │
 ▼
Gemini
```

---

## Future Improvements

- Calendar Integration
- Email Follow-up Generation
- Offline Mobile Support
- Authentication & Role-Based Access
- Analytics Dashboard
- Voice Interaction Logging
- Multi-user Collaboration

---

## Author

Developed as part of the VectorShift Frontend Technical Assessment.

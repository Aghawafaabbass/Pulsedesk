# ✦ PulseDesk
### Clinical Management System — Django

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Aghawafaabbass-181717?style=flat&logo=github&logoColor=white)

> A production-grade, multi-app Django clinical management system — demonstrating real-world Full Stack Development patterns including role-based access, relational data modelling, multi-app architecture, and a professional responsive UI.

---

## 🚀 Live Demo

👉 **Coming soon — deploying on Render.com**

---

## 👨‍💻 Developer

**Agha Wafa Abbas**
**Full Stack Developer | Lecturer, School of Computing**

| Institution | Location | Email |
|------------|----------|-------|
| University of Portsmouth | Winston Churchill Ave, Southsea, Portsmouth PO1 2UP, UK | agha.wafa@port.ac.uk |
| Arden University | Coventry, United Kingdom | awabbas@arden.ac.uk |
| Pearson | London, United Kingdom | — |
| IVY College of Management Sciences | Lahore, Pakistan | wafa.abbas.lhr@rootsivy.edu.pk |

---

## 🏭 Real-World Use Cases

This system reflects patterns used across multiple industries:

- **Private Clinics** — Patient registration, appointment scheduling, medical records
- **Family Health Teams** — Ontario/Canada multi-doctor practices
- **Walk-in Clinics** — High-volume appointment management
- **Physiotherapy Centers** — Session tracking and patient history
- **Dental Offices** — Appointment lifecycle management
- **Mental Health Clinics** — Confidential record keeping
- **Healthcare Startups** — MVP clinical management product
- **University Teaching** — Real-world Django multi-app architecture reference

---

## 👥 User Roles

| Role | Access | How They Use It |
|------|--------|-----------------|
| **System Admin** | Full access | Manages departments, staff accounts, system config |
| **Receptionist** | Frontend dashboard | Registers patients, books appointments, updates status |
| **Doctor** | Frontend dashboard | Views appointments, adds medical records |
| **Patient** | Physical visit only | Registered by receptionist — no system login |

---

## ✨ Features

### Patient Management
- 🔐 Controlled registration — admin/receptionist only
- 📋 Full patient profiles — health card, blood type, emergency contact
- 📁 Medical records — diagnosis, prescription, clinical notes
- 🔍 Search by name or health card number

### Appointment System
- 📅 Book appointments — patient + doctor + date + time
- 🔄 5-stage lifecycle — Scheduled → Confirmed → Completed → Cancelled → No Show
- 🔍 Filter by status, date, doctor or patient
- 📊 Real-time stats dashboard

### Staff Management
- 👨‍⚕️ Doctor, Nurse, Receptionist, Admin roles
- 🏥 Department assignment
- 📋 License number, specialization, availability
- 📅 Schedule management

### System
- ⚙️ Django Admin — fully configured
- 🌑 Professional dark UI — all devices
- 📱 Fully responsive
- 🔐 Session-based authentication

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+ / Django 4.x |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Google Fonts — Syne + DM Sans |
| Auth | Django contrib.auth |
| Admin | Django Admin (customized) |
| Version Control | Git + GitHub |
| Deployment | Render.com (coming soon) |

---

## 🗄️ Figure 1 — Entity Relationship Diagram (ERD)

```
┌──────────────┐      ┌──────────────────┐      ┌──────────────────┐
│     USER     │      │   DEPARTMENT     │      │     SCHEDULE     │
│──────────────│      │──────────────────│      │──────────────────│
│ id (PK)      │      │ id (PK)          │      │ id (PK)          │
│ username     │      │ name             │      │ staff_id (FK)    │
│ first_name   │      │ description      │      │ day_of_week      │
│ last_name    │      │ created_at       │      │ start_time       │
│ email        │      └────────┬─────────┘      │ end_time         │
│ password     │               │ 1              │ is_available     │
│ is_staff     │               │ N              └──────────────────┘
└──────┬───────┘      ┌────────▼─────────┐
       │ 1            │      STAFF       │
       ├──────────────│──────────────────│
       │              │ id (PK)          │
       │              │ user_id (FK)     │
       │              │ role             │
       │              │ department(FK)   │
       │              │ specialization   │
       │              │ license_number   │
       │              │ phone            │
       │              │ is_available     │
       │              └────────┬─────────┘
       │                       │ 1 (doctor)
       │ 1                     │ N
       │              ┌────────▼─────────┐
       ├──────────────│   APPOINTMENT    │
       │ N            │──────────────────│
       │              │ id (PK)          │
       │              │ patient_id (FK)  │
       │              │ doctor_id (FK)   │
       │              │ date             │
       │              │ time             │
       │              │ type             │
       │              │ status           │
       │              │ reason           │
       │              └──────────────────┘
       │ 1
       │              ┌──────────────────┐      ┌──────────────────┐
       └──────────────│    PATIENT       │      │  MEDICALRECORD   │
                   N  │──────────────────│      │──────────────────│
                      │ id (PK)          │◄─1───│ id (PK)          │
                      │ user_id (FK)     │  N   │ patient_id (FK)  │
                      │ health_card      │      │ diagnosis        │
                      │ date_of_birth    │      │ prescription     │
                      │ blood_type       │      │ notes            │
                      │ phone            │      │ created_by (FK)  │
                      │ emergency_contact│      │ created_at       │
                      └──────────────────┘      └──────────────────┘
```

---

## 🔄 Figure 2 — Request Sequence Diagram

```
Browser        URL Router     Middleware      View           Database
   │               │              │             │               │
   │─POST /login───►              │             │               │
   │               │─match───────►│             │               │
   │               │              │─auth────────►               │
   │◄──redirect /appointments/────│             │               │
   │               │              │             │               │
   │─GET /appointments/────────────────────────►│               │
   │               │              │             │─Appt.all()────►
   │               │              │             │◄──queryset────│
   │◄──200 HTML Response──────────────────────── │               │
   │               │              │             │               │
   │─POST /appointments/add/───────────────────►│               │
   │               │              │             │─Appt.create()─►
   │               │              │             │◄──saved───────│
   │◄──302 redirect────────────────────────────│               │
```

---

## 🏗️ Figure 3 — System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      PRODUCTION                           │
│                                                           │
│   Internet                                                │
│      │                                                    │
│      ▼                                                    │
│   ┌──────────────┐                                        │
│   │   Render.com │  ← Cloud platform, HTTPS auto          │
│   │   WSGI Server│                                        │
│   └──────┬───────┘                                        │
│          │                                                │
│          ▼                                                │
│   ┌────────────────────────────────────┐                  │
│   │         DJANGO APPLICATION         │                  │
│   │  patients · appointments · staff   │                  │
│   │  Views · Models · Templates · Auth │                  │
│   └──────────────┬─────────────────────┘                  │
│                  │                                        │
│                  ▼                                        │
│   ┌──────────────────────────────────┐                    │
│   │           SQLite DB              │                    │
│   │  Users · Patients · Staff        │                    │
│   │  Appointments · MedicalRecords   │                    │
│   └──────────────────────────────────┘                    │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                      DEVELOPMENT                          │
│   Browser ──► Django runserver (8000) ──► SQLite          │
└──────────────────────────────────────────────────────────┘
```

---

## 📊 Figure 4 — Appointment State Machine

```
                    APPOINTMENT LIFECYCLE
   
   ┌────────────┐  Confirm   ┌─────────────┐  Complete  ┌───────────┐
   │ SCHEDULED  │───────────►│  CONFIRMED  │───────────►│ COMPLETED │
   └─────┬──────┘            └─────────────┘            └───────────┘
         │
         │ Cancel                          No Show
         ▼                                    ▼
   ┌────────────┐                      ┌───────────┐
   │ CANCELLED  │                      │  NO SHOW  │
   └────────────┘                      └───────────┘

   APPOINTMENT TYPES:
   General Checkup · Follow Up · Emergency · Specialist · Lab Test
```

---

## ⚡ Figure 5 — URL & API Flow

```
FRONTEND (Browser)              BACKEND (Django Views)

GET  /                     ──► LoginView (Django built-in)
GET  /appointments/        ──► appointment_list() → stats + filter
POST /appointments/add/    ──► add_appointment()  → Appointment.create()
POST /appointments/<id>/status/ ──► update_status() → appt.save()
GET  /patients/            ──► patient_list()    → Patient.all()
GET  /patients/<id>/       ──► patient_detail()  → records + appointments
POST /patients/add/        ──► add_patient()     → User.create() + Patient.create()
POST /patients/<id>/record/──► add_medical_record() → MedicalRecord.create()
GET  /staff/               ──► staff_list()      → Staff.all()
POST /staff/add/           ──► add_staff()       → User.create() + Staff.create()
GET  /admin/               ──► Django Admin (superuser only)
GET  /logout/              ──► LogoutView → redirect to /
```

---

## 📦 Quick Setup

```bash
# 1. Clone
git clone https://github.com/Aghawafaabbass/Pulsedesk.git
cd Pulsedesk

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install
pip install -r requirements.txt

# 4. Database
python manage.py migrate

# 5. Admin user
python manage.py createsuperuser

# 6. Run
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```
Pulsedesk/
├── manage.py
├── requirements.txt
├── README.md
├── docs/
│   └── PulseDesk_Complete_Guide.docx
├── pulsedesk/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── patients/
│   ├── models.py       ← Patient, MedicalRecord
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── appointments/
│   ├── models.py       ← Appointment
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── staff/
│   ├── models.py       ← Staff, Department, Schedule
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── templates/
    ├── base.html
    ├── registration/
    │   └── login.html
    ├── patients/
    ├── appointments/
    └── staff/
```

---

## 🔮 Future Enhancements

- [ ] Role-based permissions (Doctor vs Receptionist vs Admin)
- [ ] Patient login portal
- [ ] Email notifications for appointments
- [ ] Invoice & billing system
- [ ] REST API with Django REST Framework
- [ ] PostgreSQL for production
- [ ] Docker containerization

---

## 📄 License

MIT License

---

<div align="center">
<strong>PulseDesk</strong> — Built with Django<br/>
<em>Full Stack Developer · Agha Wafa Abbas</em><br/>
<a href="https://github.com/Aghawafaabbass">GitHub</a>
</div>

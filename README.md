# AI-Powered Personalized Learning MVP

## Description

This MVP is designed to deliver a truly personalized, standards-based learning experience for K–12 students—starting with 8th-grade math. It uses AI to prescribe learning paths based on either historical data (like standardized test scores) or an optional diagnostic pre-assessment.

Once a student's starting point is established, the system assigns appropriate learning modules that include:

- AI-generated instructional videos using avatars
- Interactive, standards-aligned practice activities
- Project-based learning menus
- Progress monitoring and mastery tracking

The goal is to provide a student dashboard that adapts in real-time to performance, while also offering tools for teachers and parents to monitor and support the learning journey.

The project is being developed in Streamlit for rapid prototyping, with future plans to expand into a modular system with dashboards for different users (students, teachers, parents).

## Infographic

![image](https://github.com/user-attachments/assets/3a3adc58-de62-4d52-8d6f-fb97c516d924)

## Features

- Personalized learning paths
- AI-powered pre-assessment
- Visual and project-based instruction
- ... (Add more)

...

# 📊 AI-Powered Learning Personalizer (Pilot: 8th Grade Math)



> A mastery-based learning engine powered by diagnostic pre-assessments, personalized skill paths, and dynamic progress monitoring — built for real student growth.

---

## 🧠 What Problem This Solves  
Students often receive grade-level instruction that doesn’t reflect what they’re truly ready to learn. This project replaces GPA-based assumptions with diagnostic pre-assessments that pinpoint each student's entry point and generate a personalized vertical learning plan aligned to key standards.

---

## 👤 Target Users  
- Students (initial pilot: 8th Grade Math)  
- Teachers viewing student readiness, gaps, and growth  
- (Optional) Parents receiving weekly skill updates  

---

## 📥 Inputs  
- Pre-assessment scores per student, aligned to specific standards (e.g. CCSS.Math.Content.8.EE.1)  
- Optional: past standardized test data or placement exam results  
- Student name/ID and optional background info  

---

## 📤 Outputs  
- Personalized Learning Plan based on diagnostic results  
- Mastery tracker for each skill within the learning path  
- Streamlit dashboard showing current level, progress, and suggested next steps  
- Optional GPT-generated lesson prompts or visual explanations  

---

## 🛠️ Tech Stack & Tools  
- Python (Pandas for data processing)  
- Streamlit (app interface)  
- Altair or Matplotlib (for visualization)  
- Optional: GPT-4 for explanation generation or lesson prompts  
- Standards reference set (e.g., Common Core)  

---

## ✅ Success Criteria  
- Upload mock or real student diagnostic data  
- System identifies vertical entry point based on gaps  
- Personalized skill roadmap is generated  
- Dashboard displays learning trajectory with mastery visualization  
- Optional: exportable PDF or printable learning plan for teacher/parent  

---

## 🔄 Learning Loop Model  
1. 🧪 Diagnostic Pre-Assessment  
2. 🎯 Personalized Skill Path (vertical + standards-aligned)  
3. 📘 AI-supported Learning Resources (video, GPT summary, project options)  
4. 📊 Progress Monitoring + Skill Mastery  
5. 🔁 Reassessment + Learning Path Update  

---
### 🧭 Visual: Personalized Learning Loop

```mermaid
graph TD
    A[🧪 Pre-Assessment] --> B[🎯 Identify Entry Point]
    B --> C[🗺️ Personalized Skill Path]
    C --> D[📘 AI Resources & Practice]
    D --> E[📊 Progress Monitoring]
    E --> F[🔁 Reassessment & Next Step]
    F --> C

## 🔭 Future Add-Ons  
- Risk Score / Engagement Tracker (AI Retention Coach)  
- Parent View with plain-language weekly reports  
- Project-based learning menu linked to current skill level  
- Avatar-powered instruction module (HeyGen integration)

---

## 📂 Project Status  
🚧 In development – vertical learning path framework in progress

---


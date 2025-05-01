# Lesson Tagging Schema

This document outlines the lesson tagging system used in the True North Learning Platform to align instructional content with selected academic standards and support personalized learning pathways.

---

## 🎯 Purpose

Tagging lessons with structured metadata allows the platform to:
- Dynamically map lessons to various state/national standards (Common Core, NCTM, etc.)
- Support personalized recommendations based on student assessments
- Enable standards-aligned reporting and teacher dashboards
- Power flexible curriculum structures for public, private, or homeschool settings

---

## 🏷️ Tagging Categories

Each lesson will include structured tags from the following categories:

### 1. **Domain Area**
- `Math`
- `ELA`
- `Science` (future)
- `Social Studies` (future)

### 2. **Grade Band**
- `Grade 3`
- `Grade 4`
- ...
- `Grade 8`
- `Grade 9`

### 3. **Strand/Topic**
- For Math (examples):
  - `Operations and Algebraic Thinking`
  - `Expressions and Equations`
  - `Statistics and Probability`
  - `Functions`
- For ELA (examples):
  - `Reading Literature`
  - `Writing Informative`
  - `Speaking and Listening`

### 4. **Standard Reference**
- Example formats:
  - `CCSS.MATH.CONTENT.6.EE.B.5`
  - `WY.MATH.7.NS.2`
  - `NCTM.Math.Process.Standard_1`

### 5. **Skill Tags**
- Bite-sized skills or sub-competencies derived from the standard.
  - `write variable expressions`
  - `solve linear equations`
  - `identify figurative language`

### 6. **Depth of Knowledge (DOK)**
- `Level 1: Recall`
- `Level 2: Skills and Concepts`
- `Level 3: Strategic Thinking`
- `Level 4: Extended Thinking`

### 7. **Lesson Type**
- `Mini-Lesson`
- `Project-Based`
- `Interactive Activity`
- `Video Tutorial`
- `Assessment`
- `Practice Exercise`

### 8. **AI Status**
- `AI-Generated`
- `Human-Reviewed`
- `Hybrid`
- `Needs Review`

---

## 🧩 Example JSON Format (for developers)

```json
{
  "lesson_title": "Solving Two-Step Equations",
  "domain": "Math",
  "grade_level": "Grade 7",
  "strand": "Expressions and Equations",
  "standard_code": "CCSS.MATH.CONTENT.7.EE.B.4",
  "skills": ["solve two-step equations", "apply inverse operations"],
  "DOK": "Level 2: Skills and Concepts",
  "lesson_type": "Mini-Lesson",
  "ai_status": "Hybrid"
}

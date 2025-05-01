# 📚 Standards Selection & Mapping System

## Purpose
To enable flexible, scalable curriculum development and personalization by allowing schools or families to select from multiple learning standards frameworks (e.g., NCTM, NCTE, state-specific, or Common Core) while maintaining a unified internal skills progression system.

---

## 🌍 Target Use Cases
- Private or microschool opting for NCTM/NCTE-based frameworks
- Homeschooling families seeking flexibility or custom tracks
- Public schools needing Common Core or state-aligned options
- Schools switching between standards without losing student data

---

## 🧩 Phase 1: Standards Framework Selection (Onboarding)

**Standards Options:**

### Math:
- [ ] NCTM Core Math Framework *(default for private/hybrid schools)*
- [ ] Common Core State Standards
- [ ] State-Specific (e.g., Wyoming Math Standards)
- [ ] Custom Upload (future feature)

### ELA/Literacy:
- [ ] NCTE/National ILA Progressions *(default for private/hybrid schools)*
- [ ] Common Core ELA Standards
- [ ] State-Specific ELA Standards
- [ ] Custom Upload (future feature)

> ✅ Display names in UX can use phrasing like:
> “National Standards-Aligned” or “Evidence-Based Literacy Path”

---

## 🔗 Phase 2: Internal Standards Mapping Engine

All content (lessons, assessments, skills, microcredentials) will be internally tagged using **skill IDs** that map to multiple standards frameworks.

### Example Structure:
| Skill ID | Description                      | NCTM | Common Core | WY Standards |
|----------|----------------------------------|------|-------------|---------------|
| M4.1     | Add/Subtract multi-digit numbers | 4.NBT.B.4 | 4.NBT.B.4 | WY.M.4.2.1   |
| ELA5.2   | Determine theme in literature     | RL.5.2 | RL.5.2 | WY.RL.5.2     |

> This enables crosswalks between frameworks and universal lesson tagging.

---

## 🎛️ Phase 3: Smart Pathways Engine (Under Development)

- Adjusts diagnostic assessments, skill maps, and recommendations based on the selected standards path.
- Enables seamless transition if standards change (student progress persists).
- In future: supports AI-generated custom learning plans from uploaded district frameworks.

---

## 🚀 Phase 4: Admin + Partner Tools (Future Roadmap)

- Admin dashboard to switch frameworks mid-year if needed
- Upload/import tool for district-specific standards
- “Compare Frameworks” feature to show overlap and differences
- Standards impact report: which lessons satisfy which frameworks

---

## 🛠️ Developer Notes

### Standards Mapping Schema (JSON Example):
```json
{
  "skill_id": "M4.1",
  "description": "Add and subtract multi-digit numbers",
  "nctm": "NCTM.NBT.4",
  "common_core": "4.NBT.B.4",
  "wyoming": "WY.M.4.2.1"
}

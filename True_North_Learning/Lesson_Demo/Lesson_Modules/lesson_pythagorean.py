# lesson_pythagorean.py

import streamlit as st

def pythagorean_theorem_lesson():
    st.title("🔺 Unlocking Right Triangles: The Power of the Pythagorean Theorem")
    st.subheader("8th Grade Geometry • Prove and Apply the Pythagorean Theorem")

    st.markdown("""
    ### ✅ Lesson Objectives
    - Understand what the Pythagorean Theorem is and when to use it.
    - Prove how and why it works using a visual example.
    - Solve real-world and mathematical problems involving right triangles.
    
    ### 🟡 Real-Life Hook
    Imagine this: You’re building a ramp for your dog to get into the back of your truck. You know how high the truck is from the ground and how long the ramp is. But how far away should the ramp start?

    That’s where today’s secret weapon — the **Pythagorean Theorem** — comes in!

    ### 🔵 Mini-Lesson: What Is the Pythagorean Theorem?
    In a **right triangle**, the square of the **hypotenuse** (the longest side) is equal to the sum of the squares of the other two sides.

    **Formula**: `a² + b² = c²`

    Example:
    - a = 3, b = 4
    - `3² + 4² = 9 + 16 = 25 → c = 5`

    ### 🔺 Prove It!
    Use graph paper or digital drawings to compare the areas of squares off each triangle side. You’ll find the big square (on the hypotenuse) always equals the two smaller ones combined.

    ### 🟢 Guided Practice
    **Problem**: A ladder is 10 ft long and sits 6 ft from a wall. How high does it reach?

    - `6² + b² = 10²`
    - `36 + b² = 100 → b² = 64 → b = 8 ft`

    ✅ The ladder reaches **8 feet** up the wall.

    ### 🔴 Independent Practice
    1. a = 5, b = 12, c = ?
    2. a = 9, c = 15, b = ?
    3. a = 8, b = 15, c = ?

    ### ⚡️ Challenge Problem
    A drone flies 30 meters north, then 40 meters east. How far is it from the starting point?

    ### 🤖 Ask the AI
    - “Can you walk me step-by-step through a problem using my own numbers?”
    - “Create a real-world problem using sports or construction.”

    ### 🎯 Exit Reflection
    - What clicked for you today?
    - What do you want to review again tomorrow?
    """)

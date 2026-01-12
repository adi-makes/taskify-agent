# Taskify Agent - Usage Examples

This document provides practical examples of how to use Taskify Agent for academic planning.

## Example 1: Basic Study Plan Creation

### Scenario
You have 3 exams coming up and want to create a study schedule.

### Steps
1. Upload your exam timetable PDF
2. Upload syllabus PDFs for each subject
3. Ask: "Create a study plan for my upcoming exams. I can study 6 hours per day."

### Expected Output
- Exam summary with urgency levels
- Day-by-day study schedule
- Break times and subject rotation
- Warnings about time constraints

---

## Example 2: Emergency Planning (Exam in 3 Days)

### Scenario
You have an exam in 3 days and haven't started studying.

### Steps
1. Upload exam timetable and syllabus
2. Upload previous year question papers (PYQs)
3. Ask: "I have an exam in 3 days. Help me focus on the most important topics."

### Expected Output
- Emergency mode activated
- Focus on high-weightage PYQ topics only
- Intensive revision schedule
- Topics to skip due to time constraints

---

## Example 3: Handling Assignment Conflicts

### Scenario
You have an assignment due while preparing for exams.

### Steps
1. Upload exam timetable
2. Tell the agent: "I have a programming assignment due on Jan 15th, estimated 8 hours of work."
3. Ask: "Adjust my study plan to fit this assignment."

### Expected Output
- Conflict analysis
- Prioritization recommendation
- Adjusted schedule with assignment blocks
- Daily hour limits respected

---

## Example 4: Rescheduling After Missed Sessions

### Scenario
You missed 2 days of studying and need to catch up.

### Steps
1. Tell the agent: "I missed studying on Jan 10th and 11th. Can you replan?"
2. Provide updated availability

### Expected Output
- Full replanning (not just shifting)
- Reassessed priorities
- Possible scope reduction suggestions
- Realistic catch-up schedule

---

## Example 5: PYQ-Based Priority Planning

### Scenario
You want to focus on topics that appear most frequently in exams.

### Steps
1. Upload multiple PYQ PDFs
2. Upload syllabus
3. Ask: "Analyze the PYQs and tell me which topics to prioritize."

### Expected Output
- PYQ frequency analysis table
- High-priority topics identified
- Study plan weighted toward frequent topics
- Low-priority topics marked for skipping if needed

---

## Tips for Best Results

### ✅ Do This
- Provide complete exam dates and times
- Upload clear, readable PDFs
- Specify your daily study hour availability
- Mention any constraints (part-time job, other commitments)
- Ask for adjustments when your situation changes

### ❌ Avoid This
- Uploading corrupted or password-protected PDFs
- Expecting plans for >10 hours/day of study
- Not mentioning important deadlines
- Ignoring the agent's warnings about time constraints

---

## Sample Conversation Flow

```
You: [Upload exam_timetable.pdf]

Agent: 📄 I've received your exam timetable. Let me analyze it...

📅 Exam Summary:
- Mathematics: Jan 20, 2026 (8 days away) 🔵
- Physics: Jan 22, 2026 (10 days away) 🔵
- Chemistry: Jan 25, 2026 (13 days away) 🔵

To create an effective study plan, I need:
1. How many hours per day can you study?
2. Do you have syllabi for these subjects?
3. Any previous year question papers?

You: I can study 5 hours per day. [Upload syllabus_math.pdf, syllabus_physics.pdf]

Agent: Perfect! Creating your personalized study plan...

[Generates detailed day-by-day schedule with tables]
```

---

## Advanced Features

### Custom Time Preferences
"I prefer studying in the morning from 6-9 AM and evening from 7-10 PM"

### Subject Priorities
"I'm weak in Physics, please allocate more time for it"

### Progress Tracking
"I've completed Calculus and Algebra. Update my plan."

### Revision Requests
"Add extra revision sessions for Chemistry"

---

## Troubleshooting

**Problem**: Agent can't read my PDF
- **Solution**: Ensure PDF is not scanned image-only. Use text-based PDFs.

**Problem**: Plan shows unrealistic hours
- **Solution**: Specify your constraints clearly: "Maximum 6 hours per day"

**Problem**: Missing important topics
- **Solution**: Upload complete syllabus and mention: "Make sure to cover all topics"

**Problem**: Agent asks for today's date
- **Solution**: This shouldn't happen. Report as a bug if it does.

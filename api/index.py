@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "Please provide at least one name"}

    marks = []
    for student_name in name:
        mark = next((student["marks"] for student in students_data 
                     if student["name"].lower() == student_name.lower()), None)
        marks.append(mark)
    return marks  # Yahan pura list hi return kar rahe hain, bina "marks" key ke

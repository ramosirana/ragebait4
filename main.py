from pyscript import document

def gwa(event):
    # name collection
    fname = document.getElementById("fname").value.strip()
    lname = document.getElementById("lname").value.strip()
    fullname = f"{fname} {lname}".strip()

    # subject ids
    subjects = ["sci", "eng", "math", "fil", "ict", "pe"]
    grades = []

    # grade collection
    for subj in subjects:
        value = document.getElementById(subj).value
        if value:
            try:
                grade = float(value)
                grades.append(grade)
            except ValueError:
                pass

    # calculation
    if not grades:
        result_text = "please enter at least one valid grade."
    else:
        gwa_value = sum(grades) / len(grades)
        grades_str = ", ".join(f"{g:.0f}" for g in grades)
        result_text = (
            f"<strong>Name:</strong> {fullname}<br>"
            f"<strong>Grades:</strong> {grades_str}<br>"
            f"<strong>GWA:</strong> {gwa_value:.2f}"
        )

    # replacement process: removal of old
    existing = document.getElementById("result")
    if existing:
        existing.remove()
    # replacement process: addition of new
    result_div = document.createElement("div")
    result_div.id = "result"
    result_div.innerHTML = result_text
    result_div.style.marginTop = "20px"
    result_div.style.fontSize = "18px"
    result_div.style.fontFamily = "Alan Sans"
    result_div.style.textAlign = "center"

    # appending it below grade area
    document.getElementById("small2").appendChild(result_div)

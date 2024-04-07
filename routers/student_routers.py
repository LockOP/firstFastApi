from fastapi import APIRouter
from controllers.student_controllers import create_student, list_students, get_student, update_student, delete_student

router = APIRouter()

# Student Routes
router.post("/students")(create_student)
router.get("/students")(list_students)
router.get("/students/{id}")(get_student)
router.patch("/students/{id}")(update_student)
router.delete("/students/{id}")(delete_student)

# Optionally, you can include additional routes for other functionalities

# Example:
# router.get("/students/{id}/courses", get_student_courses)
# router.post("/students/{id}/courses", enroll_student_course)

# Export the router

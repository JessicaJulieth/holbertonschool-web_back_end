export default function updateStudentGradeByCity(studentList, city, newGrade) {
  const students = studentList.filter((stud) => stud.location === city);
  return students.map((stud) => {
    const student = stud;
    const studGrade = newGrade.filter((grade) => grade.studentId === stud.id);
    if (studGrade.length !== 0) student.grade = studGrade[0].grade;
    else student.grade = 'N/A';
    return stud;
  });
}

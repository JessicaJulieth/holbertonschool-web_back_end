export default function getListStudentIds(studentList) {
  if (Array.isArray(studentList)) {
    return studentList.map((stud) => stud.id);
  } return [];
}

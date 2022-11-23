export default function getStudentsByLocation(studentList, city) {
  return studentList.filter((stud) => stud.location === city);
}

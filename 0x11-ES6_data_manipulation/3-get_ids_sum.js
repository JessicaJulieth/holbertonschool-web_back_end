export default function getStudentIdsSum(studentList) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  return studentList.reduce(reducer, 0);
}

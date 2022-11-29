const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);

function readDatabase(path) {
  return readFile(path, 'utf8').then((data) => {
    const student = {};

    const datalines = data.split('\n');
    const students = datalines.slice(1).map((line) => line.split(',')).filter((line) => line.length > 0 && line[0] !== '');

    for (const line of students) {
      if (!(line[3] in student)) {
        student[line[3]] = [];
      }
      student[line[3]].push(line[0]);
    }
    return student;
  }).catch(() => {
    throw new Error('Cannot load the database');
  });
}

module.exports = readDatabase;

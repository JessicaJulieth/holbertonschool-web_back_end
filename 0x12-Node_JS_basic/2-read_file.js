const fs = require('fs');

function countStudents(path) {
  let f;
  try {
    f = fs.readFileSync(path, 'utf-8').trim().split('\n');
  } catch (e) {
    throw Error('Cannot load the database');
  }
  let count = 0;
  const c = f.slice(1).reduce((p, c) => {
    count += 1;
    const fields = c.split(',');
    if (!p[fields[3]]) {
      Object.assign(p, {
        [fields[3]]: [],
      });
    }
    p[fields[3]].push(fields[0]);
    return p;
  }, {});
  console.log(`Number of students: ${count}`);
  for (const key of Object.keys(c)) {
    console.log(`Number of students in ${key}: ${c[key].length}. List: ${c[key].join(', ')}`);
  }
}

module.exports = countStudents;

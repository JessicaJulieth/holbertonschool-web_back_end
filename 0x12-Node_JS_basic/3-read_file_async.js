const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        return reject(Error('Cannot load the database'));
      }
      console.log(data);
      const lines = data.trim().split('\n');
      let count = 0;
      const c = lines.slice(1).reduce((p, c) => {
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
      return resolve();
    });
  });
}

module.exports = countStudents;

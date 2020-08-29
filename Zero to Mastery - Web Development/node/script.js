const fs = require('fs');

fs.readFile('', (err, data) => {
  if (err) {
    console.log('error');
  }
  console.log(data);
})
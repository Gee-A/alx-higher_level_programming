#!/usr/bin/node

const count = process.argv.length;

if (count < 4) {
  console.log('0');
} else {
  let biggest = Number(process.argv[2]);
  let second = Number(process.argv[2]);

  for (let i = 3; i < count; i++) {
    const current = Number(process.argv[i]);
    if (biggest === second && current < biggest) {
      second = process.argv[i];
    } else if (current < biggest && current > second) {
      second = current;
    } else if (current > biggest) {
      second = biggest;
      biggest = current;
    }
  }
  console.log(second);
}

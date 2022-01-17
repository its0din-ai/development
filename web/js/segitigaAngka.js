let hasil = "";
for (let i = 5; i > 0; i--) {
  if (i === 5) {
    for (let j = 1; j <= i; j++) {
      hasil += "1 ";
    }
  }
  if (i === 4) {
    for (let j = 1; j <= i; j++) {
      hasil += "2 ";
    }
  }
  if (i === 3) {
    for (let j = 1; j <= i; j++) {
      hasil += "3 ";
    }
  }
  if (i === 2) {
    for (let j = 1; j <= i; j++) {
      hasil += "4 ";
    }
  }
  if (i === 1) {
    for (let j = 1; j <= i; j++) {
      hasil += "5 ";
    }
  }
  hasil += "\n";
}
console.info(hasil);

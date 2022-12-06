function calculateNumber(type, a, b) {

  if (Number.isNaN(a) || Number.isNaN(b))
    throw TypeError;

  a = Math.round(a);
  b = Math.round(b);

  switch (type) {
    case 'SUM':
      return a + b;
    case 'SUBTRACT':
      return a - b;
    case 'DIVIDE':
      if (b === 0) {
        return 'Error';
      }
      return a / b;
    default:
      return 'Error';
  }
}

module.exports = calculateNumber;

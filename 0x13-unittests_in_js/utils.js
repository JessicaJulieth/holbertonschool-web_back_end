const Utils = {
  calculateNumber(type, a, b = 0) {
    if (Number.isNaN(a) || Number.isNaN(b))
      throw TypeError('Parameters must be numbers or able to coerce to number');

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
        return NaN;
    }
  }
};

module.exports = Utils;

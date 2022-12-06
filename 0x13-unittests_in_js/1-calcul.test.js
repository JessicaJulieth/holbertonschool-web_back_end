const calculateNumber = require("./1-calcul.js");
const assert = require("assert");

describe('calculateNumber', () => {
  it('should return rounded sum', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 2), 3);
    assert.strictEqual(calculateNumber('SUM', 1, 0), 1);
    assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
    assert.strictEqual(calculateNumber('SUM', -1, -2), -3);
    assert.strictEqual(calculateNumber('SUM', 1.6, 3), 5);
    assert.strictEqual(calculateNumber('SUM',-1.2, -3.8), -5);
  });
  it('should return rounded difference', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 1), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, -1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.8), -3);
    assert.strictEqual(calculateNumber('SUBTRACT',-1.2, -3.8), 3);
  });
  it('should return rounded quotient', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 5.2), 0.2);
  });
  it('should return Error string for zero division', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
  it('should return Error string for invalid operation', () => {
    assert.strictEqual(calculateNumber('sdf', 1, 0), 'Error');
  });

});

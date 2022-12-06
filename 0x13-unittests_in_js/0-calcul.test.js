const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    it('should add integers as expected', () => {
        assert.strictEqual(calculateNumber(1, 2), 3);
        assert.strictEqual(calculateNumber(1, -2), -1);
    });

    it('should round its arguments before addition', () => {
        assert.strictEqual(calculateNumber(1.1, 2.1), 3);
        assert.strictEqual(calculateNumber(1.4, 2.4), 3);
        assert.strictEqual(calculateNumber(0.9, 2.4), 3);
    });
});

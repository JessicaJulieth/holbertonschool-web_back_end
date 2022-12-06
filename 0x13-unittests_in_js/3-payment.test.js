const { expect } = require('chai');
const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber', () => {
    const calcNumSpy = sinon.spy(utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    const res = sendPaymentRequestToApi(100, 20);

    expect(calcNumSpy.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.equal(true);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(res);

    calcNumSpy.restore();
    consoleSpy.restore();
  });
});

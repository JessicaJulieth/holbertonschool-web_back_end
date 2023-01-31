const { expect } = require('chai');
const request = require('request');
const { spy } = require('sinon');


const options = {
  hostname: '127.0.0.0',
  port: 7865,
  method: 'GET'
}

describe('index page', () => {
  spy(console, 'log');

  it('status code', () => {
    request('http://localhost:7865/', function(err, res, body) {
      console.log(res.statusCode);
      expect(console.log.calledWith(200)).to.be.true;
    });
  });
  it('body returns', () => {
    request('http://localhost:7865/', function(err, res, body) {
      console.log(body);
      expect(console.log.calledWith('Welcome to the payment system')).to.be.true;
    });
  });
  it('get', () => {
    request('http://localhost:7865/', function(err, res, body) {
      console.log(res.request.method);
      expect(console.log.calledWith('GET')).to.be.true;
    });
  });
});

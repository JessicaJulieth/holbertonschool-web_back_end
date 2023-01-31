const { expect, assert } = require('chai');
const request = require('request');
const { spy, stub } = require('sinon');


describe('index page', () => {
  // spy(console, 'log');
  beforeEach(() => {
    this.get = stub(request, 'get');
    this.post = stub(request, 'post');
  });

  afterEach(() => {
    request.get.restore();
    request.post.restore();

  });

  it('status code', () => {
    request('http://localhost:7865/cart/12', function(err, res, body) {
      expect(res.statusCode).to.equal(200);
    });
  });
  it('status code', () => {
    request('http://localhost:7865/cart/hello', function(err, res, body) {
      expect(res.statusCode).to.equal(404);
    });
  });
  it('body returns 1', () => {
    request('http://localhost:7865/', function(err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
    });
  });


  it('body returns 2', () => {
    request('http://localhost:7865/cart/12', function(err, res, body) {
      expect(body).to.equal('Payment methods for cart 12');
    });
  });

  it('get?', () => {
    request('http://localhost:7865/', function(err, res, body) {
      expect(res.request.method).to.equal('GET');
    });
  });

  it('get', () => {
    request('http://localhost:7865/available_payments', function(err, res, body) {
      expect(res.request.method).to.equal('GET');
    });
  });

  it('get payments', () => {
    request('http://localhost:7865/available_payments', function(err, res, body) {
      expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
    });
  });


  it('poster', () => {
    request({
      headers: { 'content-type': 'application/json' },
      method: 'POST',
      url: 'http://localhost:7865/login',
      body: '{ "userName": "Betty" }'
    }, function(err, res, body) {
      expect(body).to.equal('Welcome Betty');
    });
  });
  it('Post?', () => {
    request({
      headers: { 'content-type': 'application/json' },
      url: 'http://localhost:7865/login',
      method: 'POST',
      body: '{ "userName": "Betty" }'
    }, function(err, res, body) {
      expect(res.request.method).to.deep.equal('POST');
    });
  });

});

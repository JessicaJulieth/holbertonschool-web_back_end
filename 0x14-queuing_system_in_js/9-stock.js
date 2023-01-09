const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const client = redis.createClient();

const app = express();
const port = 1245;

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  for (const product of listProducts) {
    if (product.id == id) return product;
  }
  return {};
}
function reserveStockById(itemId, stock) {
  const product = getItemById(itemId);
  if (product) {
    client.hmset(itemId.toString(), 'itemId', product.id, 'itemName',
    product.name, 'price', product.price, 'initialAvailableQuantity',
    product.stock, 'currentQuantity', stock);
  }
}

async function getCurrentReservedStockById(itemId) {
  const asyncGet = promisify(client.hgetall).bind(client);
  const res = await asyncGet(itemId);
  return res;
}

app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)));
app.get('/list_products/:itemId', async (req, res) => {
  const ret = await getCurrentReservedStockById(req.params.itemId);
  if (ret) res.send(ret)
  else res.json({'status':'Product not found'}); 
});
app.get('/reserve_product/:itemId', (req, res) => {
  const product = getItemById(req.params.itemId);
  if (!product) res.json({'status':'Product not found'});
  if (product.stock > 0) {
    reserveStockById(product.id, product.stock - 1);
    res.json({'status':'Reservation confirmed', 'itemId':product.id});
  } else res.json({'status':'Not enough stock available','itemId':product.id})
})

app.listen(port);
module.exports = app;

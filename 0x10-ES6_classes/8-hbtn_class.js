export default class HolbertonClass {
  constructor(size, location) {
    if (typeof (size) === 'number') this._size = size;
    if (typeof (location) === 'string') this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this._location;
    if (hint === 'number') return this._size;
    return this;
  }
}

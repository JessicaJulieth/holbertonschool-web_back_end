export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const array = new Int8Array(buffer, 0, length);
  if (position >= 0 && position < length) array[position] = value;
  else throw Error('Position outside range');
  return buffer;
}

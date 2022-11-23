export default function cleanSet(set, startString) {
  let string = '';
  if (typeof (startString) === 'string' && startString !== '') {
    set.forEach((val) => {
      if (val.includes(startString)) string = string.concat(`-${val.replace(startString, '')}`);
    });
    string = string.substring(1);
  }
  return string;
}

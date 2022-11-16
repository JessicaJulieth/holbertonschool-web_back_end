import signUpUser from './4-all-reject';
import uploadPhoto from './5-all-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName);
  let photo = null;
  try {
    photo = await uploadPhoto(fileName);
  } catch (e) {
    photo = `${e.name}: ${e.message}`;
  }
  const x = { status: 'fulfilled', value: user };
  const y = { status: 'rejected', value: photo };
  return [x, y];
}

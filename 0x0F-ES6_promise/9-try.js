export default function guardrail(mathFunction) {
    const queue = [];
    let val = 0;
    try {
      val = mathFunction();
    } catch (e) {
      val = `${e.name}: ${e.message}`;
    }
    queue.push(val);
    queue.push('Guardrail was processed');
    return queue;
  }

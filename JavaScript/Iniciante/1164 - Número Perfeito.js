let N = parseInt(lines.shift());

for (let i = 0; i < N; i++) {
    let X = parseInt(lines.shift());
    let numero = 0;
    for (let l = 1; l < X; l++) {
        if (X%l === 0) {
            numero += l;
        }
    }
    if (numero === X) {
        console.log(`${X} eh perfeito`);
    } else {
        console.log(`${X} nao eh perfeito`);
    }
}

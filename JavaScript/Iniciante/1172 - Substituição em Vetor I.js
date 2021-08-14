let vetorX = [];
let elemento;
for (let i = 0; i < 10; i++) {
    elemento = parseInt(lines.shift());
    if (elemento > 0) {
        vetorX.push(elemento);
    } else {
        vetorX.push(1);
    }
}

for (let l = 0; l<10; l++) {
    console.log(`X[${l}] = ${vetorX[l]}`);
}

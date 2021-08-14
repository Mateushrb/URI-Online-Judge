let vetor = Array();
let elemento;
for (let i = 0; i<100; i++) {
    elemento = parseFloat(lines.shift());
    vetor.push(elemento.toFixed(1));
}
for (let l = 0; l<100; l++) {
    if (vetor[l] <= 10) {
        console.log(`A[${l}] = ${vetor[l]}`);
    }
}

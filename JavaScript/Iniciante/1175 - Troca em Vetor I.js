let vetor = Array();
let elemento;

for (let i = 0; i<20; i++) {
    elemento = parseInt(lines.shift());
    vetor.push(elemento);
}
let inicio;
let fim;
let num = 19;
for (let l = 0; l<10; l++) {
    inicio = vetor[l];
    fim = vetor[num];
    vetor[l] = fim;
    vetor[num] = inicio;
    num -= 1;
}

for (let s = 0; s < 20; s++) {
    console.log(`N[${s}] = ${vetor[s]}`);
}

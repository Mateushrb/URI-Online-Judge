let vetor = Array();
let V = parseInt(lines.shift());

for (let i = 0; i<10; i++) {
    vetor.push(V);
    V *= 2;
}
for (let l = 0; l<10; l++) {
    console.log(`N[${l}] = ${vetor[l]}`);
}

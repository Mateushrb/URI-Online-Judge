let N = Array();
let T = parseInt(lines.shift());

let qtd = Math.ceil(1000/T);

for (let i = 0; i <= qtd; i++) {
    for (let l = 0; l < T; l++) {
        N.push(l);
    }
}

let vetor = Array();

for (let s = 0; s < 1000; s++) {
    vetor.push(`N[${s}] = ${N[s]}`);
}

for (let m = 0; m < vetor.length; m++) {
    console.log(vetor[m]);
}

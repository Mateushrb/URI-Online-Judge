let linha = lines.shift().split(' ');

let A = parseInt(linha[0]);
let N;

for (let l = 1; l <= linha.length; l++) {
    if (linha[l] > 0) {
        N = parseInt(linha[l]);
        break;
    }
}

let soma = 0;
let i = 0;

while (i < N) {
    soma += A + i;
    i += 1;
}
console.log(soma);

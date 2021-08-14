let N = parseInt(lines.shift());
let X = lines.shift().split(' ');

let menorElemento = +Infinity;
let posicao = Number;

for (let i = 0; i<N; i++) {
    if (parseInt(X[i]) < menorElemento) {
        menorElemento = X[i],
        posicao = i
    } else {

    }
}

console.log(`Menor valor: ${menorElemento}`);
console.log(`Posicao: ${posicao}`);

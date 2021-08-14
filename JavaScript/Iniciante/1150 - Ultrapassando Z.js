let X = parseInt(lines.shift());

let Z = -Infinity;

while (Z <= X) {
    Z = parseInt(lines.shift());
}

let soma = X;
let qtd = 1;
X += 1;

while (soma < Z) {
    soma += X;
    qtd += 1;
    X += 1;
}

console.log(qtd);

const n1 = parseInt(lines.shift());
const n2 = parseInt(lines.shift());

let X;
let Y;

if (n1 > n2) {
    X = n1;
    Y = n2;
} else {
    X = n2;
    Y = n1;
}

let soma = 0;

for (let i = Y; i <= X; i++) {
    if (i%13 !== 0) {
        soma += i;
    } else {

    }
}

console.log(soma);

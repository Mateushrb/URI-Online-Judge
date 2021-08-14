let n1 = parseInt(lines.shift());
let n2 = parseInt(lines.shift());

let X;
let Y;

if (n1 < n2) {
    X = n1;
    Y = n2;
} else {
    X = n2;
    Y = n1;
}

let resto;

for (let i = X+1; i < Y; i++) {
    resto = i%5;
    if (resto === 2 || resto === 3) {
        console.log(i);
    }
}

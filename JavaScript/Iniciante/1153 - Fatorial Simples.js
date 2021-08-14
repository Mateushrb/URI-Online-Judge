let N = parseInt(lines.shift());
let resultado = N;

while (N != 1) {
    N -= 1;
    resultado *= N;
}

console.log(resultado);

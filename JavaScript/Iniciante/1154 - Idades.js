let idade = 0;
let soma = 0;
let divisor = 0;
while (idade >= 0) {
    soma += idade;
    divisor += 1;
    idade = parseInt(lines.shift());
}

divisor -= 1;
console.log((soma/divisor).toFixed(2));

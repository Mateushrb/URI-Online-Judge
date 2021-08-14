let valor = parseFloat(lines.shift());
console.log('NOTAS:');

let notas100 = parseInt(valor/100)
console.log(`${notas100} nota(s) de R$ 100.00`);

valor %= 100;
valor = valor.toFixed(2);
let notas50 = parseInt(valor/50);
console.log(`${notas50} nota(s) de R$ 50.00`);

valor %= 50;
valor = valor.toFixed(2);
let notas20 = parseInt(valor/20);
console.log(`${notas20} nota(s) de R$ 20.00`);

valor %= 20;
valor = valor.toFixed(2);
let notas10 = parseInt(valor/10);
console.log(`${notas10} nota(s) de R$ 10.00`);

valor %= 10;
valor = valor.toFixed(2);
let notas5 = parseInt(valor/5);
console.log(`${notas5} nota(s) de R$ 5.00`);

valor %= 5;
valor = valor.toFixed(2);
let notas2 = parseInt(valor/2);
console.log(`${notas2} nota(s) de R$ 2.00`);

valor %= 2;
valor = valor.toFixed(2);

console.log('MOEDAS:');

let moeda1 = parseInt(valor);
console.log(`${moeda1} moeda(s) de R$ 1.00`);

valor %= 1;
valor = valor.toFixed(2);
let moedas50 = parseInt(valor/0.5);
console.log(`${moedas50} moeda(s) de R$ 0.50`);

valor = valor%0.5;
valor = valor.toFixed(2);
let moedas25 = parseInt(valor/0.25);
console.log(`${moedas25} moeda(s) de R$ 0.25`);

valor = valor%0.25;
valor = valor.toFixed(2);
let moedas10 = parseInt(valor/0.10);
console.log(`${moedas10} moeda(s) de R$ 0.10`);

valor = valor%0.10;
valor = valor.toFixed(2);
let moedas5 = parseInt(valor/0.05);
console.log(`${moedas5} moeda(s) de R$ 0.05`);

valor = valor%0.05;
valor = valor.toFixed(2);
let moedas1 = parseInt(valor/0.01);
console.log(`${moedas1} moeda(s) de R$ 0.01`);

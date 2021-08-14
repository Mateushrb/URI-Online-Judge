let alcool = 0;
let gasolina = 0;
let diesel = 0;
let tipo = 0;

while (true) {
    tipo = parseInt(lines.shift());
    if (tipo === 1) {
        alcool += 1;
    } else if (tipo === 2) {
        gasolina += 1;
    } else if (tipo === 3) {
        diesel += 1;
    } else if (tipo === 4) {
        break;
    } else {

    }
}

console.log('MUITO OBRIGADO');
console.log(`Alcool: ${alcool}`);
console.log(`Gasolina: ${gasolina}`);
console.log(`Diesel: ${diesel}`);

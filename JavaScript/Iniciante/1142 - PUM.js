const N = parseInt(lines.shift());
let numero = 0;
let linha;
for (let i = 0; i < N; i++) {
    linha = '';
    for (let l = 0; l < 3; l++) {
        numero += 1;
        linha += String(numero);
        linha += ' ';
    }
    numero += 1;
    linha += 'PUM';
    console.log(linha);
}

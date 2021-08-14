let dados = lines.shift().split(' ');
let X = parseInt(dados[0]);
let Y = parseInt(dados[1]);

let linha = '';
let rep;

if (Y%X === 0) {
    rep = Y/X;
} else {
    rep = parseInt(Y/X) + 1;
}

let elemento = 1;

for (let i = 0; i < rep; i++) {
    linha += String(elemento);
    elemento += 1;
    if (elemento > Y+1) {
        break;
    } else {

    }

    for (let l = 1; l < X; l++) {
        linha += ' ';
        linha += String(elemento);
        elemento += 1;
        if (elemento > Y) {
            break;
        } else {

        }
    }
    console.log(linha);
    linha = '';
}

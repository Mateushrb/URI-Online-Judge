const N = parseInt(lines.shift());
let linha1;
let linha2;

for (let i = 1; i <= N; i++) {
    linha1 = '';
    linha2 = '';

    for (let l = 1; l < 3; l++) {
        linha1 += String(Math.pow(i, l));
        linha1 += ' ';
    }
    linha1 += String(Math.pow(i, 3));

    linha2 += String(i);
    for (let s = 2; s <= 3; s++) {
        linha2 += ' ';
        linha2 += String(Math.pow(i, s) + 1);
    }

    console.log(linha1);
    console.log(linha2);
}

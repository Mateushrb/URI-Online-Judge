let par = Array();
let impar = Array();

for (let i = 0; i < 15; i++) {
    let valor = parseFloat(lines.shift());

    if (valor%2 === 0) {
        if (par.length < 5) {
            par.push(valor);
        } else {
            for (let l = 0; l < 5; l++) {
                console.log(`par[${l}] = ${par[l]}`);
            }
            par = Array();
            par.push(valor);
        }
    } else {
        if (impar.length < 5) {
            impar.push(valor);
        } else {
            for (let s = 0; s < 5; s++) {
                console.log(`impar[${s}] = ${impar[s]}`);
            }
            impar = Array();
            impar.push(valor);
        }
    }
}

if (impar.length > 0) {
    for (let n = 0; n < impar.length; n++) {
        console.log(`impar[${n}] = ${impar[n]}`);
    }
}
if (par.length > 0) {
    for (let m = 0; m < par.length; m++) {
        console.log(`par[${m}] = ${par[m]}`);
    }
}

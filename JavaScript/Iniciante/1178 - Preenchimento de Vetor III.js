let X = parseFloat(lines.shift()).toFixed(4);

let N = Array();
N.push(X);
console.log(`N[0] = ${N[0]}`);

for (let i = 1; i < 100; i++) {
    N.push(X);
    X = (X/2).toFixed(6);
    console.log(`N[${i}] = ${formatarDecimais(X)}`);
}

function formatarDecimais(numero){
    let valoresDecimais = (numero.toString().split('.')[1]);

    if(valoresDecimais[4]<=5 && valoresDecimais[5]==0){
        return numero.toString().split('.')[0] + '.' + valoresDecimais[0] + valoresDecimais[1] + valoresDecimais[2] + valoresDecimais[3];
    }
    return parseFloat(numero).toFixed(4);
}

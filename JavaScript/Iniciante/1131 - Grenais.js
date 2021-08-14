let grenais = 0;
let inter = 0;
let gremio = 0;
let empates = 0;

while (true) {
    let gols = lines.shift().split(' ');

    if (parseInt(gols[0]) > parseInt(gols[1])) {
        inter += 1;
    } else if (parseInt(gols[0]) < parseInt(gols[1])) {
        gremio += 1;
    } else {
        empates += 1;
    }

    grenais += 1;

    let repetir = 0;
    while (repetir < 1 || repetir > 2) {
        console.log('Novo grenal (1-sim 2-nao)');
        repetir = parseInt(lines.shift());
    }

    if (repetir === 2) {
        break;
    } else {
        
    }
}

console.log(`${grenais} grenais`);
console.log(`Inter:${inter}`);
console.log(`Gremio:${gremio}`);
console.log(`Empates:${empates}`);

if (inter > gremio) {
    console.log('Inter venceu mais');
} else if (inter < gremio) {
    console.log('Gremio venceu mais');
} else {
    console.log('Nao houve vencedor');
}

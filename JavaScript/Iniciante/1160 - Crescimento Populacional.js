let T = parseInt(lines.shift());

for (let i = 0; i<T; i++) {
    let dados = lines.shift().split(' ');

    let PA = parseInt(dados[0]);
    let PB = parseInt(dados[1]);

    let G1 = parseFloat(dados[2]);
    let G2 = parseFloat(dados[3]);

    let tempo = 0;

    let crescimentoPA;
    let crescimentoPB;

    while (tempo < 102 && PA <= PB) {
        crescimentoPA = parseInt((PA*G1)/100);
        PA += crescimentoPA;
        crescimentoPB = parseInt((PB*G2)/100);
        PB += crescimentoPB;
        tempo++;
    }

    if (tempo < 101) {
        console.log(`${tempo} anos.`);
    } else {
        console.log('Mais de 1 seculo.');
    }
}

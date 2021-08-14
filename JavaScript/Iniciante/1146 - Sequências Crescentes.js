while (true) {
    let X = parseInt(lines.shift());
    let linha
    if (X === 0) {
        break;
    } else {
        linha = '1';
        for (let i = 2; i <= X; i++) {
            linha += ' ';
            linha += String(i);
        }
        console.log(linha);
    }
}

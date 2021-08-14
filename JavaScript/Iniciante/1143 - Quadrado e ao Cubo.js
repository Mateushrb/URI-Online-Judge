const N = parseInt(lines.shift());

for (let i = 1; i <= N; i++) {
    let linha = '';
    linha += String(i);
    linha += ' ';
    linha += String(i*i);
    linha += ' ';
    linha += String(i*i*i);
    console.log(linha);
}

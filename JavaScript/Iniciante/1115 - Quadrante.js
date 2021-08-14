let coordenadas;
let X;
let Y;

while (true) {
    coordenadas = lines.shift().split(' ');
    X = parseInt(coordenadas[0]);
    Y = parseInt(coordenadas[1]);

    if (X === 0 || Y === 0) {
        break;
    } else {
        if (X > 0) {
            if (Y > 0) {
                console.log('primeiro');
            } else {
                console.log('quarto');
            }
        } else {
            if (Y > 0) {
                console.log('segundo')
            } else {
                console.log('terceiro')
            }
        }
    }
}

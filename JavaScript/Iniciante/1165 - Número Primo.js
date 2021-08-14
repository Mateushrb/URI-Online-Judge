let N = parseInt(lines.shift());

for (let i = 0; i<N; i++) {
    let X = parseInt(lines.shift());
    let P = 0;
    for (let l = 2; l < X; l++) {
        if (X % l !== 0) {

        } else {
            console.log(`${X} nao eh primo`);
            P += 1;
            break;
        }
    }
    if (P === 0) {
        console.log(`${X} eh primo`);
    }
}

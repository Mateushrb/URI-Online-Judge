const N = parseInt(lines.shift())

let valor

for (let i = 0; i < N; i++) {
    valor = parseInt(lines.shift())
    if (valor === 0) {
        console.log('NULL')
    } else {
        if (valor%2 === 0) {
            if (valor > 0) {
                console.log('EVEN POSITIVE')
            } else {
                console.log('EVEN NEGATIVE')
            }
        } else {
            if (valor > 0) {
                console.log('ODD POSITIVE')
            } else {
                console.log('ODD NEGATIVE')
            }
        }
    }
}

let x = parseInt(lines.shift())

if (x % 2 === 0) {
    x += 1
}

for (let i = x; i<=x+11; i += 2) {
    console.log(i)
}

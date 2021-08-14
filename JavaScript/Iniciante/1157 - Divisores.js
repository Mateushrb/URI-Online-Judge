const N = parseInt(lines.shift());

for (let i = 1; i <= N; i++) {
    if (N%i === 0) {
        console.log(i);
    }
}

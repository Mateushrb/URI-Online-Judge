let S = 0;

let dividendo = 1;
let divisor = 1;

for (let i = 1; i < 21; i++) {
    S += dividendo/divisor;
    dividendo += 2;
    divisor *= 2;
}

console.log(S.toFixed(2));

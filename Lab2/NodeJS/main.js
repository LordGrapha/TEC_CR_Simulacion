function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}

randoms = ""
random_limit = 10000;
for (let index = 0; index < random_limit; index++) {
    randoms = randoms + (getRandomInt(1, 100000)/100000) + " ";
}

console.log(randoms);

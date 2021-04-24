let width = document.getElementById("canvas").width;
let height = document.getElementById("canvas").height;
const title = document.getElementById("title")
const ctx = document.getElementById("canvas").getContext("2d");
const cnv = document.getElementById("canvas");
let halt = document.getElementById('halt-simulation')
let running = true

class Grass {
    constructor(){
        this.x = Math.round(Math.random()*width)
        this.y = Math.round(Math.random()*height)
        // this.img = "../images/grass.png"
        this.energy = 5
    }
}

halt.addEventListener("click", function() {
    running = false
})

function main_loop() {
    if (running === true) {
        let grasses = []
        let grass = new Grass()
        grasses.push(grass)
        console.log(grasses)

        let grassImage = document.createElement('img')
        grassImage.src = "grass.png"
        ctx.drawImage(grassImage,grass.x,grass.y)

        console.log(grassImage)

        window.requestAnimationFrame(main_loop)
    }
}

window.requestAnimationFrame(main_loop);



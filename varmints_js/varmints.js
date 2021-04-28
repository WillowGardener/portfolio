let width = document.getElementById("canvas").width;
let height = document.getElementById("canvas").height;
const title = document.getElementById("title")
const ctx = document.getElementById("canvas").getContext("2d");
const cnv = document.getElementById("canvas");
let halt = document.getElementById('halt-simulation')
let running = true
let prey_list = []
let grass_list = []

halt.addEventListener("click", function() {
    running = false
})

class Grass {
    constructor(){
        this.x = Math.round(Math.random()*width)
        this.y = Math.round(Math.random()*height)
        // this.img = "../images/grass.png"
        this.energy = 5
    }
}

class Animal {
    constructor(){
        this.age = 0
        this.pregnant = false
        this.x = Math.round(Math.random()*width)
        this.y = Math.round(Math.random()*height)
        this.awareness = 25
        this.speed = 3
        this.x_move = Math.round(Math.random()*this.speed)
        this.y_move = Math.round(Math.random()*this.speed)
    }
    move() {
        this.x += this.x_move
        this.y += this.y_move
        if (this.x > width) {
            this.x_move*=-1
            this.x = width
        }
        if (this.x < 0) {
            this.x_move*=-1
            this.x = 0
        }
        if (this.y > height) {
            this.y_move*=-1
            this.y = height
        } 
        if (this.y < 0) {
            this.y_move*=-1
            this.y = 0
        }

    }
}

class Prey extends Animal {

}

function startup() {
    for (i=0; i<20; i++) {
        let prey = new Prey()
        prey_list.push(prey)
    }
}

function main_loop() {
    if (running === true) {
        
        let grass = new Grass()
        grass_list.push(grass)
        let grassImage = document.createElement('img')
        grassImage.src = "grass.png"
        ctx.drawImage(grassImage,grass.x,grass.y)

        

        window.requestAnimationFrame(main_loop)
    }
}

startup()
window.requestAnimationFrame(main_loop);

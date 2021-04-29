let width = document.getElementById("layer1").width;
let height = document.getElementById("layer1").height;
const title = document.getElementById("title")
const ctx = document.getElementById("layer1").getContext("2d");
const cnv = document.getElementById("layer1");

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
        let grassImage = document.createElement('img')
        grassImage.src = "grass.png"
        this.img = grassImage
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
    constructor(){
        super()
        let preyImage = document.createElement('img')
        preyImage.src = "rabbit.png"
        this.img = preyImage
    }
}

function startup() {
    for (i=0; i<20; i++) {
        let prey = new Prey()
        prey_list.push(prey)
    }
}

function main_loop() {
    if (running === true) {
        ctx.clearRect(0,0,width,height)
    

        let grass = new Grass()
        grass_list.push(grass)

        grass_list.forEach(function(grass){
            ctx.drawImage(grass.img,grass.x,grass.y)
        })
        
        prey_list.forEach(function(prey){
            prey.move()
            ctx.drawImage(prey.img,prey.x,prey.y)
        })

           

        window.requestAnimationFrame(main_loop)
    }
}

startup()
window.requestAnimationFrame(main_loop);

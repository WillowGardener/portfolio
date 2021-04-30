let width = document.getElementById("layer1").width;
let height = document.getElementById("layer1").height;
const title = document.getElementById("title")
const ctx = document.getElementById("layer1").getContext("2d");
const cnv = document.getElementById("layer1");

let halt = document.getElementById('halt-simulation')
let running = true
let preyList = []
let grassList = []

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

const testGrass = new Grass()

class Animal {
    constructor(){
        this.age = 0
        this.pregnant = false
        this.x = Math.round(Math.random()*width)
        this.y = Math.round(Math.random()*height)
        this.awareness = 25
        this.speed = 3
        this.size = 16
        this.x_move = Math.round(Math.random()*this.speed)
        this.y_move = Math.round(Math.random()*this.speed)
    }
    checkProximity(target) {
        let distance_x = Math.abs(this.x-target.x)
        let distance_y = Math.abs(this.y-target.y)
        let distance = Math.sqrt(distance_x*distance_x+distance_y*distance_y)
        return distance
    }
    checkAdjacent(target) {
        let distance = this.checkProximity(target)
        if (distance < 4) {
            return true
        }
    }
    eat(target_array){
        
        target_array.forEach((target) => {
            
            let proximity = this.checkProximity(target)
            let edible = this.checkAdjacent(target)
            if (edible === true) {
                this.energy += target.energy
                target_array.splice(target)
                
            }
            else if (proximity <= this.awareness) {
                this.moveToward(target)
            }
        })
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
    moveToward(target) {
        if (this.x >= target.x) {
            this.x_move = -1*this.speed
        }
        else if (this.x <= target.x) {
            this.x_move = this.speed
        }
        if (this.y >= target.y) {
            this.y_move = -1*this.speed
        }
        else if (this.y <= target.y) {
            this.y_move = this.speed
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
    for (i=0; i<2; i++) {
        let prey = new Prey()
        preyList.push(prey)
    }
}

function main_loop() {
    if (running === true) {
        ctx.clearRect(0,0,width,height)
    

        let grass = new Grass()
        grassList.push(grass)

        grassList.forEach(function(grass){
            ctx.drawImage(grass.img,grass.x,grass.y)
        })
        
        preyList.forEach(function(prey){
            prey.eat(grassList)
            prey.move()
            ctx.drawImage(prey.img,prey.x,prey.y)
        })

           

        window.requestAnimationFrame(main_loop)
    }
}

startup()
window.requestAnimationFrame(main_loop);

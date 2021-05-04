let width = document.getElementById("layer1").width;
let height = document.getElementById("layer1").height;
const title = document.getElementById("title")
const ctx = document.getElementById("layer1").getContext("2d");
const cnv = document.getElementById("layer1");

let halt = document.getElementById('halt-simulation')
let running = true
let predList = []
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
        this.energy = 10
    }
}

const testGrass = new Grass()

class Animal {
    constructor(){
        this.age = 0
        this.energy = 20
        const sexList = ["female", "male"]
        this.sex = sexList[Math.round(Math.random())]
        this.pregnant = false
        this.x = Math.round(Math.random()*width)
        this.y = Math.round(Math.random()*height)
        this.awareness = 30
        this.speed = 3
        this.size = 16
        this.x_move = Math.round(Math.random()*this.speed)
        this.y_move = Math.round(Math.random()*this.speed)
        this.gestation = 3000
        this.maxLitterSize = 1
        this.counter = 0
        this.metabolism = this.speed/6 + this.awareness/60
        this.greed = 50
        this.libido = 35
        
        this.getOlder()
        this.getHungry()
    }
    getOlder() {setInterval(()=>{
        this.age+=1
        
    },12000)
    }
    getHungry() { setInterval( ()=> {
        this.energy -= this.metabolism
    },100)
    }

    checkProximity(target) {
        let distance_x = Math.abs(this.x-target.x)
        let distance_y = Math.abs(this.y-target.y)
        let distance = Math.sqrt(distance_x*distance_x+distance_y*distance_y)
        return distance
    }
    checkAdjacent(target) {
        let distance = this.checkProximity(target)
        if (distance < this.size) {
            return true
        }
    }
    
    
    eat(target_array){
        
        target_array.forEach((target,i) => {
            
            let proximity = this.checkProximity(target)
            let edible = this.checkAdjacent(target)
            if (edible === true) {
                this.energy += target.energy
                
                target_array.splice(i,1)
                
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
    moveAway(target) {
        if (this.x >=  target.x) {
            this.x_move = this.speed
        }
        else if (this.x <= target.x) {
            this.x_move = -1 * this.speed
        }
        if (this.y >= target.y) {
            this.y_move = this.speed
        }
        else if (this.y <= target.y) {
            this.y_move = -1 * this.speed
        }
    }
    
    mate = (speciesList) => {
        
        if (this.sex === "female" && this.pregnant === false && this.age >= 1)  {
            speciesList.forEach((boy,i) => {
                if (boy.sex === "male") {
                    let mateable = this.checkProximity(boy)
                    if (mateable < this.awareness) {
                        this.pregnant = true
                        setTimeout(this.giveBirth,3000)
                        
                        
                    }
                }
            })
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
    giveBirth() {
            
            let child = new Prey()
            child.x = this.x
            child.y = this.y
            preyList.push(child)
            this.pregnant = false
            
        
    }
}

class Predator extends Animal {
    constructor(){
        super()
        this.gestation = 6000
        let predImage = document.createElement('img')
        predImage.src = "fox.png"
        this.img = predImage
    }
}

function startup() {
    for (i=0; i<10; i++) {
        let prey = new Prey()
        
        preyList.push(prey)
    }
    for (i=0; i<0; i++) {
        let pred = new Predator()
        predList.push(pred)
    }
    //Maintenance function to check data yearly
    setInterval( function() {
        console.log(preyList)
    },12000)
    
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
            predList.forEach((pred, i) => {
                let danger = prey.checkProximity(pred)
                if (danger < prey.awareness) {
                    prey.moveAway(pred)
                }
            })
            if (prey.energy < prey.greed) {
                prey.eat(grassList)
            }
            if (prey.sex === 'female' && prey.age >= 1 && prey.pregnant === false) {
                preyList.forEach((boy,i) => {
                    let mateable = prey.checkProximity(boy)
                    if (mateable <= prey.awareness && prey.pregnant === false) { 
                        prey.pregnant = true
                        //Causes the prey to give birth after 3 seconds
                        setTimeout(() => {
                            
                            for (let i=0;i<prey.maxLitterSize;i++) {
                                let child = new Prey()
                                child.x = prey.x
                                child.y = prey.y
                                preyList.push(child)
                                
                            }
                            prey.pregnant = false
                            
                        },3000)
                    }
                })
            }

            prey.move()

            //Kills prey who have no energy--they starve
            if (prey.energy <= 0) {
                preyList.splice(i,1)
            }
            
            ctx.drawImage(prey.img,prey.x,prey.y)
        })

        predList.forEach(function(pred) {
            pred.eat(preyList)
            pred.move()
            ctx.drawImage(pred.img,pred.x,pred.y)
        })

           

        window.requestAnimationFrame(main_loop)
    }
}

startup()
window.requestAnimationFrame(main_loop);

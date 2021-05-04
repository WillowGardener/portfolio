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
        this.maxAge = 8
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
        this.metabolism = this.speed/8 + this.awareness/80
        this.greed = 50 + Math.random() *50
        this.libido = 35
        this.parentalInvestment = Math.random()/2
        
        this.getOlder()
        this.getHungry()
    }
    getOlder() {setInterval(()=>{
        this.age+=1
        if (this.age >= this.maxAge) {
            this.speed = 0
            this.awareness = 0
            this.metabolism = 0
            this.sex = "corpse"
        }
        
    },12000)
    }
    getHungry() { setInterval( ()=> {
        this.energy -= this.metabolism
    },200)
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
    
    
    
    
}

class Prey extends Animal {
    constructor(){
        super()
        let preyImage = document.createElement('img')
        preyImage.src = "rabbit.png"
        this.img = preyImage
    }
    mate = (thisList) => {
        
        if (this.sex === 'female' && this.age >= 1 && this.pregnant === false && this.energy >= this.libido) {
            thisList.forEach((boy,i) => {
                let mateable = this.checkProximity(boy)
                if (mateable <= this.awareness && this.pregnant === false && boy.energy >= boy.libido) { 
                    this.pregnant = true
                    boy.energy -= boy.energy * boy.parentalInvestment
                    //Causes the prey to give birth after 3 seconds
                    setTimeout(() => {
                        let childSupport = this.parentalInvestment * this.energy
                        this.energy -= childSupport
                        let litterSize = Math.round(Math.random()*this.maxLitterSize)
                        for (let i=0;i<litterSize;i++) {
                            let child = new Prey()
                            child.energy = childSupport/litterSize
                            child.x = this.x
                            child.y = this.y
                            thisList.push(child)
                            
                        }
                        this.pregnant = false
                        
                    },3000)
                }
            })
        }
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
    mate = (thisList) => {
        
        if (this.sex === 'female' && this.age >= 1 && this.pregnant === false) {
            thisList.forEach((boy,i) => {
                let mateable = this.checkProximity(boy)
                if (mateable <= this.awareness && this.pregnant === false) { 
                    this.pregnant = true
                    //Causes the prey to give birth after 3 seconds
                    setTimeout(() => {
                        
                        for (let i=0;i<this.maxLitterSize;i++) {
                            let child = new Predator()
                            child.x = this.x
                            child.y = this.y
                            thisList.push(child)
                            
                        }
                        this.pregnant = false
                        
                    },3000)
                }
            })
        }
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

            prey.mate(preyList)
            // if (prey.sex === 'female' && prey.age >= 1 && prey.pregnant === false) {
            //     preyList.forEach((boy,i) => {
            //         let mateable = prey.checkProximity(boy)
            //         if (mateable <= prey.awareness && prey.pregnant === false) { 
            //             prey.pregnant = true
            //             //Causes the prey to give birth after 3 seconds
            //             setTimeout(() => {
                            
            //                 for (let i=0;i<prey.maxLitterSize;i++) {
            //                     let child = new Prey()
            //                     child.x = prey.x
            //                     child.y = prey.y
            //                     preyList.push(child)
                                
            //                 }
            //                 prey.pregnant = false
                            
            //             },3000)
            //         }
            //     })
            // }

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

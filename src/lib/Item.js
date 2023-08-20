class Item{
  constructor(name, price, people=[]){
    this.name = name
    this.price = price
    this.people = people
  }

  toString(){
    return `${this.name} ${this.price}`;
  }
}

export {Item}
class Person{
	constructor(name, items=[]) {
		this.name = name;
		this.items = items
	}

	toString(){
		return this.name;
	}
}

export {Person}
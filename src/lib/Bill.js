class Bill{
	constructor(people=[], items=[], tip = 0, tax = 0) {
		this.people = people;
		this.items = items;
		this.tip = tip;
		this.tax = tax;
	}

	add_person(person) {
		this.people.push(person);
	}
	
	add_item(item){
		this.items.push(item);
	}
}

export {Bill}
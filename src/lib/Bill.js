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

	// Calculate cost for every person
	// Person as the key, Payment as the value
	calculate() {
		const results = {};
		for (let i = 0; i < this.people.length; i++){
			let total = 0;
			const person = this.people[i];
			for (let j = 0; j < person.items.length; j ++){
				const item = person.items[j];
				total += item.price/item.people.length;
			}
			results[person] = total * (1 + this.tip + this.tax);
		}
		return results;
	}
}

export {Bill}
class Bill{
    constructor(people = []){
        this.people = people;
    }

	add_person(person) {
        this.people.push(person);
    }
}

export {Bill}
import { Bill } from "./Bill";
import { Person } from "./Person";
var bill = new Bill();

function add_person() {
    let personName = document.getElementById("personName").value;
    let person = new Person(personName); 
    bill.add_person(person);
    console.log(bill)
}


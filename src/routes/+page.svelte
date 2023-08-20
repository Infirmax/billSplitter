
<script>
	import {Bill} from "$lib/Bill.js";
	import {Person} from "$lib/Person.js";
  import {Item} from "$lib/Item.js";

	let bill = new Bill();

	let people = [];
  function request_person(){
		const name = prompt("Please enter the name");
		bill.add_person(new Person(name));
		people = bill.people
  }

	let items = [];
	function request_item(){
		const name = prompt("Please enter the item name");
		const price = prompt("Please enter the item price");
    bill.add_item(new Item(name, price));
		items = bill.items;
	}
	
	function split(event){
		const element = event.srcElement;
		const person = people[element.getAttribute("data-person")];
		const item = items[element.getAttribute("data-item")];
		const count = element.getAttribute("data-counter")

		// If this is a press
		if(count%2 == 0){
			element.style.backgroundColor = "#4CAF50";
			person.items.push(item);
			item.people.push(person);
		}
		// If this is an unpress
		else{
			element.style.backgroundColor = "#FFFFFF";
			person.items.splice(element.getAttribute("data-person"), 1);
			item.people.splice(element.getAttribute("data-item"), 1);
		}

		element.setAttribute("data-counter", parseInt(count) + 1);
	}

	let results = Object.entries({});
	function calculate(){
		results = Object.entries(bill.calculate());
	}
</script>

<h1>Welcome to bill splitter!</h1>

<div class="horizontal">
	<h3>Tip</h3>
	<input bind:value={bill.tip} type="number" step="0.01"/>
</div>


<div class="horizontal">
	<h3>Tax</h3>
	<input bind:value={bill.tax} type="number" step="0.01"/>
</div>


<div class="horizontal">
	<h1>Table</h1>
	<button on:click={request_person}>+</button>
</div>
{#each people as person, index}
    <p>Person {index + 1}: {person}</p>
{/each}

<div class="horizontal">
	<h1>Menu Items</h1>
	<button on:click={request_item}>+</button>
</div>
{#each items as item, itemIndex}
	<p>Item #{itemIndex + 1}: {item.name} ${item.price}</p>
	{#each people as person, personIndex}
		<button data-counter=0 data-person={personIndex} data-item={itemIndex} on:click={split}>{person}</button>
	{/each}
{/each}

<br><button on:click={calculate}>Calculate</button>
{#each results as [key, value]}
	<p>Person {key} = {value}</p>
{/each}

<style>
	.horizontal{
		display: flex;
	}
</style>
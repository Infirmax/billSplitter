
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
	
	function split(){
		console.log(document.getElementById("personButton"))
		document.getElementById("personButton").className = 'highlighted'
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
{#each items as item, index}
	<p>Item #{index + 1}: {item.name} ${item.price}</p>
	{#each people as person}
		<button id="personButton" on:click={split}>{person}</button>
	{/each}
{/each}


<style>
	.horizontal{
		display: flex;
	}
	
	.highlighted{
		background-color: #4CAF50;
	}
</style>
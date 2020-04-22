<script>

	import { onMount } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js';

	/*
	let car = [
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-1.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-2.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-3.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-4.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-5.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
		{
			title: 'Cheverolet SUV Car',
			img: 'images/car-6.jpg',
			currency: '$',
			time_price: '10.99',
			when_time: '/per hour',
			fuel: '$3/hour fuel surcharges',
			day_price: '60.99',
			when_day: '/per day',
			month_price: '995.99',
			when_month: '/per month'
		},
	];*/

	let car = [];

	const CSRF_TOKEN = Cookies.get('csrftoken');
	const PRICE_URL = getRef("price-ref");

	function getRef(id) {return document.getElementById(id).href;};

	onMount(async () => {
        const response = await fetch(PRICE_URL, {
                                      headers: {
                                        'Accept': 'application/json, text-plain, */*',
                                        'X-Requested-With': 'XMLHttpRequest',
                                      }
        });
        let car_json = await response.json();
        car = car_json['car'];
        car = car;
        console.log(car);    
    });
	
</script>

<main>

	<table class="table">
		<thead class="thead-primary">
			<tr class="text-center">
			<th>&nbsp;</th>
			<th>&nbsp;</th>
			<th class="bg-primary heading">Per Hour Rate</th>
			<th class="bg-dark heading">Per Day Rate</th>
			<th class="bg-black heading">Leasing</th>
			</tr>
		</thead>
		<tbody>

			{#each car as item}
			<tr class="">
			<td class="car-image"><div class="img" style="background-image:{'url(/static/auto/' + item.img + ')'};"></div></td>
			<td class="product-name">
				<h3>{item.title}</h3>
				<p class="mb-0 rated">
					<span>rated:</span>
					<span class="ion-ios-star"></span>
					<span class="ion-ios-star"></span>
					<span class="ion-ios-star"></span>
					<span class="ion-ios-star"></span>
					<span class="ion-ios-star"></span>
				</p>
			</td>
			
			<td class="price">
				<p class="btn-custom"><a href=".">Rent a car</a></p>
				<div class="price-rate">
					<h3>
						<span class="num"><small class="currency">{item.currency}</small> {item.time_price}</span>
						<span class="per">{item.when_time}</span>
					</h3>
					<span class="subheading">{item.fuel}</span>
				</div>
			</td>
			
			<td class="price">
				<p class="btn-custom"><a href=".">Rent a car</a></p>
				<div class="price-rate">
					<h3>
						<span class="num"><small class="currency">{item.currency}</small> {item.day_price}</span>
						<span class="per">{item.when_day}</span>
					</h3>
					<span class="subheading">{item.fuel}</span>
			</div>
			</td>

			<td class="price">
				<p class="btn-custom"><a href=".">Rent a car</a></p>
				<div class="price-rate">
					<h3>
						<span class="num"><small class="currency">{item.currency}</small> {item.month_price}</span>
						<span class="per">{item.when_month}</span>
					</h3>
					<span class="subheading">{item.fuel}</span>
				</div>
			</td>
			</tr><!-- END TR-->
			{/each}
	
</main>

<style>
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

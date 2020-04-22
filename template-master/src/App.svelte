<script>

	import { onMount } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js';

	/*
	let car = [
		{
			title: 'Mercedez-Benz C217',
			company: 'Mercedez-Benz',
			img: 'images/car-1.jpg',
			price: 10.99,
			when_day: '/day'			
		},
		{
			title: 'Range Rover Evoque',
			company: 'Land Rover',
			img: 'images/car-2.jpg',
			price: 20.25,
			when_day: '/day'			
		},
		{
			title: 'Audi RS6',
			company: 'Audi',
			img: 'images/car-3.jpg',
			price: 15.30,
			when_day: '/day'			
		},
		{
			title: 'Ford Mustang',
			company: 'Ford',
			img: 'images/car-4.jpg',
			price: 25.50,
			when_day: '/day'			
		},
		{
			title: 'BMW F22',
			company: 'BMW',
			img: 'images/car-5.jpg',
			price: 17.60,
			when_day: '/day'			
		},
		{
			title: 'Alfa Romeo 4C',
			company: 'Alfa Romeo',
			img: 'images/car-6.jpg',
			price: 14.30,
			when_day: '/day'			
		},
		{
			title: 'Mercedez-Benz A217',
			company: 'Mercedez-Benz',
			img: 'images/car-7.jpg',
			price: 16.30,
			when_day: '/day'			
		},
		{
			title: 'Jeep Wrangler',
			company: 'Jeep',
			img: 'images/car-8.jpg',
			price: 19.50,
			when_day: '/day'			
		},
	];*/

	let mash = [];

	const CSRF_TOKEN = Cookies.get('csrftoken');
	const INDEX_URL = getRef("index-ref");

	function getRef(id) {return document.getElementById(id).href;};


	onMount(async () => {
        const response = await fetch(INDEX_URL, {
                                      headers: {
                                        'Accept': 'application/json, text-plain, */*',
                                        'X-Requested-With': 'XMLHttpRequest',
                                      }
        });
        let mash_json = await response.json();
        mash = mash_json['mash'];
        mash = mash;
        console.log(mash);    
    });
	
</script>

<main>

				{#each mash as item}
    			<div class="col-md-3">
    				<div class="car-wrap ftco-animate">
    					<div class="img d-flex align-items-end" style="background-image: {'url(/static/auto/' + item.img + ')'};">
    						<div class="price-wrap d-flex">
    							<span class="rate">{item.price}</span>
    							<p class="from-day">
    								<span>From</span>
    								<span>{item.when_day}</span>
    							</p>
    						</div>
    					</div>
    					<div class="text p-4 text-center">
    						<h2 class="mb-0"><a href=".">{item.title}</a></h2>
    						<span>{item.company}</span>
    						<p class="d-flex mb-0 d-block"><a href="." class="btn btn-black btn-outline-black mr-1">Book now</a> <a href="." class="btn btn-black btn-outline-black ml-1">Details</a></p>
    					</div>
    				</div>
    			</div>
				{/each}
		
</main>

<style>
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

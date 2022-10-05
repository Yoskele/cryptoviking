



// Update the price every minute.
var intervalId = window.setInterval(function(){
  	getHistoricalPrice();
}, 60 * 1000);



const getHistoricalPrice = async event => {
	let string = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cripple%2Ccardano%2Cpolkadot%2Cthe-sandbox%2Csolana%2Cdogecoin&vs_currencies=usd";
	await fetch(string)
	.then(res => res.json())
	.then((data) => {
		for (const [key, value] of Object.entries(data)) {
		  // Grab the price container 
		  try{
		  	document.querySelector(`#${key}-price-container`).innerText = `$${value.usd.toFixed(2)}`;
		  	// console.log('Done...')
		  }catch(err){
		  	// console.log(err, "error")
		  }
		}
	});
}

// Get the price when user enter the page.
getHistoricalPrice();




























// const getHistoricalPrice = async event => {
// 	let string = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Ccardano%2Cripple%2Cpolkadot&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false";
// 	await fetch(string)
// 	.then(res => res.json())
// 	.then((data) => {

// 		for (const [key, value] of Object.entries(data)) {
// 		  console.log(key, value);
// 		  // Grab the price container 
// 		  let priceContainer = document.querySelector(`#${key}-price-container`).innerText = `$${value.usd}`;
// 		  console.log('Done...')
// 		}



// 	});



// }


// getHistoricalPrice();


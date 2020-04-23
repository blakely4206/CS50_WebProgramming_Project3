
function toppings_button_onClick() {
	let modal = document.getElementById("modal_toppings");
	if(modal.style.display == "block"){
		modal.style.display = "none";
	}
	else{
		modal.style.display = "block";
	}
}

function close_onClick() {
	let modal = document.getElementById("modal_toppings");
	modal.style.display = "none";
}

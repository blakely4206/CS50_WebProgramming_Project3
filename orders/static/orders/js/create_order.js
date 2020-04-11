function checkbox_oncheck(){
	var topping_checkboxes = document.getElementsByClassName("topping_box");
	var t_count = document.getElementById("toppings_type_dropdown").value;
	var t_total = 0;				
				
	for(i = 0; i < topping_checkboxes.length; i++){					
		if(topping_checkboxes[i].checked == true){
			t_total++;						
		}
	}	
				
	if(t_total == t_count){
		for(i = 0; i < topping_checkboxes.length; i++){				
			if(topping_checkboxes[i].checked == false){
				topping_checkboxes[i].disabled = true;					
			}
		}	
	}
	else if(t_total < t_count){
		for(i = 0; i < topping_checkboxes.length; i++){	
			topping_checkboxes[i].disabled = false;											
		}	
	}
}
			
function toppings_type_dropdown_handler(){
				
	var t_count = document.getElementById("toppings_type_dropdown").value;
				
	if(t_count == 0){
		document.getElementById("div_toppings").style.display = "none";
	}
	else{
		document.getElementById("div_toppings").style.display = "block";
	}
				
	var topping_checkboxes = document.getElementsByClassName("topping_box");
	for(i = 0; i < topping_checkboxes.length; i++){
		topping_checkboxes[i].checked = false;
		if(t_count == 0){
			topping_checkboxes[i].disabled = true;
		}
		else{
			topping_checkboxes[i].disabled = false;
		}
	}
}				

function quantiy_onchange(){
	let quant = document.getElementById("quantity").value;
	let submit = document.getElementById("order");
	
	if(quant.value === ""){
		submit.disabled = true;
	}
	else{
		submit.disabled = false;
	}
}
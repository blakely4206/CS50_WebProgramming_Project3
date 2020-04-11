function checkbox_oncheck(){
			
	let quant = document.getElementsByName("quantity");
	let lineitems = document.getElementsByName("lineitems");
				
	for(var i = 0; i < quant.length; i++){
		if(lineitems[i].checked == false){
			quant[i].value = "0";
		}
	}	
}
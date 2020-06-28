// getting elements 


// getting manual btn
let manualBtn = document.getElementById('Manual')
// getting balance btn
let checkBtn = document.getElementById('check')
//getting leave btn
let leave = document.getElementById('close')
// getting modals
let manual = document.getElementById('manual-modal')
let balance = document.getElementById('model-balance')


//actual work
//show manual modal
manualBtn.onclick = function(){
    manual.style.display="block"
}
//show balance 
checkBtn.onclick = function(){
    balance.style.display="block"
}

// leave balance 
leave.onclick = function(){
    balance.style.display="none"
}
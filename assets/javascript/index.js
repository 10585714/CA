$(document).ready(function(){
    if(jQuery){
	alert("JQury is loaded");
    } else {

    alert("JQuery is not loaded");
}
});


// Get the modal
var modal = document.getElementById('signupform');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>
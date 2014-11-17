$(document).ready(function(){
	$(".animate").mouseenter(function() {
		$(this).animate({
    		margin: "1in",
		}, 1500);
	});
	$(".animate").mouseleave(function() {
		$(this).animate({
    		margin: "0in",
		}, 1500);
	});

	$("#senior").fadeIn(3000);
	setTimeout(function(){
		$(".guard").fadeIn(5000);
	},2000);
	/*$("#senior").draggable();*/
});
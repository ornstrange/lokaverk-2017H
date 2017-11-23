var srchClicked = false;
var menuClicked = false;

$('#menu-btn').click(function(){
	if (!menuClicked) {
		$("#menu-cont").addClass("menu-content-active");
		menuClicked = true;
	}
});

$('html').click(function() {
	if (menuClicked) {
		$("#menu-cont").removeClass("menu-content-active");
		menuClicked = false;
	}
});
$('#menu-btn').click(function(event){
	event.stopPropagation();
});
$('#menu-cont').click(function(event){
	event.stopPropagation();
});

$('#srch-btn').click(function(){
	if (!srchClicked) {
		srchClicked = true;
		$("#srch-inp").addClass("srch-inp-active");
		document.getElementById('srch-inp').focus();
	} else {
		srchClicked = false;
		var srchString = $("#srch-inp").val();
		if (srchString == "") {
			$("#srch-inp").removeClass("srch-inp-active");
		} else {
			window.location.href = "/search?s="+srchString;
		}
	}
});

$("[class*=iid-]").mouseover(
	function() {
		var c = this.className;
   		console.log(c);
	}
);

$("img.lazy").lazyload();
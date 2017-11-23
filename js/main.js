var srchClicked = false;
var menuClicked = false;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

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

$("[class*=iid-]").hover(function() {
	var icount = 0;
	var items = [];
	$("[class*=iid-]").each(function(j, obj) {
		icount = j;
		items.push(obj.className.substr(9));
	});
	var iid = this.className.substr(9);
	for (var i = 0; i < icount; i++) {
		if (items[i] != iid) {
			$(".iid-"+items[i]).addClass("blurred");
		}
	}
}, function() {
	sleep(1000);
	var icount = 0;
	var items = [];
	$("[class*=iid-]").each(function(j, obj) {
		icount = j;
		items.push(obj.className.substr(9).replace(" blurred", ""));
	});
	console.log(items)
	for (var i = 0; i < icount; i++) {
		$(".iid-"+items[i]).removeClass("blurred");
	}
});

$("img.lazy").lazyload();
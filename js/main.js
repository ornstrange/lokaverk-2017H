var srchClicked = false;
var menuClicked = false;
var userClicked = false;

// menu
$('#menu-btn').click(function(){
	if (!menuClicked) {
		$("#menu-cont").addClass("menu-content-active");
		menuClicked = true;
	} else {
		$("#menu-cont").removeClass("menu-content-active");
		menuClicked = false;
	}
});

// user
$('#user-btn').click(function(){
	if (!userClicked) {
		$("#user-cont").addClass("user-content-active");
		userClicked = true;
	} else {
		$("#user-cont").removeClass("user-content-active");
		userClicked = false;
	}
});

// ehv dot
$('html').click(function() {
	if (menuClicked) {
		$("#menu-cont").removeClass("menu-content-active");
		menuClicked = false;
	}
	if (userClicked) {
		$("#user-cont").removeClass("user-content-active");
		userClicked = false;
	}
});
$('#menu-btn').click(function(event){
	event.stopPropagation();
});
$('#menu-cont').click(function(event){
	event.stopPropagation();
});
$('#user-btn').click(function(event){
	event.stopPropagation();
});

// login
$('#login-btn').click(function(){
	$("#login-cont").addClass("login-active");
});
$('#login-btn2').click(function(){
	$("#login-cont").addClass("login-active");
});
$('#close-login').click(function(){
	$("#login-cont").removeClass("login-active");
});
// forgotup
$('#sign-btn').click(function(){
	$("#signup-cont").addClass("signup-active");
});
$('#close-signup').click(function(){
	$("#signup-cont").removeClass("signup-active");
});
// logout
$('#logout-btn').click(function(){
	window.location.href = "/logout";
	return false;
});
// cart
$('#cart-btn').click(function(){
	window.location.href = "/cart";
	return false;
});
// forgot
$('#forgot-btn').click(function(){
	$("#forgot-cont").addClass("forgot-cont-active");
	$("#login-cont").removeClass("login-active");
});
$('#close-forgot').click(function(){
	$("#forgot-cont").removeClass("forgot-cont-active");
});

// search
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
			window.location.href = "/search?s="+srchString+"&srt=mu";
		}
	}
});

// items hover
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
	var icount = 0;
	var items = [];
	$("[class*=iid-]").each(function(j, obj) {
		icount = j;
		items.push(obj.className.substr(9).replace(" blurred", ""));
	});
	for (var i = 0; i < icount; i++) {
		$(".iid-"+items[i]).removeClass("blurred");
	}
});

// lazy load
$("img.lazy").lazyload();

// fancybox
$.fancybox.defaults.toolbar = false;
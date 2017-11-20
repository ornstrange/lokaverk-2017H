<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>LATE</title>
	<link rel="stylesheet" href="css/normalize.css">
	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
	<link rel="stylesheet" href="css/main.css">
</head>
<body>
	% include("header.tpl")
	<section class="land-page">
		<ul class="land-list">
			<li class="dresses"><a href="/search?s=dress">dresses</a></li>
			<li class="jackets"><a href="/search?s=jacket">jackets</a></li>
			<li class="tops"><a href="/search?s=top">tops</a></li>
		</ul>
	</section>
	<script
	src="https://code.jquery.com/jquery-3.2.1.min.js"
	integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	crossorigin="anonymous"></script>
	<script>
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
	</script>
</body>
</html>
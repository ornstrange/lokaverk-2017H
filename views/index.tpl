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
	<div class="land-page">
		<ul class="land-list">
			<li class="dresses"><a href="/search?s=$dress">dresses</a></li>
			<li class="jackets"><a href="/search?s=$jacket">jackets</a></li>
			<li class="tops"><a href="/search?s=$top">tops</a></li>
		</ul>
	</div>

	<div class="about">
		<h1 class="title">
			ABOUT US
		</h1>
		<p class="text">
			LATE is a company founded in 2017 in Brussel, Belgium.
			It concentrates on selling customers high quality products for an affordable price.
			We are an international company which sells clothes all around the world.<br>
			For contact click <a href="#contact">here</a>
		</p>
	</div>
	<script
	src="https://code.jquery.com/jquery-3.2.1.min.js"
	integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	crossorigin="anonymous"></script>
	<script src="js/jquery.lazyload.js"></script>
	<script src="js/main.js"></script>
</body>
</html>
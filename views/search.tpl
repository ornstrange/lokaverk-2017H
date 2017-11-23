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
	%include("header.tpl")
	<section class="products">
		<div class="items-container">
		% for i in items:
			<a href="/item?id={{all[i-1]["iid"]}}" class="item iid-{{all[i-1]["iid"]}}">
				<img class="lazy" src="img/temp.gif" data-original="img/items/item-{{all[i-1]["iid"]}}.jpg">
				<p class="text">{{all[i-1]["iname"].upper()}}</p>
				<p class="price">{{all[i-1]["price"]}}&euro;</p>
			</a>
		% end
		</div>
	</section>
	<script
	src="https://code.jquery.com/jquery-3.2.1.min.js"
	integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	crossorigin="anonymous"></script>
	<script src="js/jquery.lazyload.js"></script>
	<script src="js/main.js"></script>
</body>
</html>
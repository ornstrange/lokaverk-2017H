<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>LATE - {{item["iname"]}}</title>
	<link rel="stylesheet" href="css/normalize.css">
	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
	<link rel="stylesheet" href="css/main.css">
	<link rel="stylesheet" href="css/jquery.fancybox.css" type="text/css" media="screen"/>
</head>
<body>
	%include("header.tpl")
	
	<div class="single-item">
		<a data-fancybox class="img-link" href="img/items/item-{{item["iid"]}}.jpg">
			<img id="item-img" class="pic lazy" src="img/temp.gif" data-original="img/items/item-{{item["iid"]}}.jpg">
		</a>

		<div class="text">
				<h1 class="title">
					{{item["iname"]}}
				</h1>

				<p class="info">
					{{item["price"]}}&euro; &nbsp;- &nbsp;{{item["amount"]}} left
				</p>
		</div>

		<div class="color" style="background:{{item["color"]}} !important;"><span class="txt">COLOR</span></div>

		<form class="buy-btn" action="/add-cart" method="POST">
			<button class="btn" name="btn" value="{{item["iid"]}}">ADD TO CART</button>
		</form>
	</div>
	
	% include("footer.tpl")
	<script
	src="https://code.jquery.com/jquery-3.2.1.min.js"
	integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
	crossorigin="anonymous"></script>
	<script type="text/javascript" src="js/jquery.fancybox.js"></script>
	<script src="js/jquery.lazyload.js"></script>
	<script src="js/main.js"></script>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>LATE - your cart</title>
	<link rel="stylesheet" href="css/normalize.css">
	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
	<link rel="stylesheet" href="css/main.css">
	<link rel="stylesheet" href="css/jquery.fancybox.css" type="text/css" media="screen"/>
</head>
<body>
	%include("header.tpl")
	
	<div class="cart-container">	
		%if len(cart) > 0:
			<div class="cart">
				<h1 class="title">YOUR CART</h1>
				%for i in cart:
					%for j in items:
						%if i["iid"] == j["iid"]:
							<div class="item">{{j["iname"]}} - {{j["price"]}}&euro;
								<form class="del-form" action="/del-cart" method="POST">
									<button name="btn" class="del-btn" value="{{i["iid"]}}">
										<i class="fa fa-minus-circle" aria-hidden="true"></i>
									</button>
								</form>
							</div>
						%end
					%end
				%end
				<p class="total">total: {{total}}&euro;</p>
			</div>
		%else:
			<p class="no-items">
				You have no items in your cart...<br>
				<span><button id="login-btn2">login</button> and / or <a href="/search?s=$jacket">buy something!</a></span>
			</p>
		%end
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
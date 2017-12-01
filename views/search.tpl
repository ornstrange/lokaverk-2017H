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
	<style>
		% if len(items) % 3 == 0:
			.products .items-container{grid-template-columns: 1fr 1fr 1fr !important;
																 grid-gap: 80px !important;}
		% end
		% if len(items) % 5 == 0:
			.products .items-container{grid-template-columns: 1fr 1fr 1fr 1fr 1fr !important;
																 grid-gap: 16px !important;
																 width: calc(80vw - 1px);}
		% end
		% if len(items) % 4 == 0:
			.products .items-container{grid-template-columns: 1fr 1fr 1fr 1fr !important;
																 grid-gap: 16px !important;
																 width: 80vw;}
		% end
		{}
	</style>
</head>
<body>
	%include("header.tpl")
	
	<section class="products">
		<div class="sorter">
			<a href="/search?s={{srch}}&srt=mu">LOW - HIGH</a>
			<a href="/search?s={{srch}}&srt=md">HIGH - LOW</a>
			<a href="/search?s={{srch}}&srt=co">COLOR</a>
		</div>

		%if sort == "mu": all = sorted(all, key=lambda x: x["price"])
		%end
		%if sort == "md": all = sorted(all, key=lambda x: x["price"], reverse=True)
		%end
		%if sort == "co": all = sorted(all, key=lambda x: x["color"])
		%end

		<div class="items-container">
		% for i in all:
			% if i["iid"] in items:
			<a href="/item?id={{i["iid"]}}" class="item iid-{{i["iid"]}}">
				<img class="lazy" src="img/temp.gif" data-original="img/items/item-{{i["iid"]}}.jpg">
				<p class="text">{{i["iname"].upper()}}</p>
				<p class="price">{{i["price"]}}&euro;</p>
			</a>
			% end
		% end
		</div>
	</section>

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
<header>
	<div class="items">
		<button class="menu"><i class="fa fa-bars" aria-hidden="true" id="menu-btn"></i></button>
		<div class="menu-content" id="menu-cont">
			<ul>
				<li class="item"><a href="/">home</a></li>
				<li class="item"><a href="/search?s=$new">new arrivals</a></li>
				<li class="item"><a href="/search?s=$dress">dresses</a></li>
				<li class="item"><a href="/search?s=$jacket">jackets</a></li>
				<li class="item"><a href="/search?s=$top">tops</a></li>
				<li class="item filler"></li>
				<li class="item lower"><a href="#about">about</a></li>
				<li class="item bottom"><a href="#contact">contact</a></li>
			</ul>
		</div>
		<h1 class="title">LATE</h1>
		
		<form action="/search">
			<input type="text" class="srch-inp" id="srch-inp" name="s" placeholder="search">
		</form>
		<button class="search"><i class="fa fa-search" aria-hidden="true" id="srch-btn"></i></button>
	</div>

	<div class="user-items">
		<button class="user"><i class="fa fa-user" aria-hidden="true" id="user-btn"></i></button>
		<div class="user-content" id="user-cont">
			<ul>
				<li class="item"><button id="login-btn">sign in</button></li>
				<li class="item"><button id="sign-btn">sign up</button></li>
				<li class="item"><button id="logout-btn">sign out</button></li>
				<li class="filler"></li>
				<li class="item"><button id="cart-btn">cart</button></li>
			</ul>
		</div>
	</div>

	<div class="login" id="login-cont">
		<a class="close" href="/">X</a>
		<form action="/login" method="POST">
			<input type="text" name="username" placeholder="username">
			<input type="password" name="password" placeholder="password">
			<button type="submit">LOGIN</button>
		</form>
	</div>
</header>
<script src="js/main.js"></script>
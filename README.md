# lokaverk-2017H
LATE tísku-fataverslun er lokaverkefni okkar í forritun, gagnasafnsfræði og vefsíðuhönnun.

Við ákváðum að gera tísku-fataverslun því okkur fannst það nota tiltölulega jafna hluta
af forritun, vefhönnun og gagnasafnsfræði. Við vorum ekki lengi að byrja og komast á ágætt ról, 
Örn Óli sá um heildarútlit síðunnar og Elmar sá um mikið af bakenda dótinu, þó svo að við gerðum báðir
sittlítið af hvoru. Ekki láta commitin plata ykkur, við unnum þetta mikið saman og ákváðum að ýta bara úr
mínum reikning til að einfalda hlutina.

Elmar og Örn.

---
## GSF
töflur: vörutafla, usertafla, starfsmannatafla?, lager?

items: iid, iname, kind, color, size, count, date?, price, uppl um mynd
users: uid, username, email, password(encryptað?), adminFlag
veit ekki með -> employees: eid, ename, hiredate, salary...
stock: totalWorth?, eða ehv þannig

trigger þegar vara selst að reikna lagerinn okkar uppá
nýtt, og þegar starfsmaður er rekinn og blabla

---
## VEFSÍÐAN
Menu takki -- Nafn á vefsíðu -- Leita takki
menu: login?, nýtt, á útsölu, konur, karlar, flokkar
flokkar: toppar, peysur, kjólar blabla

á land-page er linkur á aðal flokkana.

HEADER
LAND PAGE
EHV UPPLÝSINGAR UM SÍÐUNA
SKRÁ Á PÓSTLISTA
FOOTER

getum náð í föt af síðum eins og misguided og ehv
fleiri, spurjum stelpur um ehv síður.

---
## BOTTLE
bottle sér bara um allt routing, hún verður mjög dynamic
þá höfum við bara nokkur template eins og index, search
og item síðu, líka kannski síðu fyrir flokka, en held
það slyppi bara að flokka síðan væri bara search nema
þá searcharu bara eftir flokk... ef þú skilur

item síða væri t.d -> sida.is/item/200, sem notar þá
iid úr items töflunni...

search væri bara síða sem tekur inn lista af hlutum og
byggir síður úr því eins og tónleika verkefnið...

index er bara basic front-page með linka í allt.

gæti hugsað mér að búa til header.tpl og footer.tpl
og includa þá alltaf bara í öllum hinum, þá er þetta
meira modular og þæginlega kannski...

þurfum líka að pæla í að hreinsa strengi fyrir user login
og allt sem hægt er að slá inn svo við séum ekki veikir
fyrir sql injection og slíkt. (skiptir samt engu máli)

---
## FORRITUN
ætla reyna búa til mjög góða og öflugan sql skipana
generator með föllum og klösum, sem tekur inn parametra
og spítir út skipunum sem tala virka allar og tala við
gagnagrunninn.

---
## GAGNAGRUNNS HÖNNUN HÉR
items, users, stock

items: 	iid: int primary-key not null,
	iname: varchar(32) not null,
	kind: varchar(16),
	color: varchar(10),
	count: int,
	size: float,
	price: int,
	arrivalDate: date,
	image: varchar(32)

users:	uid: int primary-key not null,
	username: varchar(16),
	passwd: varchar(16),
	email: varchar(24),
	isAdmin: bool,
	fname: varchar,
	lname: varchar

stock:	totalPrice: int,
	amountOfItems: int

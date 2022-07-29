# Harta šifrovačka

# Myšlenka

+ týmy dostanou šifrovací pomůcky a mapu okolí a 1. šifru
+ na mapě budou označeny stanoviště s pomocí N čísel (N > |velikost abecedy|), N idealne prvocislo
+ po vyluštění šifry vyjde nějaké slovo
+ poté udělají výpočet $(\sum_{i=0}^{|delka\_slova|} (ASCII(slovo[i]) - 97)) \mod{N}$
+ ASCII je funkce přiřazující písmenům hodnotu podle pořadí v abecedě (ASCII('a') = 97, ASCII('b') = 97,...)
+ ASCII(' ') = 96
+ celkem 31 stanivišť (0 - 30, dělí 31)
+ z toho jim vypadne číslo stanoviště, na které mají jít dál
+ na dalším stanovišti najdou šifru a postup opakují, dokud nenarazí na šifru s nadpisem FINAL

# FINAL šifra

+ chtělo by to něco fakt dobrýho (ale zase rozumně lehké, cíl je dostat je všechny na ToiToi)
+ musí jim vyjít něco ve stylu "Dostaňte celý tým najednou na TOITOI"
+ případně nějaká hádanka, ze které tohle mohou vymyslet?

# Co možná udělat

+ každý tým by mohl mít vlastní trasu, ať si nelezou za zadkem
    + můžeme prostě jenom přečíslovat mapy a nevymýšlet šifry navíc
+ pro splnění finálního úkolu nás musí najít a splnit ho před námi
+ šifry rozvěšovat viditelně, nedávat je vysoko na stromy atp.

# Hodnocení

TODO

# Legenda

Při stoupání narazili na skupiny Tibetských mnichů, kteří je nechtějí pustit dál dokud neuctí jejich božstvo. 
Jazyk ale neumí natolik, aby rozumněli, co přesně po nich mnichové chtějí a musí to zjistit -> rozšifrovat.

(Nebo jiná kravina, zatím nemám lepší nápad)

# TODO

1. zjistit pocet tymu [4]
2. mapa [?]
3. cesty pro tymy po mape
4. šifry (asi největší TODO)
    + rozebrat M&M wiki -> občas tam jsou popsané šifry (Matfyzák WARNING) [done]
    + Vojta má vyfocené nějaké šifry z šifrovaček (Matfyzák WARNING)
    
---
# Šifry

## arabská -> římská -> hodnota_čísla -> písmeno

Jde o čísla zapsaná pomocí římských číslic pomocí arabských číslic.

101051 -> XXVI -> 26 -> Z

[Tohle mi přijde OK na finální šifru (málo práce s převodem na dlouhý text)]

Výsledek:

- [x] mam skript, co to umi generovat

## Recepty - 1 divný odebrat

už jsem to dělal a podělal, pokus č.2 [Honza]

Výsledek: Edmund Hillary

Next: 22

- [x]

## strip fold

[nějaké puzzle](http://erikdemaine.org/fonts/), nvm které vybrat

[strip fold](http://erikdemaine.org/fonts/strip/)

Výsledek: vceli les 
 
Next: 25

- [x]

## Dlouhááááá šifra

Text, ve kterém se vyskytují slova krátký a dlouhý (morzeovka)

dlouhý - 
krátký .

Písmena oddělit odstavci

Výsledek: prehrada

Next: 9

- [x]

## Včelka

Včelka letí po květech. Pod každým květem je číslo, udávající vzdálenost, kterou včelka
uleťela, než se dostala na ten daný květ. Vzdálenost je mezi středy květu v mm.

Let včelky, pak udává pořadí písmen (musí být jednoznačný) v šifře.

Každý květ je pak semafor. (Okvětní lístky 2 barev)

Potřeba nějakého pravítka/něco co umí měřit vzdálenost

Výsledek: pod volarnou (Pod Volárnou, ta obora, co je u harty)

Next: 29

- [x]

## Lego

https://matfyzak.cz/wp/wp-content/uploads/2021/05/stavbyT.png

Docela dost jednoduchá

Výsledek: LETEC JI ULETEL

Next: 15

- [x]

## Porekadla

První písmeno pořekadla je vždy nějakým posledním písmenem jiného. (2 zůstanou volná)

Výsledek: mocnina

Next: 7

- [x]

# Šifrovací pomůcky

## potřeba
1. římská čísla
2. abeceda (číslování) + ' ' jako 0
3. semafor?
4. pravítko s mm

## něco, co nemusí použít 
1. braill


[Tyhle](https://chlyftym.cz/wp-content/uploads/pomucky_print_nano_1-1-4.pdf) mi přišly dobré (ale možná toho je moc)
ale nemají římské číslice
<h2 style="background-color: blue"># names_index_maker</h2>
This is a python3 script that look for a list of names inside a PDF and extracts number of the page where they appear.
It can be used to indicize books in pdf format, where the text is readable (no PDFs made with images only).
I made this little app to automatize a rather tedious task that I normally had to do manually for each book the company I work for publishes.
It works by passing arguments and, as for now, the only option is the page delta; in other words it will change the page's number according to the difference between the PDF file numbering and the actual one.
I hope it makes sense :)
Here I paste a sample output screen:

<pre style="background-color: black; color: grey;">
(base) barzi@B:~/PycharmProjects/indice_nomi$ python3 scratch.py AA9_fumagalli.pdf nomi.txt answer.txt 10 -d 1

Parsing: Boccali
	'Boccali' found in page 2
	'Boccali' found in page 5
	'Boccali' found in page 109
	'Boccali' found in page 199
	'Boccali' found in page 200
	'Boccali' found in page 202
	'Boccali' found in page 204
	'Boccali' found in page 205

...

Parsing: Dante
	'Dante' found in page 5
	'Dante' found in page 29
	'Dante' found in page 30
	'Dante' found in page 87
	'Dante' found in page 95
	'Dante' found in page 101
	'Dante' found in page 138
	'Dante' found in page 172
	'Dante' found in page 173
	'Dante' found in page 175
	'Dante' found in page 176
	'Dante' found in page 207
	'Dante' found in page 257
	'Dante' found in page 265
	'Dante' found in page 273
	'Dante' found in page 274
	'Dante' found in page 276
	'Dante' found in page 280
	'Dante' found in page 284
	'Dante' found in page 325
	'Dante' found in page 340
	'Dante' found in page 344
	'Dante' found in page 351
	'Dante' found in page 353
	'Dante' found in page 356
	'Dante' found in page 369
	'Dante' found in page 387
Parsing: 鷺山
	'鷺山' found in page 4
</pre>
This is how the output file looks like:
<pre style="background-color: black; color: grey;">
(base) barzi@B:~/PycharmProjects/indice_nomi$ cat answer.txt 
Alighieri 388n
Angelillo 3n, 4, 6, 208n, 264, 265n, 267n, 269n, 271n, 273n, 275n, 277n, 279n, 281n, 283n, 285n, 310n, 380, 386n
Aurora 209n, 210n, 211, 212n, 213, 217n, 219n, 220n, 221n, 222n, 224n, 227n, 230 e n
Bellingeri 6, 170, 171, 173, 175, 177, 388n
Boccali 3n, 6, 110n, 200, 201n, 203n, 205n, 206n, 207n, 208n, 232n, 241n, 244n, 378, 380n, 382n, 388n
Brereton 212n, 213n, 214n, 216n, 217n, 221n, 222n, 231n
Dante 6, 30n, 31n, 88, 96n, 102n, 139n, 173n, 174n, 176n, 177n, 208n, 258n, 266n, 274n, 275n, 277n, 281n, 285n, 326n, 341n, 345n, 352n, 354n, 357n, 370n, 388n
Maggi 6, 39n, 41n, 86n, 91n, 102n, 106n, 110n, 114n, 115n, 119n, 129n, 162n, 203n, 208, 209n, 211n, 213n, 215n, 217n, 219n, 221n, 223n, 225n, 227n, 229n, 231n, 237n, 246n, 249n, 250n, 261n, 272n, 276n, 289n, 296n, 298n, 302n, 304n, 305n, 306n, 311n, 314n, 317n, 318n, 320n, 324n, 328n, 329n, 331n, 338n, 339n, 346n, 347n, 349n, 351n, 355n, 369n, 379, 381n, 392n
Motoaki 57n, 58n, 74n
Oldenberg 208n, 211n, 212n, 215n, 220n, 223n
Raynaud 5, 10n, 12n, 15n, 134, 135n, 137n, 139n, 141n, 143n, 393n
Renou 112n, 210n, 211n, 213n, 214n, 215n, 216n, 217n, 219n, 220n, 224n, 226n, 231n
鷺山 5
</pre>

Legend: n stands for note, and "e n" means that the name can be found both in the page and in the footnote.

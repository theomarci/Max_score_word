<img src=".\src\Votre texte de paragraphe.png">
<hr>
<div>
  <blockquote align="center">
    <b><i>Delenda Carthago Est</i></b>
    <p><b>Marcus Porcus Cato</b> known as <b>Cato the elder</b></p>
  </blockquote>
</div>
<hr>
<div>
  <h2 align="center">Introduction :</h2>
  <p>
    Hello everyone ! <br>
    I'm so happy to show you my new project. In a continuation of my AI learning path, I decided to create a project to find the word frequetly repeated in a large latin text. Funny isn't it ? To resolve this, I use and learn a new algorithm : The simulated annealing algorithm. What's that you'll tell me ? The explanation of this algorithm, and that I understood, will be in the next part. Moreover, During my fantastic process, I Thought that will be more interessting if I vizualise my data with a graph. So, for this reason, I use a python librairy : Matplotlib. But All in good time like I said in french "Tout viens à point à qui sait attendre" and in english "All things come to those who wait" (Thanks to my dictionnary wordreference.com 😄). Anyway, I devided my explanation into a multiple parts. First, I introduce to the incredible universe of the simulated annealing algorithm. In a second time, I explain my process step by step with screenshots. Finnally, I'll tell you how can you install in local my project if you want to try my code on your machine. Before starting my explanatiion, I want to prevent you I'm not a senior or a junior so my co has a lot of nonsens coding practice but anyone don't make errors at the beginning. Now let's go !
  </p>
</div>
<hr>
<div>
  <h2 align="center">What is the simulated annealing algorithm ?</h2>
  <p>
    Good question ! The simulated annealing algorithm is an algorithm inspired by the smelting work. It's a probalistic optimization algorithm which can escape the local minimum or optimum. It can be use as a research algorithm and it is more effective than the high climbing algorithm (my previous project).
  </p>
</div>
<hr>
<div>
  <h2 align="center">Step by Step :</h2>
  <ol>
    <li>
      <h4>Find a latin text :</h4>
      <p>
        The first thing to do before starting to code is to find a text in latin. For that, I use chatgpt to help me to translate the text that I chose. I starting to create, with the chatgp help, an eulogy about volcano. After a lot of          repetition to write the perfect text with 50 000 words, with no conclusive results, I decided to change the direction. I looked for a text about the punic wars, opposing Roma against Carthago during the ancient time. I found a            website describing the three wars. Then, a translate it in latin with chatGPT. 
      </p>
      <h6>This is an extract of the text :</h6>
      <blockquote>
        Primum Bellum Punicum (264-241 a.C.n.) fuit conflictus inter Carthaginem et Romam, praesertim de dominio Siciliae. Bellum hoc in Sicilia, mari et Africa septentrionali gestum est. Utrumque exercitum et victorias et clades paene           catastrophicas pertulit. Tandem Romani, quorum opes inexhaustae videbantur, ad necessitates belli navalis aptari potuerunt, atque vicerunt.
        Post bellum, quod usque tunc longissimum conflictum continuatum in historia fuisse creditur, Sicilia prima provincia Romana extra fines eius facta est. Tamen Carthago nondum finem habuit cum Roma: sic, postquam res suas internas          composuit et novas facultates pecuniarias obtinuit, bellum mox generatio postea renovatum est in forma Secundi Belli Punici.
        Causae Conflictus Relationes inter duas potestates plerumque pacatae fuerunt per saecula quae bellum praecesserunt. Foedera pacis, sphaeras cuiusque imperii influentiae determinantia, facta sunt annis 509, 348, 306, et 279 a.C.n.         Cum tamen Roma in Magna Graecia maiorem ambitionem ostendere coepit, Carthago decrevit suos in regione interesse tueri. Controversia maxime ardens inter duas potestates erat de Sicilia, insula magni momenti strategici et florenti         oeconomia, quam Carthaginienses diu civitatibus Graecis oppugnabant et quae nunc Romam allicitabat.
        Itaque, cum Roma Rhegium occupavit et Messana (Messine) a Roma petivit ut se tueretur contra duplicem minas Carthaginis et Hieronis II (tyranni Syracusarum), relationes inter duas magnas potestates Mediterraneae deterius factae           sunt. Utraque ex iis de hegemonia sollicita et aemula erat, nec facilis permittere alteram aliquam formam dominationis statuere.
        Anno 288 a.C.n., Mamertini, grex mercennariorum malae famae e Campania in Italia oriundus, Messanam ceperunt
      </blockquote>
    </li>
    <li>
      <h4>First function, clean the data :</h4>
      <p>
        I started my project by organizing my data that I can use. My function take one parameter, the text. Then, I remove all special character like comma or dot. After that, I split the text. The split method, in python, store items in a list. Moreover, I add each elements of my new list in an empty dictionnary without words equal or inferior of 3 letters, with a loop if the current word don't exist in the dictionnary. For each words, I 
      </p>
    </li>
  </ol>
</div>

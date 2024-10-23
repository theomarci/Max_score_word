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
    I'm so happy to show you my new project. In a continuation of my AI learning path, I decided to create a project to find the word frequently repeated in a large latin text. Funny isn't it ? To resolve this, I use and learn a new     
    algorithm : The simulated annealing algorithm. What is it you'll tell me ? I'll explain this algorithm, and that I understood, in the next part. Moreover, During my fantastic process, I Thought that will be more 
    interessting if I vizualise my data with a graph. So, for this reason, I use two python librairies : Matplotlib and pandas. But All in good time like I said in french "Tout viens à point à qui sait attendre" and in english "All 
    things come to those who wait" (Thanks to my dictionnary wordreference.com 😄). Anyway, I devided my explanation into a multiple parts. First, I introduce to the incredible universe of the simulated annealing algorithm. In a second 
    time, I explain my process step by step with screenshots. Finnally, I'll tell you how can you install in local my project if you want to try my code on your machine. Now let's go !
  </p>
</div>
<hr>
<div>
  <h2 align="center">What is the simulated annealing algorithm ?</h2>
  <p>
    Good question ! The simulated annealing algorithm is an algorithm inspired by the smelting work. It's a probalistic optimization algorithm which can escape the local minimum or optimum to find the global maximum or minimum. It can 
    be use as a research algorithm and it is more effective than the high climbing algorithm (my previous project).<br>
    This algorithm take a several parameter : a set, the cooling rate (use to reduce the temperature), temperature (usually I fix it with the 100 value) and finally the iteration (which begins at 0).<br>
    At the beginning, I chosoe the starting point randomly.<br> 
    For each iteration, I select another random point in the set and compare it with the previous point, or with the starting point if it's the first iteration. If the new point is higher than the previous point then the new point 
    become the new reference point, in case of the global maximum search. But if the new point is smaller than the previous one, so I need to calculate the acceptance : 
  </p>
  <h5 align="center">acceptance (for a global maximum)= exponantial((new_value - previous_value) / current_temperature)</h5>
  <h5 align="center">acceptance (for a global minimum) = exponential((previous_value - current_value) / current_temperature)</h5>
  <p>
    Next, I choose a random value between 0 and 1 and I compare this the acceptance. If the random value is smaller than the acceptance, so the worst solutions is accepted. <br>
    Before the end, I calculate the new temperature :
  </p>
  <h5 align="center">temperature = current_temperature * cooling_rate</h5>
  <p>Finally, the function loop until the temperature is equal to 0 or the number of iteration reach 2000, this two condition are my objectives. This is the simulated annealing algorithm.</p>
</div>
<hr>
<div>
  <h2 align="center">Step by Step :</h2>
  <ol>
    <li>
      <h4>Find a latin text :</h4>
      <p>
        The first thing to do before coding my project, I need the most important elements : a latin text. For that, I use chatgpt to help me to translate the text that I chose. I started to create, with chatgp help, an eulogy about 
        volcano. After a lot of repetition to write the perfect text with 50 000 words, with no conclusive results, I decided to change the direction. I looked for a text about the punic wars, opposing Roma against Carthago during the 
        ancient time. I found a website describing the three wars. Then, I translate it in latin with chatGPT. 
      </p>
      <h6>This is an extract of the text :</h6>
      <blockquote>
        Primum Bellum Punicum (264-241 a.C.n.) fuit conflictus inter Carthaginem et Romam, praesertim de dominio Siciliae. Bellum hoc in Sicilia, mari et Africa septentrionali gestum est. Utrumque exercitum et victorias et clades paene          catastrophicas pertulit. Tandem Romani, quorum opes inexhaustae videbantur, ad necessitates belli navalis aptari potuerunt, atque vicerunt.
        Post bellum, quod usque tunc longissimum conflictum continuatum in historia fuisse creditur, Sicilia prima provincia Romana extra fines eius facta est. Tamen Carthago nondum finem habuit cum Roma: sic, postquam res suas internas         composuit et novas facultates pecuniarias obtinuit, bellum mox generatio postea renovatum est in forma Secundi Belli Punici.
        Causae Conflictus Relationes inter duas potestates plerumque pacatae fuerunt per saecula quae bellum praecesserunt. Foedera pacis, sphaeras cuiusque imperii influentiae determinantia, facta sunt annis 509, 348, 306, et 279 
        a.C.n. Cum tamen Roma in Magna Graecia maiorem ambitionem ostendere coepit, Carthago decrevit suos in regione interesse tueri. Controversia maxime ardens inter duas potestates erat de Sicilia, insula magni momenti strategici et 
        florenti oeconomia, quam Carthaginienses diu civitatibus Graecis oppugnabant et quae nunc Romam allicitabat.
        Itaque, cum Roma Rhegium occupavit et Messana (Messine) a Roma petivit ut se tueretur contra duplicem minas Carthaginis et Hieronis II (tyranni Syracusarum), relationes inter duas magnas potestates Mediterraneae deterius factae           sunt. Utraque ex iis de hegemonia sollicita et aemula erat, nec facilis permittere alteram aliquam formam dominationis statuere.
        Anno 288 a.C.n., Mamertini, grex mercennariorum malae famae e Campania in Italia oriundus, Messanam ceperunt
      </blockquote>
    </li>
    <li>
      <h4>First function, clean the data :</h4>
      <p>
        I started my project by organizing my data that I can use. My function take one parameter, the text. Then, I removed all special character like comma or dot. After that, I splited the text. The split method, in python, store 
        items in a list. Moreover, I added each elements of my new list in an empty dictionnary without words equal or smaller of 3 letters, with a loop if the current word don't exist in the dictionnary. For each words, I counted the 
        frequency of appearence and added as the value of the current key. Finally, I returned the dictionnary.
      </p>
    </li>
    <li>
      <h4>Calculate probability</h4>
      <p>
        At this step, I created a new function that calculate for each keys the probability of the word. So, I created a new dictionnary, looped into my previous dictionnary and calculated the new value. In fact, At the moment where I 
        wrote this line, I thought myself to delete this function and calculate the value in the prévious function. Perharps for the next time.
      </p>
    </li>
    <li>
      <h4>Simulated annealing algorithm function</h4>
      <p>
        Now, it's time to code the famous simulated annealing algorithm, the core of my project. This step, for me, was not easy. I started by a recursive function. It's work but I encountered two problems : if there are more of 1000 
        recursion then I have an error and I cannot return the final value when I print my function, on my terminal I see "None", so I can't use the value out of my function. To resolve my problems with the reccursive function, I did 
        some research on the web and found a solution using the while loop. Then, I recreate entirely my function to implement a  while loop. Hurra ! it's work ! <br>
        The goal of my simulated annealing function is to return the word that appears the most time in the text. If you want more precision about this algorithm you can see my little explanation in the previous part, or see my 
        commentary in my code file.
      </p>
    </li>
    <li>
      <h4>Creation of the dataframe of my Dictionnary</h4>
      <p>
        When I finish my first goal for this project, I Thought that will be more interested if I have a data that I can visualize and I can learn about datavisualisation with matplotlib. My first problem is what is the story that I 
        want to tell with my data ? Answer this question, help me to define boundary, select the right data and chart. It's not an easy task but I rise the challenge !<br>
        I started to think to display my data with scatter plot, then with a donut, and also with a scatterd point with different size. I didn't thought, at this moment, what data I want to show, I had not selected any values yet. With 
        some discussion with my school mate, I started to define some boundaries, and selected some data. I search some tip, larn on the web and finally I chose to select 20 data representing the 20 words frequently appear in the text 
        and visualize it with horizontal bar. But before built the chart, I need to transform my dictionnary into a dataframe.<br>
        To do that I chose pandas a python librairy for data manipulation. So, I created a function that return a dataframe of the 20 words with the most occurences.
      </p>
    </li>
    <li>
      <h4>Building my horizontal bar chart</h4>
      <p>
        At this step, I write a new function that display My graph adding tittle and description for abssissa and ordinate.
      </p>
    </li>
    <li>
      <h4>The final result</h4>
      <p>On my terminal :</p>
      <img src=".\src\output.png" align="center">
      <p>This my chart :</p>
      <img src=".\src\Graph_word.png" align="center">
    </li>
  </ol>
</div>
<hr>
<div>
  <h2 align="center">Installation</h2>
  <ol>
    <li>
      Do a fork of my repo
    </li>
    <li>
      on your terminal, move to the venv folder
    </li>
    <li>
      Then, write the command : Scripts\activate
    </li>
    <li>
      Install the librairies : Matplotlib, Pandas
    </li>
    <li>
      Now, you can run my project with this command : python3 .\main.py. That's it !
    </li>
  </ol>
</div>
<hr>
<img src=".\src\New_text.png">


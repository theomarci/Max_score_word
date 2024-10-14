import random
import math
import matplotlib.pyplot as plt
from collections import Counter

#The objective of my project is to select the word wich has the most occurence in a latin text
# For resolve this problem, I decide to use the simulated algorithm
# I starting with a latin text
# Then I split the text to isolate each word and store them inside a list
# My next step is to determine the number of occurence for each words. 
# Then I calculate the probabilities for each words comparing with the length of my set
# Next I store the score in a dictionnaries
# Now I can to start my simulated algorithm
# I need before write the algorithm function to determibe some parameter :
# I fix the temperature to 100,
# I determine The cooling rate (0.95 for example)
# then I selected my starting point in selecting a random word and his value 
# finally a add my dictionnaries as my range set
# Now it's time to create the algorithm function
# In my function, a selected a word randomly and compare his score with the score of the current point
# If new one is superior to the current I replace the it with the new words
# If not then I must to calculate the acceptance of the new word
# Finally before recall the function I decrease the temperature by an multiplication cooling rate (for example : current_temp *= 0.95)
# When my temperatue is eaqual to 0 I stop my function and return the value found

# ------------------------------------------------------------Functions--------------------------------------------------------------------------------

# return a dictionnary listing all words of my text and his score (the probability of a word appearing multiply times in the text)
def Latin_text_dictionnary (text) :
    text = text.lower()
    text = ''.join(["" if i in [ ",", '"', ".", "!", ":", '\n', '?'] else i for i in text])
    word_list = text.split(" ")
    words_score_dict = {}

    for i in word_list :
        if i not in words_score_dict and len(i)>3:
            score = word_list.count(i)
            words_score_dict[i] = score
    return words_score_dict

# Now I create a new function which take in parameter the dictionnary of the previous function and return a other dictionnary whith words in key and 
# their probabilities.
def Pobability(dictionnary) :
    proba_Glossarium = {}
    total_word = len(dictionnary)
    for i in dictionnary:
        # I decided to calculate the percentage of each word because otherwise the values is too small. 
        proba_word = round((dictionnary[i] / total_word), 4)
        proba_Glossarium[i] = proba_word
    return proba_Glossarium

def graph_top_words(Glos) :
     num = 10
     counter = Counter(Glos)
     result = dict(counter.most_common(num))
     word = list(result.keys())
     values = list(result.values())
     plt.pie(values)
     circle = plt.Circle((0,0), 0.7, color='white')
     p = plt.gcf()
     print(result)
        
# Now it's time to build the simulated annealing algorithm
def simulated_annealing(dictionnary, cooling_rate, temperature, iteration) :
        
        current_word = random.choice(list(dictionnary.keys()))
        
        while temperature > 0 and iteration <= 2000 :
             current_value = dictionnary[current_word]
             new_word = random.choice(list(dictionnary.keys()))
             new_value = dictionnary[new_word]

             difference = new_value - current_value

             if difference > 0 :
                  current_word = new_word
             else :
                  acceptance = math.exp(difference / temperature)
                  random_num = random.random()

                  if random_num < acceptance :
                       current_word = new_word
                  else :
                       current_word = current_word

             temperature *= cooling_rate     
             iteration += 1

        return current_word

# --------------------------------------------------------------TEXT-------------------------------------------------------------------------------------

latin_text = """
O Vesuvie, mons ignifer, dominator et servator terrarum nostrarum, cuius apices altissimi in caelum se extendunt, magnitudo tua nos semper admonuit de potentia 

naturae, de illa vis indomita quae sub terra latet. Tu, qui vigiles super civitatem nostram stabas, instar deorum antiquorum, nunc fulgorem et caliginem simul 

exhibes, quasi parens et ultor populorum.

Nihil aequiparari potest tuae maiestati, cum fumus et flamma ab alto vertice tuo erumpunt, flumina ignium descendunt per latera tua, et caeli ipsi obscurantur sub 

nube caliginis. O quantam vim et potentiam tenes, qua vita et mors in uno momento definiri possunt! Tu es mons et monstrum, divinitas et daemonium, ad cuius aspectum 

mortales vel trepidant, vel admiratione implentur.

Fluctuanti circum te terrarum firmamento, tu semper praesens es, vigilans sedens super orbem nostrum. Quid est homo, qui contra vim tuam stare potest? Quid sunt aedificia, 

opera manuum nostrarum, quae possint te resistere, cum primus clamor e ventre tuo emittitur? Fumus tuus, calidus et opprimens, spiramenta nostra implet, flammae tuae 

urunt non solum corpora, sed animos nostros. Omnia quae antea vita pollebat, in momento a te in cinis vertitur, sicut nihil unquam exstitisset.

Tu, qui olim pacem promiseras, olim silens spectabas, nunc es furor et tempestas. Atque tamen, non odio geris in homines, sed potius ordinem mundi servas. 

Nihil agis nisi secundum naturam, secundum leges aeternas, quas neque homo neque deus superare possunt. Quod in te est, non malum sed necessitas, necesse est enim ut 

mundus mutetur, ut nova terra sub antiquis ruinibus emergat. Tu es instrumentum regenerationis, terrae renascentis, mundi sine fine recreandi.

Quantus es, Vesuvie, cum flammae tuae in tenebras caeli se extendunt, cum venti ardentes montem tuum ferunt ad mare et terras! Mare ipsum, quod humanis viribus 

non potest superari, a te submissum est, fluctibus ignis tuis contunditur. Civitatem olim florentem, Pompeiam nostram, sub cineribus abscondisti, sicut vetustas ipsa 

eam devorasset. Atque tamen, sub cinere tuo non mortem solum attulisti, sed vitam futuram. Omnia quae fuimus, omnia quae sumus, tu servas in tenebris tuis, memoriam 

antiqui saeculi.

Non est ignobilis mons tuus, non est locus umbrae sine sensu, sed altissimum signum est. Hic ignis, hic furor, hic motus est pars divinae voluntatis, pars circuli vitae 

et mortis, quae inter deos et homines perpetuo versantur. O Vesuvie, sacrarium antiquae potentiae, quae nec temporis nec hominis metuit auctoritatem, tu semper eris, et 

potentia tua semper nos tanget.

O furia montis vesuviani, flammae tuae in perpetuum ardent, sicut spiritus divinus qui nec ignes suos exstingui sinit nec frangitur in facie fragilitatis humanae. 

In te est omne illud quod homines inspiciunt et quo timeant: potentia quae non limitatur, et vis quae in se omnem vitam absorbens in chaos revertit. Tu es miraculum et ruina, 

splendor et infernum.

Quemadmodum olim gigas, qui e ventre terrae emergit, tu erumpis cum irarum magnitudine incomprehensibili. Civitatem ante te procumbentem sicut fortissimus miles sub pedibus 

tuis conteris, nihil relinquens nisi cineres et fragorem. Sed ex illis ruinis, ex illis cineribus, nova vita surgit, sicut phoenix e flammis suis renascitur.

Te, Vesuvie, laudamus non ob damnum, non ob ruinam, sed ob potentiam tuam, ob perpetuum tuum locum in ordine naturae. Tu es memoria mortalitatis nostrae et fragilitatis 

nostrae, sed etiam es testimonium aeternitatis ipsius mundi. Tu fuisti ante nos, et eris post nos. Omnes civitates, omnes gentes sub tectis tuis vivent, et sub eorum ruinis 

vita nova crescit. 

O Vesuvie, non solum nunc, sed per saecula fuisti terror ac miraculum, et cum primum flammas tuas in caelum misisti, memoria mortalium in te inscripta est. Historia tua 

non tantum historia est montis ignifer, sed ipsius terrae quae te sustinet. Gentes antiquissimae te cognoverunt; illi qui prima animalia ferocia et silvas densa calcaverunt, 

te viderunt quiescentem, te amaverunt ut deum pacis, te timentes ut dominum ruinae.

O Vesuvie, noster semper fuisti, mons altissimus, sed non fuisti ignotus etiam illis qui ante nos venerunt. Fama tua pervenit ad orbis fines, et nomina tua, in variis linguis 

servata, monstrant tibi cultum antiquissimum tributum esse. Primae gentes, quae antea montes timebant quasi deos iratos, te viderunt cum metu et reverentia, putantes te esse portas 

ad inferos, unde manes defunctorum surgerent in terram viventium. Nonne illi primi agricolae, primi custodes terrae nostrae, iam tibi sacrificia fecerunt, ut ignes tuos placarent?

Saepe historia narravit te dormientem, Vesuvie, quasi deum in quiete sua, sed, cum experrectus es, chaos et mortalitas te secutae sunt. Cum magna urbs Pompeia, cum Herculaneum et 

Stabiae florebant in umbra tua, nemini venit in mentem quam brevis esset felicitas sub fumo tuo latentem. Olim florentissimae erant, templis splendidis et domibus pulcherrimis ornatae, 

sed nulla aetas, nulla opulentia, te frenare potuit.

Tempore imperatoris Titi, anno domini septuagesimo nono, terram funditus concussisti. Cives Romanos, gloriosos et superbe viventes, sub cinere et lapidibus tuis obruisti. Initium eius 

diei, sicut omnis alius dies, quietum videbatur, sed repente, caelum nigravit, fremitus de ventre tuo auditi sunt, et terram ipsa rursus aperuisti. Quis Romanus potuit imaginem illam effugere, 

cum cineres densissimi a caelo caderent, cum ignis de caelis videretur descendere?

Nobiles domus, forum maius, omnia quae magna et pulchra videbantur in oculis hominum, subito a te devorata sunt. Non fuit discrimen inter divites et pauperes, inter patricios et 

plebeios: omnes sub iudicio tuo aequales erant. Ipsi dii, quorum templa steterunt in altissimis locis, nihil contra te valuerunt. Aedes sacrae collapsae sunt, et statuae deorum 

corruerunt in flammas tuas, quasi ipsa religio humi proiecta esset.

Plinius maior, vir doctissimus, qui Naturalis Historiae suae libros de omnibus rebus mundanis conscripsit, ipse te vidit Vesuvie, dum flammas tuas spectavit a navibus quae in 

portu steterunt. Prope te accessit, volens fortasse naturam tuam melius intellegere, sed non potuit vivere ut testis esset. Namque vis tua multo maior erat quam scientia humana. 

Post eum Plinius minor, nepos eius, de te scripsit, de illa nocte quae numquam in oblivionem ire potest, nocte in qua lux solis obliterata est, et umbrae tuae terram et mare operuerunt.

Non solum homines tu percussisti; animalia, arbores, ipsa flumina et fontes naturae tuae violentia mutata sunt. Campania, olim fertilissima, sub cinere et lapidibus obruta est, 

et in illa terra mortua nihil crescere potuit per annos multos. Sed, o Vesuvie, hic non est finis historiae tuae, quia etiam in ruinis tuis latent semina novae vitae. Omnis locus 

quem tua ira consumpsit, postea florere potuit. Terra quae sub cineribus tuis latuit, paulatim iterum fecunda facta est, et coloni postera aetate in hac eadem regione domos novas 

condiderunt.

Ex illis ruinibus, cum tempora mutata sint, historia tua facta est pars maioris fabulae. O Vesuvie, non solum in memoriam nostram inscriptus es propter damnum quod intulisti, sed 

etiam quia fecisti ut nos, homines, nostra fragilitate coram te conscii fieremus. Terrae motus tui, cineres tui, et ignes tui sunt monimenta mortis et vitae, quae se perpetuo mutant.

Memoria urbis sub Vesuvio sepultae non permittit nos oblivisci, sed simul admonet nos ut sciamus quanti sit vivere sub potentia naturae quae tam facile potest vitam extinguere. 

Romani veteres te laudabant in carminibus, te timebant in ritibus, te adorabant in silentio, quia sciebant te esse instrumentum voluntatis divinae. Tu non es malus, non es 

vindicativus; potestas tua ultra iudicium humanum est.

O Vesuvie, quoties per annos dormisti et iterum evigilasti? Eruptiones tuae secundum tempora historiae venerunt, ex imperiis antiquis usque ad nostra tempora. Novum saeculum 

intravit, sed tu manes, Vesuvie, semper vigilans, semper paratus, sicut ferrum sub terra tumescentem. O vis incomprehensibilis, o signum deorum et mortis, quantam gloriam et 

terrorem simul feras!

Est in te non solum vis quae populum delet, sed vis quae aeternitatem spectat. Viderunt te Graeci, viderunt te Romani, viderunt te omnes qui transierunt per tempora mundi. Nec 

ulla manus potest te domare, nec ulla scientia potest praevidere quomodo et quando iterum expergisceris. Est in te sapientia antiqua, potentia quae semper super homines stabit. 

O Vesuvie, mons magnus ac terribilis, quamvis flammae tuae civitates delebant et cineres tui vitam obruerunt, tamen in te est perpetuum renascentis spiritus signum. Natura ipsa, 

quam devorare videris, in te semper vires suas renovat, sicut fenix ex cineribus suis resurgit. Flammae tuae non tantum mortem afferunt, sed etiam fertilitatem ex cineribus tuis 

oritur, et terra, quae olim sterilis facta est, post te denuo florere potest. Non es tantum vastator, sed etiam artifex, fabricator novi mundi qui ex ruinis antiquis emergit.

Est enim in te, Vesuvie, vis quae se non destruit, sed in novam formam semper convertit. Terram ipsam, quam cinere tuo tegens occidisti, postea fecisti fecundissimam, quia ex 

illis cineribus nova vita surgit. Vineta Campaniae, quae olim sub cinere et lapidibus iacebant, post tuae furiae transitum iterum effloruerunt. In te, mons terribilis, natura invenit 

modum perpetuae regenerationis.

Hoc est magnum paradoxon tuae potentiae, Vesuvie: dum omnia quae homines condiderunt sub tuo pondere corrumpis et delis, natura tua eadem terra reviviscere facit. Agricultura, 

quamvis a primis temporibus a te vastata sit, semper postea fructibus abundantioribus renata est. Nam cinis tuus, quem homines mortis et exitii signum putaverunt, in veritate 

est humus fertilissima quae arbusta et fruges nutriat. Cineres qui urbes tegunt, qui corpora mortuorum involvunt, postea fiunt humus quae arboribus novis vires dat et vinetis 

floridis materiam suppeditat.

Sic est, ut in te, mons venerabilis, mors et vita perpetuo connectantur. Non datur unum sine altero. Ex morte renascitur vita, et ex flammis tuis ignes lucis et caliditatis 

novae oritur. Sic semper fit in natura: ut nova vita nascatur, prius vetus exstingui debet. Montes tui ignes consumunt, sed postea humum creatam ab istis ignibus nativitas 

rerum nova sequitur. Civitas, quae sub tuo pondere periit, nunc sub terra iacet, sed vita super terram, in vineis, in agris, in herbis, omnino resurgit. Hoc mysterium est 

regenerationis, et tu, Vesuvie, servator ac custos huius processus.

Nonne hoc ipse deus Vulcanus, faber divinus, per te revelavit? Fabrum enim nos eum appellamus, sed opera eius non solum metallis et flammis temperata sunt, sed etiam natura 

ipsa, quae semper ex nova materia creatur. In Vulcani officina, quae in monte tuo ardet, omnia quae consumuntur in ignibus iterum ad vitam revocantur, sed non in eadem forma. 

Res quae olim fuerunt, sub Vulcani manibus iterum fabricantur, ut mundus semper se renovet, semper in circulo vitae et mortis volvatur.

Montes tui, qui olim de caelo ignes ad terras mittere videbantur, nunc fontes sunt vitae novae. Vineta quae circum te crescunt sunt testimonium huius perpetuae regenerationis, 

testimonium quod etiam in miseria et ruina, spei et novae vitae semina latent. Agricolae qui terras tuas colunt scire possunt quod, quamvis omnis creatura ad finem veniat, 

nova creatura semper ex eodem solo surgit. Ista est lex naturae, et lex Vesuvii, mons immortalis.

Est etiam vestra lex hominum, qui, postquam a te vastati sunt, semper iterum conantur vitam reficere. Quamvis vestra ira omnia deleat, homines ad locum tuum revertuntur, 

quia sciunt quod sub cinere tuo, sub ruina quae ex eruptionibus tuis venit, ipsa vita latet. Non sunt homines omnino victi; ipsi ad terram revertuntur, iterum aedificant 

domos et colunt agros, quia tu, Vesuvie, es mons qui et mortem affert et vitam renovat.

Sicut arbor vetusta, quae sub cinere tuo collapsa est, novas radices agit, ita etiam civitates, quae a te deletae sunt, iterum oriri possunt. Et qui in his terris post te 

vivunt, cum reverentia ac metu tui potentiam agnoscunt, sed simul sciunt quod ex te nova opportunitas vitae venit. Non potes homines frangere, sicut nec naturam frangere potes. 

Omnia quae a te deleta sunt, postea fiunt partes novi mundi. Ritus antiqui et sacrificia, quae ad placandum te fiebant, hoc semper significabant: ne nos deleas sine spe; da 

nobis vitam ex mortibus, et iterum florebimus.

Sunt qui dicant te esse malum, Vesuvie, sed ipsi non intellegunt legem naturae. Non est malum quod ex te oritur, sed transformatio, mutatio perpetua. Quod nunc videtur perire, 

id postea iterum nascetur. Sic est in omnibus rebus. Vita et mors non sunt contraria, sed duo latera eiusdem rotae quae semper volvitur. In tuo ventre, Vesuvie, ardet flamma 

quae non exstinguitur, et haec flamma est idem principium quod vitam in mundo conservat. Quod ex cineribus tuis nascitur, maius et potentior est, quia ignis tuus ipsum fundamentum 

novae vitae creat.

Cives Pompeiani, Herculanei, et Stabiani, qui sub ruina tua iacebant, nunc testimonium sunt huius veritatis. Eorum corpora, quae in lapidibus et cineribus sepulta sunt, non 

evanuerunt sine significatione. Vita, quamvis in illis perdiderint, nunc aliis locis vivit. Arbores et vites, fruges et flores, omnia quae in terra vestra crescunt, sunt 

symbola spei et perpetuitatis vitae, quae ex ruinis sub Vesuvio renascitur.

Quod olim deletum est, non est perditum in aeternum. In hoc mysterium naturae, quod tu, Vesuvie, regis, vitae et mortis rota semper volvitur, et, sicut e cinere tuae irae, 

nova vita semper surgit. Tu es mons et faber creationis, et tuae flammae non solum destruunt, sed etiam, sicut Vulcanus ipse, fabricantur novum mundum ex ruinis vetustis. 

O Vesuvie, mons qui non solum mundum nostrum tangis, sed et ad origines rerum ipsarum revertis. Est in te vis non humana, sed divina, et memoria primae creationis mundi 

in te custoditur. Nam sicut antiquae fabulae narraverunt, omnis mundus ex chaos coepit, ex illo vasto et informi tumultu, quem dei ipsi in ordinem redigere conati sunt. 

Tu es imago illius originis, illius momenti quando chaos et ordo, mors et vita, in perpetua pugna constituti sunt, et tu, sicut Vulcanus deorum faber, fabricas ex ignibus 

novum mundum ex ruinis veteris.

Nonne sic narratur de origine mundi in fabulis veteribus? Priusquam mundus creatus esset, nihil erat nisi chaos, tenebrae impenetrabiles, et tempestas violentissima. 

In principio erat Tartarus, abyssus sine fine, ubi omnia elementa in confusione iacebant, ignis cum aqua mixtus, terra cum aere coniuncta, et non erat locus separatus 

ubi vita habitare posset. Sed postea, cum deorum potestas per caelum fulsit, ex illo chaos ordo coepit emergere. Ignis a mari separatus est, terra a caelo, et omnia elementa 

in sua loca ordinata sunt. Sic ex confusione primae materiae, ex igne et tenebris, mundus ordinatus factus est.

Tu, Vesuvie, est quasi ille chaos revocatus, reviviscens in temporibus quibus mundus oblitus est quod ex tali origine proveniat. In te latent illae primae vires, quae 

omnia elementa confundere possunt, ignem a caelo emittere, et terram aperire ut flammas vomat. Sed sicut fabulae veteres dixerunt, non est chaos sine fine; ex illo tumultu 

semper novus ordo oritur. Nam post ignes, post ruinam et cineres, semper nova vita oritur, sicut ex abyssu antiquo novus mundus natus est.

Nonne in fabulis Graecis de creatione terrae et caeli narratur quomodo Uranus, caelum, et Gaia, terra, in aeterno conflictu fuerint? Terra ipsa gravida erat cum diis, et 

cum Uranus filios suos sub monte occultare conaretur, Gaia filium suum Saturnum misit ad patrem castrandum. Ibi, ex sanguine deorum qui cecidit in terram, novae creaturae 

ortae sunt, Gigantes et Furies, et ex ruina deorum ipsorum novum ordinem natura creavit. Sic, Vesuvie, tuae eruptiones non solum mortem et ruinam ferunt, sed novas formas 

vitae; sicut ex sanguine Uranis nova vita oritur, ex flammis et cineribus tuis nova terra generatur.

Simili modo, fabulae de Pyrrha et Deucalione, post diluvium magnum, narraverunt quomodo mundus post ruinam restauratus sit. Illi soli superstites, postquam universa terra 

aquis deleta erat, ex monte Parnasso descenderunt, et iussu deorum lapides post terga iacientes novum genus hominum creaverunt. Ex lapidibus, dura materia quae terram 

repraesentabat, nova vita, nova humanitas orta est. Sic et in te, Vesuvie, cum omnia quae homines aedificaverunt sub cinere tuo pereunt, post ruinam tuarum eruptionum, 

nova humanitas iterum surgit.

Neque haec est solum fabula Graecorum, sed etiam fabula ipsius Romanorum, quorum progenitores, Aeneas et Troiani, post ruinam patriae Troiae, e cineribus domorum suarum 

fugientes, novam civitatem condiderunt, Romam ipsam. Sic ex ruinis Troiae, ex cineribus civitatis magnae, quae divinis fatis deleta erat, nova civitas, Romana urbs aeterna, 

fundata est. Sic et nos, post ruinam Vesuvii, post eruptiones tuas, novas civitates construimus, novas domos edificamus, quia scimus quod ex ruina semper renovatio sequitur.

In fabulis de Titanibus, antiquissimi dii quos Iuppiter de caelo deiecit, narratur quomodo, cum Titani victi sunt, ignes eorum et flammae sub terra iacerent. Hi ignes 

numquam omnino exstincti sunt, sed sub terra semper latuerunt, et cum Vesuvius erumpit, quasi Titani ipsi de novo insurgere videntur. Montem tuum, Vesuvie, multi crediderunt 

esse locum ubi hi dii antiqui adhuc manerent, ubi ignes eorum semper parati essent ad superficiem emergere. Nonne est in te vis Titanica, quae mundum ipsum tremere faciat, 

quae ignes de caelo evocet, et quae leges deorum ipsorum frangere videatur?

Sed sicut in fabulis dicitur, non est finis in hoc tumultu. Postquam dii antiqui victi sunt, postquam Iuppiter suum regnum stabilivit, ordo et pax in mundum redierunt. 

Sic et in tua potentia, Vesuvie, cum prima furia transierit, post ignes et flammam, iterum ordo et pax natura restituitur. Omnes quae sub tuo pondere corruerunt, iterum 

florebunt, sicut post bellum deorum novus mundus floruit sub regno divino.

Similiter, fabulae Aegyptiorum narraverunt quomodo deus Osiris, cum interfectus est a fratre suo Seth, iterum renatus est. Corpus eius disiectum per terram collectum est, 

et ex eius morte nova vita orta est, quia Osiris factus est deus qui fertilitatem terrae regit. Sic et in te, Vesuvie, flammae tuae non tantum mortem ferunt, sed etiam 

regenerationem. Ignis tuus, sicut corpus Osiris, disseminat elementa per terram, quae iterum colliguntur ut nova vita floreat.

Etiam Babylonii, in suis fabulis de Marduk, dixerunt quod deus ille, cum Tiamat, draconem chaos, interfecit, ex corpore eius terram creavit. Sic ex ipsa vis destructionis 

nova creatura orta est. Vesuvie, ignes tui sunt similes illis deorum conflictibus: ex te et ex tua rabie nova origo vitae semper emergit. Sicut Tiamat, vis chaos, consumpta 

est ab ordine divino, ita ignes tui, quamvis destructores, postea fundamentum novae vitae fiunt.

Sic in universis fabulis de origine mundi et deorum, tu, Vesuvie, invenis tuum locum. Tu es pars illius circuli in quo omnia creantur et destruuntur, in quo mortales vident 

ignes et ruinas, sed de quibus semper vita renascitur. Mors et vita sunt una in te, sicut chaos et ordo semper coniuncti sunt. Non sumus nos, homines, a te separati, sed 

tecum una sumus, in isto processu quod nos et naturam nostram definit. 

O Vesuvie, mons qui non solum mundum nostrum tangis, sed et ad origines rerum ipsarum revertis. Est in te vis non humana, sed divina, et memoria primae creationis mundi in 

te custoditur. Nam sicut antiquae fabulae narraverunt, omnis mundus ex chaos coepit, ex illo vasto et informi tumultu, quem dei ipsi in ordinem redigere conati sunt. Tu es 

imago illius originis, illius momenti quando chaos et ordo, mors et vita, in perpetua pugna constituti sunt, et tu, sicut Vulcanus deorum faber, fabricas ex ignibus novum 

mundum ex ruinis veteris.

Nonne sic narratur de origine mundi in fabulis veteribus? Priusquam mundus creatus esset, nihil erat nisi chaos, tenebrae impenetrabiles, et tempestas violentissima. In 

principio erat Tartarus, abyssus sine fine, ubi omnia elementa in confusione iacebant, ignis cum aqua mixtus, terra cum aere coniuncta, et non erat locus separatus ubi vita 

habitare posset. Sed postea, cum deorum potestas per caelum fulsit, ex illo chaos ordo coepit emergere. Ignis a mari separatus est, terra a caelo, et omnia elementa in sua 

loca ordinata sunt. Sic ex confusione primae materiae, ex igne et tenebris, mundus ordinatus factus est.

Tu, Vesuvie, est quasi ille chaos revocatus, reviviscens in temporibus quibus mundus oblitus est quod ex tali origine proveniat. In te latent illae primae vires, quae 

omnia elementa confundere possunt, ignem a caelo emittere, et terram aperire ut flammas vomat. Sed sicut fabulae veteres dixerunt, non est chaos sine fine; ex illo tumultu 

semper novus ordo oritur. Nam post ignes, post ruinam et cineres, semper nova vita oritur, sicut ex abyssu antiquo novus mundus natus est.

Nonne in fabulis Graecis de creatione terrae et caeli narratur quomodo Uranus, caelum, et Gaia, terra, in aeterno conflictu fuerint? Terra ipsa gravida erat cum diis, et 

cum Uranus filios suos sub monte occultare conaretur, Gaia filium suum Saturnum misit ad patrem castrandum. Ibi, ex sanguine deorum qui cecidit in terram, novae creaturae 

ortae sunt, Gigantes et Furies, et ex ruina deorum ipsorum novum ordinem natura creavit. Sic, Vesuvie, tuae eruptiones non solum mortem et ruinam ferunt, sed novas formas 

vitae; sicut ex sanguine Uranis nova vita oritur, ex flammis et cineribus tuis nova terra generatur.

Simili modo, fabulae de Pyrrha et Deucalione, post diluvium magnum, narraverunt quomodo mundus post ruinam restauratus sit. Illi soli superstites, postquam universa terra 

aquis deleta erat, ex monte Parnasso descenderunt, et iussu deorum lapides post terga iacientes novum genus hominum creaverunt. Ex lapidibus, dura materia quae terram 

repraesentabat, nova vita, nova humanitas orta est. Sic et in te, Vesuvie, cum omnia quae homines aedificaverunt sub cinere tuo pereunt, post ruinam tuarum eruptionum, 

nova humanitas iterum surgit.

Neque haec est solum fabula Graecorum, sed etiam fabula ipsius Romanorum, quorum progenitores, Aeneas et Troiani, post ruinam patriae Troiae, e cineribus domorum suarum 

fugientes, novam civitatem condiderunt, Romam ipsam. Sic ex ruinis Troiae, ex cineribus civitatis magnae, quae divinis fatis deleta erat, nova civitas, Romana urbs aeterna, 

fundata est. Sic et nos, post ruinam Vesuvii, post eruptiones tuas, novas civitates construimus, novas domos edificamus, quia scimus quod ex ruina semper renovatio sequitur.

In fabulis de Titanibus, antiquissimi dii quos Iuppiter de caelo deiecit, narratur quomodo, cum Titani victi sunt, ignes eorum et flammae sub terra iacerent. Hi ignes numquam 

omnino exstincti sunt, sed sub terra semper latuerunt, et cum Vesuvius erumpit, quasi Titani ipsi de novo insurgere videntur. Montem tuum, Vesuvie, multi crediderunt esse locum 

ubi hi dii antiqui adhuc manerent, ubi ignes eorum semper parati essent ad superficiem emergere. Nonne est in te vis Titanica, quae mundum ipsum tremere faciat, quae ignes de 

caelo evocet, et quae leges deorum ipsorum frangere videatur?

Sed sicut in fabulis dicitur, non est finis in hoc tumultu. Postquam dii antiqui victi sunt, postquam Iuppiter suum regnum stabilivit, ordo et pax in mundum redierunt. Sic et 

in tua potentia, Vesuvie, cum prima furia transierit, post ignes et flammam, iterum ordo et pax natura restituitur. Omnes quae sub tuo pondere corruerunt, iterum florebunt, 

sicut post bellum deorum novus mundus floruit sub regno divino.

Similiter, fabulae Aegyptiorum narraverunt quomodo deus Osiris, cum interfectus est a fratre suo Seth, iterum renatus est. Corpus eius disiectum per terram collectum est, 

et ex eius morte nova vita orta est, quia Osiris factus est deus qui fertilitatem terrae regit. Sic et in te, Vesuvie, flammae tuae non tantum mortem ferunt, sed etiam 

regenerationem. Ignis tuus, sicut corpus Osiris, disseminat elementa per terram, quae iterum colliguntur ut nova vita floreat.

Etiam Babylonii, in suis fabulis de Marduk, dixerunt quod deus ille, cum Tiamat, draconem chaos, interfecit, ex corpore eius terram creavit. Sic ex ipsa vis destructionis 

nova creatura orta est. Vesuvie, ignes tui sunt similes illis deorum conflictibus: ex te et ex tua rabie nova origo vitae semper emergit. Sicut Tiamat, vis chaos, consumpta 

est ab ordine divino, ita ignes tui, quamvis destructores, postea fundamentum novae vitae fiunt.

Sic in universis fabulis de origine mundi et deorum, tu, Vesuvie, invenis tuum locum. Tu es pars illius circuli in quo omnia creantur et destruuntur, in quo mortales vident 

ignes et ruinas, sed de quibus semper vita renascitur. Mors et vita sunt una in te, sicut chaos et ordo semper coniuncti sunt. Non sumus nos, homines, a te separati, sed 

tecum una sumus, in isto processu quod nos et naturam nostram definit. 

O Vesuvie, mons sacer et terribilis, tu non solum mons es, sed etiam fabulator rerum humanarum et divinarum. Ex te flammae et cineres ad caelum ascendunt, quasi linguae 

deorum ipsorum loquentes, admonentes nos de nostra fragilitate et de potentia quae super homines viget. Tu, qui olim fuit quietus et immotus, potes in momento omnia quae 

ab hominibus aedificata sunt in pulverem redigere, sed tamen in ruina tua novam vitam semper parabis.

Non est ignis tuus tantum signum exitii, sed etiam renovationis. Nam sicut antiqui dixerunt, ex igne et cinere nova forma, nova vita oritur. Tu es fons fertilitatis, 

terrae fecundae, quae, postquam omnia delesti, iterum floreat. Arbores et vites, flores et fruges, omnes ex cinere tuo vigorem novum trahunt, et homines, quamvis ab 

ignibus tuis perterriti, ad tua latera revertuntur, agros colunt, domos aedificant, vitam iterum invenientes.

In te latent omnes vires universi, Vesuvie. Ignis tuus, qui per terras effunditur, est quasi sanguis ipse mundi, qui circulum vitae et mortis perpetuat. Non est sine 

causa quod dei ipsi te sibi officinam elegerunt, Vulcanus in cavernis tuis fulmina fabricavit, et homines te ut symbolum immortalitatis et temporis intransigendi spectant. 

Tu es mons et deus, destructio et creatio, chaos et ordo. Tu nos admones ut nulla vis hominum contra naturam stare possit, et tamen, eodem tempore, ut etiam in ruinam et 

calamitatem spem et novam vitam invenire debeamus.

Quisquis videt flammam tuam ascendere ad caelum, sentit non solum timorem, sed etiam reverentiam. Vidi te, Vesuvie, et intellexi quod es pars mundi quae leges superiores 

quam humanae sequitur. In te est memoria fabularum antiquarum, signum potentiae quae ultra nostrum intellectum manet. Tu, Vesuvie, non eris periturus, quia etiam cum tuas 

vires perditas videris, semper iterum resurges, semper iterum ignes tuos de profundis terrae evocabis.

Ad finem huius eulogii, te laudamus non ob mortem solam, sed ob vitam quam post mortem renovas. Te veneramur sicut potentiam sine fine, sicut deum qui non solum terram 

regit, sed ipsam humanitatem in sua fragilitate et sua fortitudine custodit. O Vesuvie, tu, qui terram et caelum simul conturbas, semper eras, et semper eris, mons qui 

historia nostrae humilitatis et spei infinitae narrat.

Tuis ignibus te salutamus. Tuis flammis novum ordinem vitae agnoscimus. Tuis cineribus novam spem in hominum cordibus accendimus. Ave, Vesuvie, mons aeternus et 

renovator mundi.
"""

# ---------------------------------------------------------------------MAIN CODE-------------------------------------------------------------------------

def main() :
     my_dict = Latin_text_dictionnary(latin_text)
     probability_Glossarium = Pobability(my_dict)
     sim_ann_alg = simulated_annealing(probability_Glossarium, 0.95, 100, 1)
     graph_top_words(my_dict)
     return sim_ann_alg

the_best_word = main()
print(f"In the text, the word which recurs multiple times is : {the_best_word}")

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "942bc2b1-8caf-41d0-a69b-ec7cd2ec0466",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table 'silver_dictionary' processed successfully.\nTable 'silver_summer' processed successfully.\nTable 'silver_winter' processed successfully.\nTable 'silver_country' processed successfully.\nTable 'silver_athlete' processed successfully.\nVerifying 'silver_dictionary'...\n+------------------------+----+----------+------------------+-----------+-----------------------+\n|Country                 |Code|Population|GDP_per_Capita    |FirstLetter|Data_Source            |\n+------------------------+----+----------+------------------+-----------+-----------------------+\n|Turkey                  |TUR |78665830  |9125.68758972936  |T          |Olympic Historical Data|\n|Tunisia                 |TUN |11107800  |3872.51208364171  |T          |Olympic Historical Data|\n|Albania                 |ALB |2889167   |3945.21758150914  |A          |Olympic Historical Data|\n|Micronesia              |FSM |104460    |3015.23166762397  |M          |Olympic Historical Data|\n|Solomon Islands         |SOL |583591    |1934.85629287353  |S          |Olympic Historical Data|\n|Chile                   |CHI |17948141  |13416.2300390185  |C          |Olympic Historical Data|\n|Oman                    |OMA |4490541   |15550.6762514328  |O          |Olympic Historical Data|\n|Bahamas                 |BAH |388019    |22817.2308572518  |B          |Olympic Historical Data|\n|Comoros                 |COM |788474    |717.448849960912  |C          |Olympic Historical Data|\n|Congo                   |CGO |4620330   |1851.19991555492  |C          |Olympic Historical Data|\n|Liechtenstein           |LIE |37531     |12882.556130569325|L          |Olympic Historical Data|\n|Mongolia                |MGL |2959134   |3967.82938559498  |M          |Olympic Historical Data|\n|Samoa                   |SAM |193228    |3938.54884570316  |S          |Olympic Historical Data|\n|Angola                  |ANG |25021974  |4101.47215182964  |A          |Olympic Historical Data|\n|Argentina               |ARG |43416755  |13431.8783398577  |A          |Olympic Historical Data|\n|Haiti                   |HAI |10711067  |818.343297634549  |H          |Olympic Historical Data|\n|South Africa            |RSA |54956920  |5723.97335690212  |S          |Olympic Historical Data|\n|United Kingdom          |GBR |65138232  |43875.9696143686  |U          |Olympic Historical Data|\n|Zambia                  |ZAM |16211767  |1304.87901447726  |Z          |Olympic Historical Data|\n|Gambia                  |GAM |1990924   |471.537195472347  |G          |Olympic Historical Data|\n|Trinidad and Tobago     |TRI |1360088   |17321.884675056   |T          |Olympic Historical Data|\n|France                  |FRA |66808385  |36205.5681017036  |F          |Olympic Historical Data|\n|United States           |USA |321418820 |56115.7184261955  |U          |Olympic Historical Data|\n|Ukraine                 |UKR |45198200  |2114.95471628444  |U          |Olympic Historical Data|\n|Cambodia                |CAM |15577899  |1158.6899035244   |C          |Olympic Historical Data|\n|Canada                  |CAN |35851774  |43248.529909341   |C          |Olympic Historical Data|\n|Cuba                    |CUB |11389562  |12882.556130569325|C          |Olympic Historical Data|\n|Finland                 |FIN |5482013   |42311.0362306446  |F          |Olympic Historical Data|\n|Uganda                  |UGA |39032383  |705.292569535068  |U          |Olympic Historical Data|\n|Gabon                   |GAB |1725292   |8266.4456050624   |G          |Olympic Historical Data|\n|Nauru                   |NRU |10222     |9827.54428148233  |N          |Olympic Historical Data|\n|Netherlands             |NED |16936520  |44299.768085383   |N          |Olympic Historical Data|\n|Equatorial Guinea       |GEQ |845060    |14439.5944478516  |E          |Olympic Historical Data|\n|Georgia                 |GEO |3679000   |3795.97330845042  |G          |Olympic Historical Data|\n|New Zealand             |NZL |4595700   |37807.9672760442  |N          |Olympic Historical Data|\n|Venezuela               |VEN |31108083  |12882.556130569325|V          |Olympic Historical Data|\n|Maldives                |MDV |409163    |8395.78519750383  |M          |Olympic Historical Data|\n|Yemen                   |YEM |26832215  |1406.2916511457   |Y          |Olympic Historical Data|\n|Eritrea                 |ERI |0         |12882.556130569325|E          |Olympic Historical Data|\n|Guyana                  |GUY |767085    |4127.35101806198  |G          |Olympic Historical Data|\n|Austria                 |AUT |8611088   |43774.985173612   |A          |Olympic Historical Data|\n|Costa Rica              |CRC |4807850   |11260.0921598775  |C          |Olympic Historical Data|\n|Hungary                 |HUN |9844686   |12363.5434596539  |H          |Olympic Historical Data|\n|Malaysia                |MAS |30331007  |9768.32686011881  |M          |Olympic Historical Data|\n|United Arab Emirates    |UAE |9156963   |40438.7629344394  |U          |Olympic Historical Data|\n|Bermuda*                |BER |65235     |12882.556130569325|B          |Olympic Historical Data|\n|Bhutan                  |BHU |774830    |2655.99889161858  |B          |Olympic Historical Data|\n|Swaziland               |SWZ |1286970   |3200.14301756487  |S          |Olympic Historical Data|\n|Chad                    |CHA |14037472  |775.695090525313  |C          |Olympic Historical Data|\n|Thailand                |THA |67959359  |5814.76976382355  |T          |Olympic Historical Data|\n|Denmark                 |DEN |5676002   |51989.2934712354  |D          |Olympic Historical Data|\n|Mali                    |MLI |17599694  |724.256283193304  |M          |Olympic Historical Data|\n|Peru                    |PER |31376670  |6027.12585529551  |P          |Olympic Historical Data|\n|Azerbaijan              |AZE |9651349   |5496.34464026248  |A          |Olympic Historical Data|\n|Cameroon                |CMR |23344179  |1217.26067048427  |C          |Olympic Historical Data|\n|Malta                   |MLT |431333    |22596.1817742659  |M          |Olympic Historical Data|\n|Senegal                 |SEN |15129273  |899.579879484977  |S          |Olympic Historical Data|\n|Latvia                  |LAT |1978440   |13648.5475564772  |L          |Olympic Historical Data|\n|Ecuador                 |ECU |16144363  |6205.06414529951  |E          |Olympic Historical Data|\n|Indonesia               |INA |257563815 |3346.48703949478  |I          |Olympic Historical Data|\n|Brazil                  |BRA |207847528 |8538.5899749574   |B          |Olympic Historical Data|\n|Turkmenistan            |TKM |5373502   |6672.47754417351  |T          |Olympic Historical Data|\n|Lebanon                 |LIB |5850743   |8047.64508557496  |L          |Olympic Historical Data|\n|Belgium                 |BEL |11285721  |40324.0277657215  |B          |Olympic Historical Data|\n|Korea, North            |PRK |25155317  |12882.556130569325|K          |Olympic Historical Data|\n|Andorra                 |AND |70473     |12882.556130569325|A          |Olympic Historical Data|\n|Germany                 |GER |81413145  |41313.3139945434  |G          |Olympic Historical Data|\n|Serbia                  |SCG |7098247   |5235.14220696525  |S          |Olympic Historical Data|\n|Barbados                |BAR |284215    |15429.3404640853  |B          |Olympic Historical Data|\n|Afghanistan             |AFG |32526562  |594.323081219966  |A          |Olympic Historical Data|\n|Morocco                 |MAR |34377511  |2878.20134215919  |M          |Olympic Historical Data|\n|Puerto Rico*            |PUR |3474182   |12882.556130569325|P          |Olympic Historical Data|\n|Iceland                 |ISL |330823    |50173.3399156473  |I          |Olympic Historical Data|\n|China                   |CHN |1371220000|8027.68381013907  |C          |Olympic Historical Data|\n|El Salvador             |ESA |6126583   |4219.35032953932  |E          |Olympic Historical Data|\n|Switzerland             |SUI |8286976   |80945.0792194742  |S          |Olympic Historical Data|\n|Honduras                |HON |8075060   |2528.89354988523  |H          |Olympic Historical Data|\n|Netherlands Antilles*   |AHO |0         |12882.556130569325|N          |Olympic Historical Data|\n|East Timor (Timor-Leste)|TLS |1245015   |1157.99295590816  |E          |Olympic Historical Data|\n|Ethiopia                |ETH |99390750  |619.169406475891  |E          |Olympic Historical Data|\n|Burundi                 |BDI |11178921  |277.068309170914  |B          |Olympic Historical Data|\n|Cayman Islands*         |CAY |59967     |12882.556130569325|C          |Olympic Historical Data|\n|Kenya                   |KEN |46050302  |1376.71282894881  |K          |Olympic Historical Data|\n|Lithuania               |LTU |2910199   |14147.0493792403  |L          |Olympic Historical Data|\n|Burkina Faso            |BUR |18105570  |589.774414136617  |B          |Olympic Historical Data|\n|Sao Tome and Principe   |STP |190344    |1669.06326801326  |S          |Olympic Historical Data|\n|Somalia                 |SOM |10787104  |549.266976567576  |S          |Olympic Historical Data|\n|Dominica                |DMA |72680     |7116.38639189547  |D          |Olympic Historical Data|\n|Palau                   |PLW |21291     |13498.661406228   |P          |Olympic Historical Data|\n|Grenada                 |GRN |106825    |9212.02035173484  |G          |Olympic Historical Data|\n|Kyrgyzstan              |KGZ |5957000   |1103.2153515202   |K          |Olympic Historical Data|\n|Qatar                   |QAT |2235355   |73653.3944346574  |Q          |Olympic Historical Data|\n|Iraq                    |IRQ |36423395  |4943.76038832056  |I          |Olympic Historical Data|\n|American Samoa*         |ASA |55538     |12882.556130569325|A          |Olympic Historical Data|\n|Libya                   |LBA |6278438   |12882.556130569325|L          |Olympic Historical Data|\n|Mauritania              |MTN |4067564   |12882.556130569325|M          |Olympic Historical Data|\n|Namibia                 |NAM |2458830   |4673.56724769495  |N          |Olympic Historical Data|\n|Tajikistan              |TJK |8481855   |925.91188767081   |T          |Olympic Historical Data|\n|Tanzania                |TAN |53470420  |878.97510552608   |T          |Olympic Historical Data|\n|Cape Verde              |CPV |520502    |3080.17881445563  |C          |Olympic Historical Data|\n+------------------------+----+----------+------------------+-----------+-----------------------+\nonly showing top 100 rows\n\nVerifying 'silver_summer'...\n+----+---------------------+-------------+---------------+---------------------------------+-------+------+-----------------------------------+------+---------------+------------+-----------+-----------------------+\n|Year|City                 |Sport        |Discipline     |Athlete                          |Country|Gender|Event                              |Medal |Sport_Category |Century     |FirstLetter|Data_Source            |\n+----+---------------------+-------------+---------------+---------------------------------+-------+------+-----------------------------------+------+---------------+------------+-----------+-----------------------+\n|1904|St Louis             |Boxing       |Boxing         |Oliver L. Kirk                   |USA    |M     |52.16 - 56.7KG (Featherweight)     |Gold  |Other          |20th Century|U          |Olympic Historical Data|\n|1904|St Louis             |Lacrosse     |Lacrosse       |Sullivan                         |USA    |M     |Lacrosse                           |Silver|Other          |20th Century|U          |Olympic Historical Data|\n|1908|London               |Athletics    |Athletics      |Francis C. Irons                 |USA    |M     |Long Jump                          |Gold  |Track & Field  |20th Century|U          |Olympic Historical Data|\n|1908|London               |Cycling      |Cycling Track  |Benjamin Jones                   |GBR    |M     |1980 Yards Pursuit, Team           |Gold  |Track & Field  |20th Century|G          |Olympic Historical Data|\n|1908|London               |Hockey       |Hockey         |Eric Hubert Green                |GBR    |M     |Hockey                             |Gold  |Other          |20th Century|G          |Olympic Historical Data|\n|1908|London               |Hockey       |Hockey         |Robert L. Kennedy                |GBR    |M     |Hockey                             |Silver|Other          |20th Century|G          |Olympic Historical Data|\n|1908|London               |Lacrosse     |Lacrosse       |J. Fyon                          |CAN    |M     |Lacrosse                           |Gold  |Other          |20th Century|C          |Olympic Historical Data|\n|1908|London               |Skating      |Figure skating |Florence Syers                   |GBR    |F     |Pairs                              |Bronze|Other          |20th Century|G          |Olympic Historical Data|\n|1912|Stockholm            |Fencing      |Fencing        |Robert Cecil Montgomerie         |GBR    |M     |Épée Team                          |Silver|Other          |20th Century|G          |Olympic Historical Data|\n|1912|Stockholm            |Gymnastics   |Artistic G.    |Rikard Hannibal Wilhelm Nordström|DEN    |M     |Team, Free System                  |Bronze|Artistic Sports|20th Century|D          |Olympic Historical Data|\n|1912|Stockholm            |Gymnastics   |Artistic G.    |Bjarne Viktor Pettersen          |NOR    |M     |Team, Free System                  |Gold  |Artistic Sports|20th Century|N          |Olympic Historical Data|\n|1912|Stockholm            |Gymnastics   |Artistic G.    |Frithjof Saelen                  |NOR    |M     |Team, Free System                  |Gold  |Artistic Sports|20th Century|N          |Olympic Historical Data|\n|1912|Stockholm            |Shooting     |Shooting       |Johan Hübner Von Holst           |SWE    |M     |25M Rapid Fire Pistol (60 Shots)   |Bronze|Other          |20th Century|S          |Olympic Historical Data|\n|1912|Stockholm            |Shooting     |Shooting       |Amos De Kache                    |RU1    |M     |30M Army Pistol, Team              |Silver|Other          |20th Century|R          |Olympic Historical Data|\n|1920|Antwerp              |Aquatics     |Swimming       |Grace Mac Kenzie                 |GBR    |F     |4X100M Freestyle Relay             |Silver|Water Sports   |20th Century|G          |Olympic Historical Data|\n|1920|Antwerp              |Fencing      |Fencing        |Victor Boin                      |BEL    |M     |Épée Team                          |Silver|Other          |20th Century|B          |Olympic Historical Data|\n|1920|Antwerp              |Fencing      |Fencing        |Philippe Le Hardy De Beaulieu    |BEL    |M     |Épée Team                          |Silver|Other          |20th Century|B          |Olympic Historical Data|\n|1920|Antwerp              |Gymnastics   |Artistic G.    |Fernand Fauconnier               |FRA    |M     |Team Competition                   |Bronze|Artistic Sports|20th Century|F          |Olympic Historical Data|\n|1920|Antwerp              |Gymnastics   |Artistic G.    |Lorenzo Mangiante                |ITA    |M     |Team Competition                   |Gold  |Artistic Sports|20th Century|I          |Olympic Historical Data|\n|1920|Antwerp              |Gymnastics   |Artistic G.    |Théophile Bauer                  |BEL    |M     |Team Competition                   |Silver|Artistic Sports|20th Century|B          |Olympic Historical Data|\n|1920|Antwerp              |Gymnastics   |Artistic G.    |Frede Hansen                     |DEN    |M     |Team, Swedish System               |Silver|Artistic Sports|20th Century|D          |Olympic Historical Data|\n|1920|Antwerp              |Polo         |Polo           |Arthur Ringland Harris           |USA    |M     |Polo                               |Bronze|Other          |20th Century|U          |Olympic Historical Data|\n|1920|Antwerp              |Polo         |Polo           |Leopoldo De La Maza              |ESP    |M     |Polo                               |Silver|Other          |20th Century|E          |Olympic Historical Data|\n|1920|Antwerp              |Rowing       |Rowing         |Birger Var                       |NOR    |M     |Four-Oared Shell With Coxswain (4-)|Bronze|Other          |20th Century|N          |Olympic Historical Data|\n|1920|Antwerp              |Sailing      |Sailing        |Erik Örvig                       |NOR    |M     |12M (Rating 1919)                  |Gold  |Other          |20th Century|N          |Olympic Historical Data|\n|1920|Antwerp              |Sailing      |Sailing        |Bernard Carp                     |NED    |M     |6.5M (Rating 1919)                 |Gold  |Other          |20th Century|N          |Olympic Historical Data|\n|1920|Antwerp              |Sailing      |Sailing        |Thorleif Holbye                  |NOR    |M     |8M (Rating 1907)                   |Gold  |Other          |20th Century|N          |Olympic Historical Data|\n|1920|Antwerp              |Shooting     |Shooting       |Afranio Antonio Da Costa         |BRA    |M     |50M Pistol (60 Shots)              |Silver|Other          |20th Century|B          |Olympic Historical Data|\n|1924|Paris                |Aquatics     |Water polo     |Herbert Eberhard Vollmer         |USA    |M     |Water Polo                         |Bronze|Water Sports   |20th Century|U          |Olympic Historical Data|\n|1924|Paris                |Athletics    |Athletics      |Eero Berg                        |FIN    |M     |10000M                             |Bronze|Track & Field  |20th Century|F          |Olympic Historical Data|\n|1924|Paris                |Athletics    |Athletics      |S. Talja                         |FIN    |M     |3000M Team                         |Gold  |Track & Field  |20th Century|F          |Olympic Historical Data|\n|1924|Paris                |Rugby        |Rugby          |Theodor Marian                   |ROU    |M     |Rugby                              |Bronze|Other          |20th Century|R          |Olympic Historical Data|\n|1928|Amsterdam            |Athletics    |Athletics      |Mary T. Washburn                 |USA    |F     |4X100M Relay                       |Silver|Track & Field  |20th Century|U          |Olympic Historical Data|\n|1928|Amsterdam            |Fencing      |Fencing        |Ödön Tersztyanszky               |HUN    |M     |Sabre Team                         |Gold  |Other          |20th Century|H          |Olympic Historical Data|\n|1928|Amsterdam            |Hockey       |Hockey         |Gerd Strantzen                   |GER    |M     |Hockey                             |Bronze|Other          |20th Century|G          |Olympic Historical Data|\n|1932|Los Angeles          |Weightlifting|Weightlifting  |Gastone Pierini                  |ITA    |M     |60 - 67.5KG, Total (Lightweight)   |Bronze|Other          |20th Century|I          |Olympic Historical Data|\n|1936|Berlin               |Aquatics     |Diving         |Richard Kempster Degener         |USA    |M     |3M Springboard                     |Gold  |Water Sports   |20th Century|U          |Olympic Historical Data|\n|1936|Berlin               |Handball     |Handball       |Alois Schnabel                   |AUT    |M     |Handball                           |Silver|Other          |20th Century|A          |Olympic Historical Data|\n|1936|Berlin               |Rowing       |Rowing         |Enrico Garzelli                  |ITA    |M     |Eight With Coxswain (8+)           |Silver|Other          |20th Century|I          |Olympic Historical Data|\n|1936|Berlin               |Rowing       |Rowing         |Hans Homberger                   |SUI    |M     |Four-Oared Shell With Coxswain (4-)|Silver|Other          |20th Century|S          |Olympic Historical Data|\n|1948|London               |Basketball   |Basketball     |Robert Albert Kurland            |USA    |M     |Basketball                         |Gold  |Other          |20th Century|U          |Olympic Historical Data|\n|1948|London               |Fencing      |Fencing        |Edouard Artigas                  |FRA    |M     |Épée Team                          |Gold  |Other          |20th Century|F          |Olympic Historical Data|\n|1948|London               |Fencing      |Fencing        |Aladar Gerevich                  |HUN    |M     |Sabre Individual                   |Gold  |Other          |20th Century|H          |Olympic Historical Data|\n|1948|London               |Gymnastics   |Artistic G.    |Michael Reusch                   |SUI    |M     |Parallel Bars                      |Gold  |Artistic Sports|20th Century|S          |Olympic Historical Data|\n|1952|Helsinki             |Athletics    |Athletics      |Robert Mathias                   |USA    |M     |Decathlon                          |Gold  |Track & Field  |20th Century|U          |Olympic Historical Data|\n|1952|Helsinki             |Boxing       |Boxing         |Viktor Jörgensen                 |DEN    |M     |63.5 - 67KG (Welterweight)         |Bronze|Other          |20th Century|D          |Olympic Historical Data|\n|1952|Helsinki             |Canoe / Kayak|Canoe / Kayak F|Wilfried Soltau                  |GER    |M     |C-2 10000M                         |Bronze|Other          |20th Century|G          |Olympic Historical Data|\n|1952|Helsinki             |Gymnastics   |Artistic G.    |Viktor Ivanovich Chukarin        |URS    |M     |Team Competition                   |Gold  |Artistic Sports|20th Century|U          |Olympic Historical Data|\n|1952|Helsinki             |Hockey       |Hockey         |Derek Malcolm Day                |GBR    |M     |Hockey                             |Bronze|Other          |20th Century|G          |Olympic Historical Data|\n|1952|Helsinki             |Rowing       |Rowing         |Jiri Havlis                      |TCH    |M     |Four-Oared Shell With Coxswain (4-)|Gold  |Other          |20th Century|T          |Olympic Historical Data|\n|1952|Helsinki             |Sailing      |Sailing        |Magnus Wassen                    |SWE    |M     |5.5M                               |Bronze|Other          |20th Century|S          |Olympic Historical Data|\n|1956|Melbourne / Stockholm|Athletics    |Athletics      |Adhemar Ferreira Da Silva        |BRA    |M     |Triple Jump                        |Gold  |Track & Field  |20th Century|B          |Olympic Historical Data|\n|1956|Melbourne / Stockholm|Canoe / Kayak|Canoe / Kayak F|Lajos Kiss                       |HUN    |M     |K-1 1000M (Kayak Single)           |Bronze|Other          |20th Century|H          |Olympic Historical Data|\n|1956|Melbourne / Stockholm|Hockey       |Hockey         |Udham Singh Kullar               |IND    |M     |Hockey                             |Gold  |Other          |20th Century|I          |Olympic Historical Data|\n|1960|Rome                 |Aquatics     |Swimming       |Joan Arlene Spillane             |USA    |F     |4X100M Freestyle Relay             |Gold  |Water Sports   |20th Century|U          |Olympic Historical Data|\n|1960|Rome                 |Athletics    |Athletics      |Halina Herrmann-gorecka-richter  |POL    |F     |4X100M Relay                       |Bronze|Track & Field  |20th Century|P          |Olympic Historical Data|\n|1960|Rome                 |Basketball   |Basketball     |Lester E. Lane                   |USA    |M     |Basketball                         |Gold  |Other          |20th Century|U          |Olympic Historical Data|\n|1960|Rome                 |Gymnastics   |Artistic G.    |Adolfina Tacova-tkacikova        |TCH    |F     |Team Competition                   |Silver|Artistic Sports|20th Century|T          |Olympic Historical Data|\n|1960|Rome                 |Wrestling    |Wrestling Gre-R|Dinko Petrov Stoykov             |BUL    |M     |52 - 57KG (Bantamweight)           |Bronze|Other          |20th Century|B          |Olympic Historical Data|\n|1964|Tokyo                |Aquatics     |Diving         |Klaus Dibiasi                    |ITA    |M     |10M Platform                       |Silver|Water Sports   |20th Century|I          |Olympic Historical Data|\n|1964|Tokyo                |Aquatics     |Swimming       |Gary Steven Ilman                |USA    |M     |4X100M Freestyle Relay             |Gold  |Water Sports   |20th Century|U          |Olympic Historical Data|\n|1964|Tokyo                |Aquatics     |Swimming       |Kevin John Berry                 |AUS    |M     |4X100M Medley Relay                |Bronze|Water Sports   |20th Century|A          |Olympic Historical Data|\n|1964|Tokyo                |Equestrian   |Jumping        |Piero D'inzeo                    |ITA    |M     |Team                               |Bronze|Other          |20th Century|I          |Olympic Historical Data|\n|1964|Tokyo                |Hockey       |Hockey         |Robin Hodder                     |AUS    |M     |Hockey                             |Bronze|Other          |20th Century|A          |Olympic Historical Data|\n|1964|Tokyo\n\n*** WARNING: max output size exceeded, skipping output. ***\n\n         |Biathlon  |Biathlon                 |Evgeny Ustyugov               |RUS    |M     |15KM Mass Start      |Gold  |Other         |21st Century|R          |Olympic Historical Data|\n|2010|Vancouver             |Ice Hockey|Ice Hockey               |Linda Valimaki                |FIN    |F     |Ice Hockey           |Bronze|Winter Sports |21st Century|F          |Olympic Historical Data|\n|2010|Vancouver             |Skiing    |Freestyle Skiing         |Hedda Berntsen                |NOR    |F     |Ski Cross            |Silver|Winter Sports |21st Century|N          |Olympic Historical Data|\n|2010|Vancouver             |Skiing    |Snowboard                |Nicolien Sauerbreij           |NED    |F     |Giant Parallel Slalom|Gold  |Winter Sports |21st Century|N          |Olympic Historical Data|\n|2014|Sochi                 |Biathlon  |Biathlon                 |Darya Domracheva              |BLR    |F     |15KM                 |Gold  |Other         |21st Century|B          |Olympic Historical Data|\n|2014|Sochi                 |Skating   |Speed skating            |Olga Graf                     |RUS    |F     |3000M                |Bronze|Other         |21st Century|R          |Olympic Historical Data|\n|2014|Sochi                 |Skiing    |Ski Jumping              |Daiki Ito                     |JPN    |M     |Teams                |Bronze|Winter Sports |21st Century|J          |Olympic Historical Data|\n|1924|Chamonix              |Ice Hockey|Ice Hockey               |William Anderson              |GBR    |M     |Ice Hockey           |Bronze|Winter Sports |20th Century|G          |Olympic Historical Data|\n|1924|Chamonix              |Ice Hockey|Ice Hockey               |Albert Mac Caffery            |CAN    |M     |Ice Hockey           |Gold  |Winter Sports |20th Century|C          |Olympic Historical Data|\n|1928|St.Moritz             |Skating   |Speed skating            |Ivar Ballangrud               |NOR    |M     |1500M                |Bronze|Other         |20th Century|N          |Olympic Historical Data|\n|1964|Innsbruck             |Ice Hockey|Ice Hockey               |Boris Mayorov                 |URS    |M     |Ice Hockey           |Gold  |Winter Sports |20th Century|U          |Olympic Historical Data|\n|1968|Grenoble              |Biathlon  |Biathlon                 |Magnar Solberg                |NOR    |M     |20KM                 |Gold  |Other         |20th Century|N          |Olympic Historical Data|\n|1968|Grenoble              |Bobsleigh |Bobsleigh                |Erwin Thaler                  |AUT    |M     |Four-Man             |Silver|Winter Sports |20th Century|A          |Olympic Historical Data|\n|1968|Grenoble              |Luge      |Luge                     |Erica Lechner                 |ITA    |F     |Singles              |Gold  |Winter Sports |20th Century|I          |Olympic Historical Data|\n|1984|Sarajevo              |Skiing    |Ski Jumping              |Jens Weissflog                |GDR    |M     |K90 Individual (70M) |Gold  |Winter Sports |20th Century|G          |Olympic Historical Data|\n|1988|Calgary               |Skating   |Speed skating            |Bonnie Blair                  |USA    |F     |500M                 |Gold  |Other         |20th Century|U          |Olympic Historical Data|\n|1992|Albertville           |Bobsleigh |Bobsleigh                |Donat Acklin                  |SUI    |M     |Two-Man              |Gold  |Winter Sports |20th Century|S          |Olympic Historical Data|\n|1992|Albertville           |Ice Hockey|Ice Hockey               |David Archibald               |CAN    |M     |Ice Hockey           |Silver|Winter Sports |20th Century|C          |Olympic Historical Data|\n|1992|Albertville           |Skiing    |Alpine Skiing            |Katja Seizinger               |GER    |F     |Super-G              |Bronze|Winter Sports |20th Century|G          |Olympic Historical Data|\n|1994|Lillehammer           |Ice Hockey|Ice Hockey               |Janne Laukkanen               |FIN    |M     |Ice Hockey           |Bronze|Winter Sports |20th Century|F          |Olympic Historical Data|\n|1994|Lillehammer           |Ice Hockey|Ice Hockey               |Hannu Virta                   |FIN    |M     |Ice Hockey           |Bronze|Winter Sports |20th Century|F          |Olympic Historical Data|\n|1994|Lillehammer           |Skating   |Speed skating            |Rintje Ritsma                 |NED    |M     |5000M                |Bronze|Other         |20th Century|N          |Olympic Historical Data|\n|1998|Nagano                |Luge      |Luge                     |Angelika Neuner               |AUT    |F     |Singles              |Bronze|Winter Sports |20th Century|A          |Olympic Historical Data|\n|1998|Nagano                |Skating   |Short Track Speed Skating|Annie Perreault               |CAN    |F     |500M                 |Gold  |Other         |20th Century|C          |Olympic Historical Data|\n|1998|Nagano                |Skating   |Speed skating            |Bart Veldkamp                 |BEL    |M     |5000M                |Bronze|Other         |20th Century|B          |Olympic Historical Data|\n|2002|Salt Lake City        |Biathlon  |Biathlon                 |Frank Luck                    |GER    |M     |20KM                 |Silver|Other         |21st Century|G          |Olympic Historical Data|\n|2002|Salt Lake City        |Biathlon  |Biathlon                 |Katrin Apel                   |GER    |F     |4X7.5KM Relay        |Gold  |Other         |21st Century|G          |Olympic Historical Data|\n|2002|Salt Lake City        |Biathlon  |Biathlon                 |Uschi Disl                    |GER    |F     |7.5KM                |Silver|Other         |21st Century|G          |Olympic Historical Data|\n|2002|Salt Lake City        |Bobsleigh |Skeleton                 |Jim Shea                      |USA    |M     |Individual           |Gold  |Winter Sports |21st Century|U          |Olympic Historical Data|\n|2002|Salt Lake City        |Skating   |Speed skating            |Cindy Klassen                 |CAN    |F     |3000M                |Bronze|Other         |21st Century|C          |Olympic Historical Data|\n|2006|Turin                 |Skating   |Speed skating            |Anna Friesinger-postma        |GER    |F     |1000M                |Bronze|Other         |21st Century|G          |Olympic Historical Data|\n|2006|Turin                 |Skiing    |Alpine Skiing            |Alexandra Meissnitzer         |AUT    |F     |Super-G              |Bronze|Winter Sports |21st Century|A          |Olympic Historical Data|\n|2010|Vancouver             |Skating   |Short Track Speed Skating|Jessica Gregg                 |CAN    |F     |3000M Relay          |Silver|Other         |21st Century|C          |Olympic Historical Data|\n|2010|Vancouver             |Skating   |Short Track Speed Skating|Marianne St-gelais            |CAN    |F     |500M                 |Silver|Other         |21st Century|C          |Olympic Historical Data|\n|2014|Sochi                 |Curling   |Curling                  |Jill Officer                  |CAN    |F     |Curling              |Gold  |Other         |21st Century|C          |Olympic Historical Data|\n|2014|Sochi                 |Skating   |Speed skating            |Jan Szymanski                 |POL    |M     |Team Pursuit         |Bronze|Other         |21st Century|P          |Olympic Historical Data|\n|2014|Sochi                 |Skiing    |Ski Jumping              |Thomas Diethart               |AUT    |M     |Teams                |Silver|Winter Sports |21st Century|A          |Olympic Historical Data|\n|1932|Lake Placid           |Ice Hockey|Ice Hockey               |Walter Leinweber              |GER    |M     |Ice Hockey           |Bronze|Winter Sports |20th Century|G          |Olympic Historical Data|\n|1936|Garmisch Partenkirchen|Ice Hockey|Ice Hockey               |Paul Edward Rowe              |USA    |M     |Ice Hockey           |Bronze|Winter Sports |20th Century|U          |Olympic Historical Data|\n|1936|Garmisch Partenkirchen|Ice Hockey|Ice Hockey               |Herman Murray                 |CAN    |M     |Ice Hockey           |Silver|Winter Sports |20th Century|C          |Olympic Historical Data|\n+----+----------------------+----------+-------------------------+------------------------------+-------+------+---------------------+------+--------------+------------+-----------+-----------------------+\nonly showing top 100 rows\n\nVerifying 'silver_country'...\n+--------------------------------+-------+----------+------------------+-----------+-----------------------+\n|CountryName                     |NOCCode|Population|GDP               |FirstLetter|Data_Source            |\n+--------------------------------+-------+----------+------------------+-----------+-----------------------+\n|Poland                          |POL    |37999494  |12554.5475536313  |P          |Olympic Historical Data|\n|Syria                           |SYR    |18502413  |12882.556130569325|S          |Olympic Historical Data|\n|Gabon                           |GAB    |1725292   |8266.4456050624   |G          |Olympic Historical Data|\n|Portugal                        |POR    |10348648  |19222.1500764153  |P          |Olympic Historical Data|\n|Pakistan                        |PAK    |188924874 |1434.69666504969  |P          |Olympic Historical Data|\n|United Kingdom                  |GBR    |65138232  |43875.9696143686  |U          |Olympic Historical Data|\n|Cayman Islands*                 |CAY    |59967     |12882.556130569325|C          |Olympic Historical Data|\n|Tajikistan                      |TJK    |8481855   |925.91188767081   |T          |Olympic Historical Data|\n|Liechtenstein                   |LIE    |37531     |12882.556130569325|L          |Olympic Historical Data|\n|Malaysia                        |MAS    |30331007  |9768.32686011881  |M          |Olympic Historical Data|\n|Guinea                          |GUI    |12608590  |531.320595188714  |G          |Olympic Historical Data|\n|Indonesia                       |INA    |257563815 |3346.48703949478  |I          |Olympic Historical Data|\n|Afghanistan                     |AFG    |32526562  |594.323081219966  |A          |Olympic Historical Data|\n|Malawi                          |MAW    |17215232  |371.985747810344  |M          |Olympic Historical Data|\n|Panama                          |PAN    |3929141   |13268.1137549335  |P          |Olympic Historical Data|\n|Jordan                          |JOR    |7594547   |4940.04583574111  |J          |Olympic Historical Data|\n|Solomon Islands                 |SOL    |583591    |1934.85629287353  |S          |Olympic Historical Data|\n|Chile                           |CHI    |17948141  |13416.2300390185  |C          |Olympic Historical Data|\n|Malta                           |MLT    |431333    |22596.1817742659  |M          |Olympic Historical Data|\n|Iraq                            |IRQ    |36423395  |4943.76038832056  |I          |Olympic Historical Data|\n|Romania                         |ROM    |19832389  |8972.92251840971  |R          |Olympic Historical Data|\n|Denmark                         |DEN    |5676002   |51989.2934712354  |D          |Olympic Historical Data|\n|Senegal                         |SEN    |15129273  |899.579879484977  |S          |Olympic Historical Data|\n|Central African Republic        |CAF    |4900274   |323.201674024141  |C          |Olympic Historical Data|\n|Laos                            |LAO    |6802023   |1818.44137293236  |L          |Olympic Historical Data|\n|Jamaica                         |JAM    |2725941   |5232.02458271187  |J          |Olympic Historical Data|\n|Grenada                         |GRN    |106825    |9212.02035173484  |G          |Olympic Historical Data|\n|Slovakia                        |SVK    |5424050   |16088.2775872723  |S          |Olympic Historical Data|\n|Eritrea                         |ERI    |0         |12882.556130569325|E          |Olympic Historical Data|\n|Sudan                           |SUD    |40234882  |2414.72360102858  |S          |Olympic Historical Data|\n|Madagascar                      |MAD    |24235390  |401.836006029745  |M          |Olympic Historical Data|\n|Monaco                          |MON    |37731     |12882.556130569325|M          |Olympic Historical Data|\n|Tunisia                         |TUN    |11107800  |3872.51208364171  |T          |Olympic Historical Data|\n|Sao Tome and Principe           |STP    |190344    |1669.06326801326  |S          |Olympic Historical Data|\n|Slovenia                        |SLO    |2063768   |20726.5398863708  |S          |Olympic Historical Data|\n|Guatemala                       |GUA    |16342897  |3903.47885604613  |G          |Olympic Historical Data|\n|Angola                          |ANG    |25021974  |4101.47215182964  |A          |Olympic Historical Data|\n|Dominica                        |DMA    |72680     |7116.38639189547  |D          |Olympic Historical Data|\n|Canada                          |CAN    |35851774  |43248.529909341   |C          |Olympic Historical Data|\n|Palestine, Occupied Territories |PLE    |0         |12882.556130569325|P          |Olympic Historical Data|\n|Germany                         |GER    |81413145  |41313.3139945434  |G          |Olympic Historical Data|\n|Italy                           |ITA    |60802085  |29957.8043154372  |I          |Olympic Historical Data|\n|Belize                          |BIZ    |359287    |4878.72126724745  |B          |Olympic Historical Data|\n|Uzbekistan                      |UZB    |31299500  |2132.07036847857  |U          |Olympic Historical Data|\n|Argentina                       |ARG    |43416755  |13431.8783398577  |A          |Olympic Historical Data|\n|Nauru                           |NRU    |10222     |9827.54428148233  |N          |Olympic Historical Data|\n|Togo                            |TOG    |7304578   |559.635876661945  |T          |Olympic Historical Data|\n|Morocco                         |MAR    |34377511  |2878.20134215919  |M          |Olympic Historical Data|\n|Cape Verde                      |CPV    |520502    |3080.17881445563  |C          |Olympic Historical Data|\n|British Virgin Islands          |IVB    |30117     |12882.556130569325|B          |Olympic Historical Data|\n|Congo, Dem Rep                  |COD    |77266814  |456.052740548027  |C          |Olympic Historical Data|\n|Gambia                          |GAM    |1990924   |471.537195472347  |G          |Olympic Historical Data|\n|Switzerland                     |SUI    |8286976   |80945.0792194742  |S          |Olympic Historical Data|\n|Vietnam                         |VIE    |91703800  |2111.13802366815  |V          |Olympic Historical Data|\n|Ecuador                         |ECU    |16144363  |6205.06414529951  |E          |Olympic Historical Data|\n|Saint Lucia                     |LCA    |184999    |7735.91048440102  |S          |Olympic Historical Data|\n|Samoa                           |SAM    |193228    |3938.54884570316  |S          |Olympic Historical Data|\n|Benin                           |BEN    |10879829  |762.051205441965  |B          |Olympic Historical Data|\n|Sweden                          |SWE    |9798871   |50579.6736486777  |S          |Olympic Historical Data|\n|Kuwait                          |KUW    |3892115   |29300.5755750333  |K          |Olympic Historical Data|\n|Burma                           |MYA    |53897154  |1161.48815791087  |B          |Olympic Historical Data|\n|Lebanon                         |LIB    |5850743   |8047.64508557496  |L          |Olympic Historical Data|\n|Costa Rica                      |CRC    |4807850   |11260.0921598775  |C          |Olympic Historical Data|\n|Fiji                            |FIJ    |892145    |4960.51995438419  |F          |Olympic Historical Data|\n|Aruba*                          |ARU    |103889    |12882.556130569325|A          |Olympic Historical Data|\n|Singapore                       |SIN    |5535002   |52888.7446717529  |S          |Olympic Historical Data|\n|Uruguay                         |URU    |3431555   |15573.9009191818  |U          |Olympic Historical Data|\n|Hong Kong*                      |HKG    |7305700   |42327.8399570345  |H          |Olympic Historical Data|\n|Lesotho                         |LES    |2135022   |1066.98562625017  |L          |Olympic Historical Data|\n|Saudi Arabia                    |KSA    |31540372  |20481.7453220484  |S          |Olympic Historical Data|\n|Cyprus                          |CYP    |1165300   |23242.8400685313  |C          |Olympic Historical Data|\n|Swaziland                       |SWZ    |1286970   |3200.14301756487  |S          |Olympic Historical Data|\n|Bhutan                          |BHU    |774830    |2655.99889161858  |B          |Olympic Historical Data|\n|Nepal                           |NEP    |28513700  |743.322965726435  |N          |Olympic Historical Data|\n|Chad                            |CHA    |14037472  |775.695090525313  |C          |Olympic Historical Data|\n|Palau                           |PLW    |21291     |13498.661406228   |P          |Olympic Historical Data|\n|Russia                          |RUS    |144096812 |9092.58053606884  |R          |Olympic Historical Data|\n|Comoros                         |COM    |788474    |717.448849960912  |C          |Olympic Historical Data|\n|Nicaragua                       |NCA    |6082032   |2086.89500277099  |N          |Olympic Historical Data|\n|Turkey                          |TUR    |78665830  |9125.68758972936  |T          |Olympic Historical Data|\n|Libya                           |LBA    |6278438   |12882.556130569325|L          |Olympic Historical Data|\n|Seychelles                      |SEY    |92900     |15476.01944443    |S          |Olympic Historical Data|\n|Kazakhstan                      |KAZ    |17544126  |10509.9810699442  |K          |Olympic Historical Data|\n|Cote d'Ivoire                   |CIV    |22701556  |1398.98995768413  |C          |Olympic Historical Data|\n|Saint Vincent and the Grenadines|VIN    |109462    |6739.17483286945  |S          |Olympic Historical Data|\n|United States                   |USA    |321418820 |56115.7184261955  |U          |Olympic Historical Data|\n|Maldives                        |MDV    |409163    |8395.78519750383  |M          |Olympic Historical Data|\n|Micronesia                      |FSM    |104460    |3015.23166762397  |M          |Olympic Historical Data|\n|Suriname                        |SUR    |542975    |9485.31924429496  |S          |Olympic Historical Data|\n|Somalia                         |SOM    |10787104  |549.266976567576  |S          |Olympic Historical Data|\n|Algeria                         |ALG    |39666519  |4206.03123244958  |A          |Olympic Historical Data|\n|Hungary                         |HUN    |9844686   |12363.5434596539  |H          |Olympic Historical Data|\n|South Africa                    |RSA    |54956920  |5723.97335690212  |S          |Olympic Historical Data|\n|Liberia                         |LBR    |4503438   |455.873934536237  |L          |Olympic Historical Data|\n|Mauritius                       |MRI    |1262605   |9252.11072429051  |M          |Olympic Historical Data|\n|Philippines                     |PHI    |100699395 |2904.20208191528  |P          |Olympic Historical Data|\n|Sri Lanka                       |SRI    |20966000  |3926.17439589454  |S          |Olympic Historical Data|\n|Guyana                          |GUY    |767085    |4127.35101806198  |G          |Olympic Historical Data|\n|Cameroon                        |CMR    |23344179  |1217.26067048427  |C          |Olympic Historical Data|\n|Japan                           |JPN    |126958472 |32477.2151449234  |J          |Olympic Historical Data|\n+--------------------------------+-------+----------+------------------+-----------+-----------------------+\nonly showing top 100 rows\n\nVerifying 'silver_athlete'...\n+---------+-----------------------------+------+\n|AthleteID|Name                         |Gender|\n+---------+-----------------------------+------+\n|1        |- Johnson                    |M     |\n|2        |..... Daumain                |M     |\n|3        |A Lam Shin                   |F     |\n|4        |A. Albert                    |M     |\n|5        |A. B. Zumelzu                |M     |\n|6        |A. Bögli                     |M     |\n|7        |A. Eskelinen                 |M     |\n|8        |A. Faehlmann                 |M     |\n|9        |A. Fasani                    |M     |\n|10       |A. Fauquet Lemaitre          |M     |\n|11       |A. Ferraris                  |M     |\n|12       |A. Gilpin                    |M     |\n|13       |A. Guerrier                  |M     |\n|14       |A. Haslam                    |M     |\n|15       |A. Helman                    |M     |\n|16       |A. Henry Thomas              |M     |\n|17       |A. Lawrey                    |M     |\n|18       |A. Mara                      |M     |\n|19       |A. Mariacher                 |M     |\n|20       |A. Mcevoy                    |M     |\n|21       |A. Melogno                   |M     |\n|22       |A. Pena                      |M     |\n|23       |A. Rieger                    |M     |\n|24       |A. Sihvola                   |M     |\n|25       |A. Viviano                   |M     |\n|26       |A. Willcocks                 |M     |\n|27       |A.h. Venn                    |M     |\n|28       |A.j. Hinch                   |M     |\n|29       |A.j. Schneidau               |M     |\n|30       |Aage Birch                   |M     |\n|31       |Aage Ernst Larsen            |M     |\n|32       |Aage Ingvar Eriksen          |M     |\n|33       |Aage Jörgensen               |M     |\n|34       |Aage Marius Hansen           |M     |\n|35       |Aage Valdemar Harald Frandsen|M     |\n|36       |Aage Walther                 |M     |\n|37       |Aagje Ada Kok                |F     |\n|38       |Aarne Eemeli Reini           |M     |\n|39       |Aarne Pelkonen               |M     |\n|40       |Aarne Pohjonen               |M     |\n|41       |Aarne Salovaara              |M     |\n|42       |Aaron Egbele                 |M     |\n|43       |Aaron Gate                   |M     |\n|44       |Aaron Mcintosh               |M     |\n|45       |Aaron Miller                 |M     |\n|46       |Aaron Nguimbat               |M     |\n|47       |Aaron Peirsol                |M     |\n|48       |Aaron Ross Flood             |M     |\n|49       |Aatos Tuomas Jaskari         |M     |\n|50       |Aavo Pikkuus                 |M     |\n|51       |Abaz Arslanagic              |M     |\n|52       |Abbas Jadidi                 |M     |\n|53       |Abbos Atoev                  |M     |\n|54       |Abby Bishop                  |F     |\n|55       |Abby Wambach                 |F     |\n|56       |Abdalaati Iguider            |M     |\n|57       |Abdel Aal Ahmed Rashed       |M     |\n|58       |Abdel Moneim El Gindy        |M     |\n|59       |Abdelhak Achik               |M     |\n|60       |Abderrahmane Hammad          |M     |\n|61       |Abdesiem Rhadi Ben Abdesselem|M     |\n|62       |Abdollah Modjtabavi          |M     |\n|63       |Abdollah Movahed-ardabili    |M     |\n|64       |Abdon Pamich                 |M     |\n|65       |Abdoulaye Seye               |M     |\n|66       |Abdul Wahid Aziz             |M     |\n|67       |Abdullah Waleed Sharbatly    |M     |\n|68       |Abdullo Tangriev             |M     |\n|69       |Abebe Bikila                 |M     |\n|70       |Abel Kiprop Mutai            |M     |\n|71       |Abel Kirui                   |M     |\n|72       |Abel Kiviat                  |M     |\n|73       |Abel Ricardo Laudonio        |M     |\n|74       |Abelardo Fernandez Antuña    |M     |\n|75       |Abelardo Olivier             |M     |\n|76       |Abhinav Bindra               |M     |\n|77       |Abigail Johnston             |F     |\n|78       |Abiodon Obafemi              |M     |\n|79       |Abraham Charite              |M     |\n|80       |Abraham Kurland              |M     |\n|81       |Abraham Olano                |M     |\n|82       |Abramo Albini                |M     |\n|83       |Abutaleb Gorgori             |M     |\n|84       |Ace Rusevski                 |M     |\n|85       |Acer Nethercott              |M     |\n|86       |Achille C. M. Tribouillet    |M     |\n|87       |Achille Paroche              |M     |\n|88       |Achille Piccini              |M     |\n|89       |Achille Souchard             |M     |\n|90       |Achim Hill                   |M     |\n|91       |Ada Smith                    |F     |\n|92       |Adalberts Bubenko            |M     |\n|93       |Adam Commens                 |M     |\n|94       |Adam Deadmarsh               |M     |\n|95       |Adam Enright                 |M     |\n|96       |Adam Everett                 |M     |\n|97       |Adam Foote                   |M     |\n|98       |Adam Gunn                    |M     |\n|99       |Adam Korol                   |M     |\n|100      |Adam Kreek                   |M     |\n+---------+-----------------------------+------+\nonly showing top 100 rows\n\n"
     ]
    }
   ],
   "source": [
    "# Comprehensive Silver Layer Transformation Script\n",
    "\n",
    "# Import required libraries\n",
    "from pyspark.sql.functions import (\n",
    "    col, trim, when, lit, avg, upper, substring, split, concat_ws, initcap, regexp_replace, row_number\n",
    ")\n",
    "from pyspark.sql.utils import AnalysisException\n",
    "from pyspark.sql.window import Window\n",
    "\n",
    "# Helper function to check table existence\n",
    "def table_exists(table_name):\n",
    "    try:\n",
    "        spark.read.table(table_name)\n",
    "        return True\n",
    "    except AnalysisException:\n",
    "        return False\n",
    "\n",
    "# Enhanced Silver Layer Processing Function\n",
    "def process_silver_layer_enhanced(bronze_table, silver_table):\n",
    "    # Read Bronze layer data\n",
    "    df = spark.read.format(\"delta\").table(bronze_table)\n",
    "\n",
    "    # ------------------ Data Cleansing ------------------\n",
    "    # Trim whitespace from string columns\n",
    "    for column in df.columns:\n",
    "        df = df.withColumn(column, trim(col(column)))\n",
    "\n",
    "    # ------------------ Data Standardization ------------------\n",
    "    # Standardize Gender Column\n",
    "    if \"Gender\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Gender\",\n",
    "            when(col(\"Gender\").isin(\"Men\", \"M\"), \"M\")\n",
    "            .when(col(\"Gender\").isin(\"Women\", \"F\"), \"F\")\n",
    "            .otherwise(\"Unknown\")\n",
    "        )\n",
    "\n",
    "    # Standardize Medal Column\n",
    "    if \"Medal\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Medal\",\n",
    "            when(col(\"Medal\").isin([\"Gold\", \"Silver\", \"Bronze\"]), col(\"Medal\"))\n",
    "            .otherwise(\"Unknown\")\n",
    "        )\n",
    "\n",
    "    # Athlete Name Standardization: \"Last, First\" to \"First Last\" and remove special chars\n",
    "    if \"Athlete\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Athlete\",\n",
    "            when(col(\"Athlete\").contains(\",\"),\n",
    "                concat_ws(\n",
    "                    \" \",\n",
    "                    initcap(trim(split(col(\"Athlete\"), \",\")[1])),\n",
    "                    initcap(trim(split(col(\"Athlete\"), \",\")[0]))\n",
    "                )\n",
    "            ).otherwise(initcap(regexp_replace(col(\"Athlete\"), \"[^a-zA-Z\\s]\", \"\")))\n",
    "        )\n",
    "\n",
    "    # ------------------ Data Normalization ------------------\n",
    "    if \"Sport\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Sport_Category\",\n",
    "            when(col(\"Sport\").isin([\"Aquatics\", \"Swimming\", \"Water polo\"]), \"Water Sports\")\n",
    "            .when(col(\"Sport\").isin([\"Athletics\", \"Track\", \"Cycling\"]), \"Track & Field\")\n",
    "            .when(col(\"Sport\").isin([\"Skiing\", \"Ice Hockey\", \"Bobsleigh\", \"Luge\"]), \"Winter Sports\")\n",
    "            .when(col(\"Sport\") == \"Gymnastics\", \"Artistic Sports\")\n",
    "            .otherwise(\"Other\")\n",
    "        )\n",
    "\n",
    "    # ------------------ Derived Columns ------------------\n",
    "    if \"Year\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Century\",\n",
    "            when(col(\"Year\") < 2000, \"20th Century\").otherwise(\"21st Century\")\n",
    "        )\n",
    "\n",
    "    if \"Country\" in df.columns:\n",
    "        df = df.withColumn(\"FirstLetter\", upper(substring(col(\"Country\"), 1, 1)))\n",
    "\n",
    "    # ------------------ Handle Missing Values ------------------\n",
    "    if \"GDP_per_Capita\" in df.columns:\n",
    "        avg_gdp = df.select(avg(col(\"GDP_per_Capita\"))).collect()[0][0]\n",
    "        df = df.withColumn(\n",
    "            \"GDP_per_Capita\",\n",
    "            when(col(\"GDP_per_Capita\").isNull(), avg_gdp)\n",
    "            .otherwise(col(\"GDP_per_Capita\"))\n",
    "        )\n",
    "\n",
    "    if \"Population\" in df.columns:\n",
    "        df = df.withColumn(\n",
    "            \"Population\",\n",
    "            when(col(\"Population\").isNull() | (col(\"Population\") < 0), 0)\n",
    "            .otherwise(col(\"Population\").cast(\"long\"))\n",
    "        )\n",
    "\n",
    "    if \"Code\" in df.columns:\n",
    "        df = df.withColumn(\"Code\", when(col(\"Code\") == \"ZZX\", \"Unknown\").otherwise(col(\"Code\")))\n",
    "\n",
    "    # ------------------ Data Enrichment ------------------\n",
    "    df = df.withColumn(\"Data_Source\", lit(\"Olympic Historical Data\"))\n",
    "\n",
    "    # ------------------ Removing Duplicates ------------------\n",
    "    df = df.dropDuplicates()\n",
    "\n",
    "    # ------------------ Write to Silver Layer ------------------\n",
    "    df.write.format(\"delta\") \\\n",
    "        .mode(\"overwrite\") \\\n",
    "        .option(\"overwriteSchema\", \"true\") \\\n",
    "        .saveAsTable(silver_table)\n",
    "\n",
    "    print(f\"Table '{silver_table}' processed successfully.\")\n",
    "\n",
    "# Process Bronze → Silver tables\n",
    "process_silver_layer_enhanced(\"bronze_dictionary\", \"silver_dictionary\")\n",
    "process_silver_layer_enhanced(\"bronze_summer\", \"silver_summer\")\n",
    "process_silver_layer_enhanced(\"bronze_winter\", \"silver_winter\")\n",
    "\n",
    "# ------------------ Create 'silver_country' ------------------\n",
    "if table_exists(\"silver_dictionary\"):\n",
    "    df_country = spark.read.table(\"silver_dictionary\")\n",
    "\n",
    "    df_country = df_country.select(\n",
    "        col(\"Country\").alias(\"CountryName\"),\n",
    "        col(\"Code\").alias(\"NOCCode\"),\n",
    "        col(\"Population\"),\n",
    "        col(\"GDP_per_Capita\").alias(\"GDP\"),\n",
    "        col(\"FirstLetter\"),\n",
    "        col(\"Data_Source\")\n",
    "    ).dropDuplicates()\n",
    "\n",
    "    df_country.write.format(\"delta\") \\\n",
    "        .mode(\"overwrite\") \\\n",
    "        .option(\"overwriteSchema\", \"true\") \\\n",
    "        .saveAsTable(\"silver_country\")\n",
    "\n",
    "    print(\"Table 'silver_country' processed successfully.\")\n",
    "else:\n",
    "    print(\"Table 'silver_dictionary' not found.\")\n",
    "\n",
    "# ------------------ Create 'silver_athlete' ------------------\n",
    "silver_athlete_df = spark.table(\"silver_summer\").select(\"Athlete\", \"Gender\") \\\n",
    "    .union(spark.table(\"silver_winter\").select(\"Athlete\", \"Gender\")) \\\n",
    "    .distinct() \\\n",
    "    .withColumnRenamed(\"Athlete\", \"Name\") \\\n",
    "    .withColumn(\"AthleteID\", lit(None).cast(\"int\"))\n",
    "\n",
    "# Assign unique AthleteID\n",
    "windowSpec = Window.orderBy(\"Name\")\n",
    "silver_athlete_df = silver_athlete_df.withColumn(\"AthleteID\", row_number().over(windowSpec))\n",
    "\n",
    "silver_athlete_df.select(\"AthleteID\", \"Name\", \"Gender\").write.format(\"delta\") \\\n",
    "    .mode(\"overwrite\") \\\n",
    "    .option(\"overwriteSchema\", \"true\") \\\n",
    "    .saveAsTable(\"silver_athlete\")\n",
    "\n",
    "print(\"Table 'silver_athlete' processed successfully.\")\n",
    "\n",
    "# ------------------ Verify Silver Tables ------------------\n",
    "tables = [\n",
    "    \"silver_dictionary\",\n",
    "    \"silver_summer\",\n",
    "    \"silver_winter\",\n",
    "    \"silver_country\",\n",
    "    \"silver_athlete\"\n",
    "]\n",
    "\n",
    "for table in tables:\n",
    "    if table_exists(table):\n",
    "        print(f\"Verifying '{table}'...\")\n",
    "        spark.table(table).show(100, truncate=False)\n",
    "    else:\n",
    "        print(f\"Table '{table}' does not exist. Please check previous steps.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ccf6bac0-4fee-4bfd-84da-0c4472252e32",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table 'silver_athlete' processed successfully with duplicate removal.\n"
     ]
    }
   ],
   "source": [
    "# ------------------ Create 'silver_athlete' with Duplicate Removal ------------------\n",
    "from pyspark.sql.window import Window\n",
    "from pyspark.sql.functions import row_number, lower, trim, col\n",
    "\n",
    "# Union athletes from both summer and winter, standardize names to avoid duplicates\n",
    "silver_athlete_df = spark.table(\"silver_summer\").select(\"Athlete\", \"Gender\") \\\n",
    "    .union(spark.table(\"silver_winter\").select(\"Athlete\", \"Gender\")) \\\n",
    "    .withColumn(\"Name_Clean\", lower(trim(col(\"Athlete\")))) \\\n",
    "    .dropDuplicates([\"Name_Clean\", \"Gender\"]) \\\n",
    "    .withColumnRenamed(\"Athlete\", \"Name\")\n",
    "\n",
    "# Assign unique AthleteID after deduplication\n",
    "windowSpec = Window.orderBy(\"Name\")\n",
    "silver_athlete_df = silver_athlete_df.withColumn(\"AthleteID\", row_number().over(windowSpec))\n",
    "\n",
    "# Final select for athlete table\n",
    "silver_athlete_df.select(\"AthleteID\", \"Name\", \"Gender\") \\\n",
    "    .write.format(\"delta\") \\\n",
    "    .mode(\"overwrite\") \\\n",
    "    .option(\"overwriteSchema\", \"true\") \\\n",
    "    .saveAsTable(\"silver_athlete\")\n",
    "\n",
    "print(\"Table 'silver_athlete' processed successfully with duplicate removal.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "43664114-3ae0-4be2-9e66-0b636ca35a9f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table 'silver_dictionary' has 201 rows.\nTable 'silver_summer' has 31163 rows.\nTable 'silver_winter' has 5770 rows.\nTable 'silver_country' has 201 rows.\nTable 'silver_athlete' has 26494 rows.\n"
     ]
    }
   ],
   "source": [
    "tables = ['silver_dictionary', 'silver_summer', 'silver_winter', 'silver_country', 'silver_athlete']\n",
    "for tbl in tables:\n",
    "    count = spark.table(tbl).count()\n",
    "    print(f\"Table '{tbl}' has {count} rows.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "428d930a-fa33-490a-a124-2ce087993a96",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table 'silver_dictionary' has 0 duplicate rows.\nTable 'silver_summer' has 0 duplicate rows.\nTable 'silver_winter' has 0 duplicate rows.\nTable 'silver_country' has 0 duplicate rows.\nTable 'silver_athlete' has 0 duplicate rows.\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import count\n",
    "\n",
    "for tbl in tables:\n",
    "    duplicates = spark.table(tbl).groupBy(spark.table(tbl).columns)\\\n",
    "                   .count().filter(\"count > 1\").count()\n",
    "    print(f\"Table '{tbl}' has {duplicates} duplicate rows.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "7c9f3406-687f-4158-bb7d-2c165699c16b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NULL check for 'silver_dictionary':\n+-------+----+----------+--------------+-----------+-----------+\n|Country|Code|Population|GDP_per_Capita|FirstLetter|Data_Source|\n+-------+----+----------+--------------+-----------+-----------+\n|      0|   0|         0|             0|          0|          0|\n+-------+----+----------+--------------+-----------+-----------+\n\nNULL check for 'silver_summer':\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n|Year|City|Sport|Discipline|Athlete|Country|Gender|Event|Medal|Sport_Category|Century|FirstLetter|Data_Source|\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n|   0|   0|    0|         0|      0|      4|     0|    0|    0|             0|      0|          4|          0|\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n\nNULL check for 'silver_winter':\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n|Year|City|Sport|Discipline|Athlete|Country|Gender|Event|Medal|Sport_Category|Century|FirstLetter|Data_Source|\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n|   0|   0|    0|         0|      0|      0|     0|    0|    0|             0|      0|          0|          0|\n+----+----+-----+----------+-------+-------+------+-----+-----+--------------+-------+-----------+-----------+\n\nNULL check for 'silver_country':\n+-----------+-------+----------+---+-----------+-----------+\n|CountryName|NOCCode|Population|GDP|FirstLetter|Data_Source|\n+-----------+-------+----------+---+-----------+-----------+\n|          0|      0|         0|  0|          0|          0|\n+-----------+-------+----------+---+-----------+-----------+\n\nNULL check for 'silver_athlete':\n+---------+----+------+\n|AthleteID|Name|Gender|\n+---------+----+------+\n|        0|   0|     0|\n+---------+----+------+\n\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import col, sum\n",
    "\n",
    "def null_counts(df):\n",
    "    return df.select([sum(col(c).isNull().cast(\"int\")).alias(c) for c in df.columns])\n",
    "\n",
    "for tbl in tables:\n",
    "    print(f\"NULL check for '{tbl}':\")\n",
    "    null_counts(spark.table(tbl)).show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "7e9ade81-0c2a-4edc-9c11-90136fe1610b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------+-----+\n| Medal|count|\n+------+-----+\n|  Gold|10484|\n|Bronze|10369|\n|Silver|10310|\n+------+-----+\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_summer\")\\\n",
    "     .groupBy(\"Medal\")\\\n",
    "     .count()\\\n",
    "     .orderBy(\"count\", ascending=False)\\\n",
    "     .show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c20a2408-4d06-4e2c-a24e-1cc4a36b52a3",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------+-----+\n|Gender|count|\n+------+-----+\n|     M|19592|\n|     F| 6902|\n+------+-----+\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_athlete\")\\\n",
    "     .groupBy(\"Gender\")\\\n",
    "     .count()\\\n",
    "     .orderBy(\"count\", ascending=False)\\\n",
    "     .show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "cf282e33-dacc-43a1-bedf-3d28afcc6587",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+-----+\n|     Century|count|\n+------------+-----+\n|20th Century|23160|\n|21st Century| 8003|\n+------------+-----+\n\n+------------+-----+\n|     Century|count|\n+------------+-----+\n|20th Century| 3617|\n|21st Century| 2153|\n+------------+-----+\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_summer\")\\\n",
    "     .groupBy(\"Century\")\\\n",
    "     .count()\\\n",
    "     .orderBy(\"Century\")\\\n",
    "     .show()\n",
    "\n",
    "spark.table(\"silver_winter\")\\\n",
    "     .groupBy(\"Century\")\\\n",
    "     .count()\\\n",
    "     .orderBy(\"Century\")\\\n",
    "     .show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3f7225a4-bf8c-4e65-903f-ef5f9a8d8ea9",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------------+-----+\n| Sport_Category|count|\n+---------------+-----+\n|          Other|19916|\n|  Track & Field| 4743|\n|   Water Sports| 4170|\n|Artistic Sports| 2307|\n|  Winter Sports|   27|\n+---------------+-----+\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_summer\")\\\n",
    "     .groupBy(\"Sport_Category\")\\\n",
    "     .count()\\\n",
    "     .orderBy(\"count\", ascending=False)\\\n",
    "     .show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "168b6538-9ca9-45bc-ba12-4c35643b6874",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----------+----------------+----------+\n|CountryName|GDP             |Population|\n+-----------+----------------+----------+\n|Nauru      |9827.54428148233|10222     |\n|Malaysia   |9768.32686011881|30331007  |\n|Suriname   |9485.31924429496|542975    |\n|Mauritius  |9252.11072429051|1262605   |\n|Tajikistan |925.91188767081 |8481855   |\n|Zimbabwe   |924.143819253412|15602751  |\n|Grenada    |9212.02035173484|106825    |\n|Turkey     |9125.68758972936|78665830  |\n|Russia     |9092.58053606884|144096812 |\n|Mexico     |9005.02426497766|127017224 |\n+-----------+----------------+----------+\nonly showing top 10 rows\n\n+-------------+----------+\n|CountryName  |Population|\n+-------------+----------+\n|China        |1371220000|\n|India        |1311050527|\n|United States|321418820 |\n|Indonesia    |257563815 |\n|Brazil       |207847528 |\n|Pakistan     |188924874 |\n|Nigeria      |182201962 |\n|Bangladesh   |160995642 |\n|Russia       |144096812 |\n|Mexico       |127017224 |\n+-------------+----------+\nonly showing top 10 rows\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_country\")\\\n",
    "     .select(\"CountryName\", \"GDP\", \"Population\")\\\n",
    "     .orderBy(col(\"GDP\").desc())\\\n",
    "     .show(10, truncate=False)\n",
    "\n",
    "spark.table(\"silver_country\")\\\n",
    "     .select(\"CountryName\", \"Population\")\\\n",
    "     .orderBy(col(\"Population\").desc())\\\n",
    "     .show(10, truncate=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b811c4fa-7637-44ca-8c74-7e2d7d68ae1b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------------------------+\n|Name                       |\n+---------------------------+\n|Cheong-shim Kim            |\n|Chil-sung Chun             |\n|Birte Christoffersen-hanson|\n|Anne-caroline Chausson     |\n|Badar-uugan Enkhbat        |\n|Charles Macleod-robertson  |\n|Chen-jung Lo               |\n|Christian Due-boje         |\n|Caroline Evers-swindell    |\n|..... Daumain              |\n|Beatriz Ferrer-salat       |\n|Borislava Ivanova-milkova  |\n|Carl-erik Svensson         |\n|Catherine Fleury-vachon    |\n|Bruno Marie-rose           |\n|Carl-friedrich Von Langen  |\n|Byung-kwan Chun            |\n|B.-n. Patton               |\n|Birute Zalogajtite-kaledene|\n|Ali Saidi-sief             |\n+---------------------------+\nonly showing top 20 rows\n\n"
     ]
    }
   ],
   "source": [
    "spark.table(\"silver_athlete\")\\\n",
    "     .select(\"Name\")\\\n",
    "     .distinct()\\\n",
    "     .filter(\"Name LIKE '%,%' OR Name LIKE '%..%' OR Name LIKE '%-%'\")\\\n",
    "     .show(truncate=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3b2e5f30-2229-4dd4-a71d-c076b6bc724a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data sample for 'silver_dictionary':\n+---------------+----+----------+----------------+-----------+-----------------------+\n|Country        |Code|Population|GDP_per_Capita  |FirstLetter|Data_Source            |\n+---------------+----+----------+----------------+-----------+-----------------------+\n|Turkey         |TUR |78665830  |9125.68758972936|T          |Olympic Historical Data|\n|Tunisia        |TUN |11107800  |3872.51208364171|T          |Olympic Historical Data|\n|Albania        |ALB |2889167   |3945.21758150914|A          |Olympic Historical Data|\n|Micronesia     |FSM |104460    |3015.23166762397|M          |Olympic Historical Data|\n|Solomon Islands|SOL |583591    |1934.85629287353|S          |Olympic Historical Data|\n+---------------+----+----------+----------------+-----------+-----------------------+\nonly showing top 5 rows\n\nData sample for 'silver_summer':\n+----+--------+---------+-------------+-----------------+-------+------+------------------------------+------+--------------+------------+-----------+-----------------------+\n|Year|City    |Sport    |Discipline   |Athlete          |Country|Gender|Event                         |Medal |Sport_Category|Century     |FirstLetter|Data_Source            |\n+----+--------+---------+-------------+-----------------+-------+------+------------------------------+------+--------------+------------+-----------+-----------------------+\n|1904|St Louis|Boxing   |Boxing       |Oliver L. Kirk   |USA    |M     |52.16 - 56.7KG (Featherweight)|Gold  |Other         |20th Century|U          |Olympic Historical Data|\n|1904|St Louis|Lacrosse |Lacrosse     |Sullivan         |USA    |M     |Lacrosse                      |Silver|Other         |20th Century|U          |Olympic Historical Data|\n|1908|London  |Athletics|Athletics    |Francis C. Irons |USA    |M     |Long Jump                     |Gold  |Track & Field |20th Century|U          |Olympic Historical Data|\n|1908|London  |Cycling  |Cycling Track|Benjamin Jones   |GBR    |M     |1980 Yards Pursuit, Team      |Gold  |Track & Field |20th Century|G          |Olympic Historical Data|\n|1908|London  |Hockey   |Hockey       |Eric Hubert Green|GBR    |M     |Hockey                        |Gold  |Other         |20th Century|G          |Olympic Historical Data|\n+----+--------+---------+-------------+-----------------+-------+------+------------------------------+------+--------------+------------+-----------+-----------------------+\nonly showing top 5 rows\n\nData sample for 'silver_winter':\n+----+---------+----------+--------------------+------------------------------+-------+------+------------+------+--------------+------------+-----------+-----------------------+\n|Year|City     |Sport     |Discipline          |Athlete                       |Country|Gender|Event       |Medal |Sport_Category|Century     |FirstLetter|Data_Source            |\n+----+---------+----------+--------------------+------------------------------+-------+------+------------+------+--------------+------------+-----------+-----------------------+\n|1948|St.Moritz|Skiing    |Cross Country Skiing|Olav Ökern                    |NOR    |M     |4X10KM Relay|Bronze|Winter Sports |20th Century|N          |Olympic Historical Data|\n|1952|Oslo     |Ice Hockey|Ice Hockey          |Stig Gunnar Andersson-tvilling|SWE    |M     |Ice Hockey  |Bronze|Winter Sports |20th Century|S          |Olympic Historical Data|\n|1952|Oslo     |Skiing    |Alpine Skiing       |Christian Pravda              |AUT    |M     |Giant Slalom|Silver|Winter Sports |20th Century|A          |Olympic Historical Data|\n|1952|Oslo     |Skiing    |Cross Country Skiing|Magnar Estenstad              |NOR    |M     |50KM        |Bronze|Winter Sports |20th Century|N          |Olympic Historical Data|\n|1964|Innsbruck|Skating   |Figure skating      |Hans Jürgen Bäumler           |EUA    |M     |Pairs       |Silver|Other         |20th Century|E          |Olympic Historical Data|\n+----+---------+----------+--------------------+------------------------------+-------+------+------------+------+--------------+------------+-----------+-----------------------+\nonly showing top 5 rows\n\nData sample for 'silver_country':\n+-----------+-------+----------+------------------+-----------+-----------------------+\n|CountryName|NOCCode|Population|GDP               |FirstLetter|Data_Source            |\n+-----------+-------+----------+------------------+-----------+-----------------------+\n|Poland     |POL    |37999494  |12554.5475536313  |P          |Olympic Historical Data|\n|Syria      |SYR    |18502413  |12882.556130569325|S          |Olympic Historical Data|\n|Gabon      |GAB    |1725292   |8266.4456050624   |G          |Olympic Historical Data|\n|Portugal   |POR    |10348648  |19222.1500764153  |P          |Olympic Historical Data|\n|Pakistan   |PAK    |188924874 |1434.69666504969  |P          |Olympic Historical Data|\n+-----------+-------+----------+------------------+-----------+-----------------------+\nonly showing top 5 rows\n\nData sample for 'silver_athlete':\n+---------+-------------+------+\n|AthleteID|Name         |Gender|\n+---------+-------------+------+\n|1        |- Johnson    |M     |\n|2        |..... Daumain|M     |\n|3        |A Lam Shin   |F     |\n|4        |A. Albert    |M     |\n|5        |A. B. Zumelzu|M     |\n+---------+-------------+------+\nonly showing top 5 rows\n\n"
     ]
    }
   ],
   "source": [
    "for tbl in tables:\n",
    "    print(f\"Data sample for '{tbl}':\")\n",
    "    spark.table(tbl).show(5, truncate=False)\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "2"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "O_Silver",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}